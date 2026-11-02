#!/usr/bin/env bash
# Upload one image to TokPortal. Replaces `tokportal upload-image-direct`: CLI 0.1.2 sends the file without a
# content type and TokPortal answers UPLOAD_FAILED. Prints the JSON response (storage_path, public_url).
#
#   tp-upload-image.sh <file> <bundle_id> [carousel|profile_picture]   # default: carousel
#   TP_DRY_RUN=1 tp-upload-image.sh …                                  # validate only, nothing stored
set -euo pipefail
: "${TOKPORTAL_API_KEY:?Set TOKPORTAL_API_KEY (a key from app.tokportal.com/developer) in the environment}"
FILE="${1:?image file}"; BUNDLE="${2:?bundle id}"; PURPOSE="${3:-carousel}"
case "${FILE,,}" in *.png) TYPE=image/png;; *.jpg|*.jpeg) TYPE=image/jpeg;; *.webp) TYPE=image/webp;; *.heic) TYPE=image/heic;; *) echo "unsupported image type: $FILE" >&2; exit 2;; esac
DRY=(); [[ "${TP_DRY_RUN:-}" == 1 ]] && DRY=(-H "X-TokPortal-Dry-Run: true")
curl -sS -X POST "${TOKPORTAL_BASE_URL:-https://app.tokportal.com/api/ext}/upload/image/direct" \
  -H "X-API-Key: ${TOKPORTAL_API_KEY}" -H "Accept: application/json" "${DRY[@]}" \
  -F "file=@${FILE};type=${TYPE}" -F "bundle_id=${BUNDLE}" -F "purpose=${PURPOSE}"
echo
