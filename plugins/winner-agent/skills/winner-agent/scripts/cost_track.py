#!/usr/bin/env python3
"""Lightweight SQLite for tracking Winner Agent run costs over time.

Usage:
  cost_track.py start <app> <week>           -> prints run_id
  cost_track.py log <run_id> <kind> <usd>    -> log a cost entry
  cost_track.py finish <run_id>              -> close run
  cost_track.py report [days=30]             -> summary by app

DB lives at ~/.claude/skills/winner-agent/data/runs.db (auto-created).
"""

import sqlite3
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "runs.db"
DB.parent.mkdir(parents=True, exist_ok=True)

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id TEXT PRIMARY KEY, app TEXT, week TEXT,
    started_at TEXT, finished_at TEXT, total_cost REAL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS cost_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT, kind TEXT, usd REAL, at TEXT
);
"""


def conn():
    c = sqlite3.connect(str(DB))
    c.executescript(SCHEMA)
    return c


def cmd_start(app, week):
    rid = str(uuid.uuid4())[:8]
    with conn() as c:
        c.execute("INSERT INTO runs (id, app, week, started_at) VALUES (?, ?, ?, ?)",
                  (rid, app, week, datetime.utcnow().isoformat()))
    print(rid)


def cmd_log(run_id, kind, usd):
    usd = float(usd)
    with conn() as c:
        c.execute("INSERT INTO cost_entries (run_id, kind, usd, at) VALUES (?, ?, ?, ?)",
                  (run_id, kind, usd, datetime.utcnow().isoformat()))
        c.execute("UPDATE runs SET total_cost = total_cost + ? WHERE id = ?", (usd, run_id))
    print(f"logged ${usd:.4f} {kind} to {run_id}")


def cmd_finish(run_id):
    with conn() as c:
        c.execute("UPDATE runs SET finished_at = ? WHERE id = ?",
                  (datetime.utcnow().isoformat(), run_id))
    print(f"finished {run_id}")


def cmd_report(days=30):
    cutoff = (datetime.utcnow() - timedelta(days=int(days))).isoformat()
    with conn() as c:
        c.row_factory = sqlite3.Row
        rows = c.execute(
            """SELECT app, COUNT(*) as runs, SUM(total_cost) as total
               FROM runs WHERE started_at >= ? GROUP BY app ORDER BY total DESC""",
            (cutoff,),
        ).fetchall()
    print(f"Cost report (last {days} days)")
    print(f"{'App':15} {'Runs':>6} {'Total $':>10}")
    for r in rows:
        print(f"{r['app']:15} {r['runs']:>6} ${r['total'] or 0:>9.2f}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "start": cmd_start(sys.argv[2], sys.argv[3])
    elif cmd == "log": cmd_log(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "finish": cmd_finish(sys.argv[2])
    elif cmd == "report": cmd_report(sys.argv[2] if len(sys.argv) > 2 else 30)
    else: print(f"unknown command: {cmd}"); sys.exit(1)
