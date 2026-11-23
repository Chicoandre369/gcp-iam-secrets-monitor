# P2 - GCP IAM + Secrets + Monitoring

Auditor read-only de IAM, Secret Manager y Logging en Google Cloud. Solo lee, no cambia nada, salvo que uses `--apply` explícitamente.

## Qué audita
- Cuentas con roles Owner / Editor (demasiado privilegio)
- Service Accounts con roles amplios (`roles/owner`, `roles/editor`, `roles/iam.securityAdmin`)
- Secretos en Secret Manager sin rotación o sin etiquetas
- Audit Logs y alertas de cambios IAM desactivados

## Stack
Python, Bash, gcloud CLI, GitHub Actions, Google Cloud (capa gratuita)

## Uso rápido
```bash
# Solo auditoría, no cambia nada
python src/audit_iam.py --project TU-PROYECTO-GCP --check-only

# Ver secretos (sin mostrar valores)
python src/check_secrets.py --project TU-PROYECTO-GCP --check-only
```

## Seguridad
- Nunca imprime valores de secretos
- Nunca usa credenciales reales en el repo, solo variables de entorno / Workload Identity
- Modo `--check-only` por defecto
- Solo tu proyecto, tu lab, con tu autorización

## Estructura
```
src/audit_iam.py - auditoría IAM
src/check_secrets.py - auditoría Secret Manager
scripts/setup_baseline.sh - habilita APIs y logs (requiere --apply)
tests/test_audit.py - tests
.github/workflows/security.yml - CI
docs/setup-gcp.md - paso a paso GCP
```

## Estado
P2 en progreso - MVP: auditoría read-only + CI en verde.
