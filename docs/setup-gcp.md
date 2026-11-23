# Setup GCP para P2 - Paso a paso

## 1. Crear proyecto lab (capa gratuita)
- Ve a console.cloud.google.com
- Crea proyecto, ej: `p2-iam-lab`

## 2. Autenticar local
```bash
gcloud auth login
gcloud config set project p2-iam-lab
```

## 3. Probar auditoría (read-only)
```bash
python src/audit_iam.py --project p2-iam-lab --check-only
python src/check_secrets.py --project p2-iam-lab --check-only
```

## 4. Baseline (opcional)
```bash
./scripts/setup_baseline.sh p2-iam-lab --apply
```

## Seguridad
- Usa solo tu proyecto lab
- Nunca subas `service-account.json` ni secretos al repo
- En GitHub Actions usa Workload Identity, no claves JSON
