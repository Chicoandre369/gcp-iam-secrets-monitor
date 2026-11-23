#!/bin/bash
# P2 - Baseline seguro en GCP. Requiere --apply, si no, solo muestra lo que haría.
set -euo pipefail
PROJECT="${1:-}"
if [ -z "$PROJECT" ]; then
  echo "Uso: ./scripts/setup_baseline.sh TU-PROYECTO-GCP --apply"
  echo "Sin --apply no cambia nada, solo muestra el plan."
  exit 1
fi
APPLY=false
if [ "${2:-}" = "--apply" ]; then APPLY=true; fi
echo "[*] Proyecto: $PROJECT - apply: $APPLY"
echo "[*] APIs a habilitar: iam.googleapis.com secretmanager.googleapis.com logging.googleapis.com monitoring.googleapis.com"
if [ "$APPLY" = false ]; then
  echo "[check-only] No se cambió nada. Agrega --apply para aplicar."
  exit 0
fi
echo "[*] Habilitando APIs..."
gcloud services enable iam.googleapis.com secretmanager.googleapis.com logging.googleapis.com monitoring.googleapis.com --project="$PROJECT"
echo "[OK] Baseline aplicado"
