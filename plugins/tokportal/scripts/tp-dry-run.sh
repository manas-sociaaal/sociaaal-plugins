#!/usr/bin/env bash
# Dry-run any TokPortal write before doing it for real. The CLI (@tokportal/cli 0.1.2) has no dry-run flag, so this
# sends the same request with `X-TokPortal-Dry-Run: true`: full validation and the real price, nothing created,
# no credits debited. The response carries `dry_run: true` and `credits_would_charge`.
#
#   tp-dry-run.sh POST /bundles bundle.json                       # JSON body from a file
#   tp-dry-run.sh PUT  /bundles/<id>/videos/1 slot.json
#   tp-dry-run.sh POST /bundles/<id>/videos/1/publish             # no body
#   tp-dry-run.sh POST /upload/image/direct --image 01.png <bundle_id>   # multipart image upload
set -euo pipefail
: "${TOKPORTAL_API_KEY:?Set TOKPORTAL_API_KEY (a key from app.tokportal.com/developer) in the environment}"
BASE="${TOKPORTAL_BASE_URL:-https://app.tokportal.com/api/ext}"
METHOD="${1:?method}"; PATH_="${2:?path, e.g. /bundles}"; shift 2
H=(-H "X-API-Key: ${TOKPORTAL_API_KEY}" -H "X-TokPortal-Dry-Run: true" -H "Accept: application/json")
if [[ "${1:-}" == "--image" ]]; then
  curl -sS -X "$METHOD" "${BASE}${PATH_}" "${H[@]}" -F "file=@${2:?image file}" -F "bundle_id=${3:?bundle id}" -F "purpose=carousel"
elif [[ -n "${1:-}" ]]; then
  curl -sS -X "$METHOD" "${BASE}${PATH_}" "${H[@]}" -H "Content-Type: application/json" --data-binary "@$1"
else
  curl -sS -X "$METHOD" "${BASE}${PATH_}" "${H[@]}"
fi
echo
