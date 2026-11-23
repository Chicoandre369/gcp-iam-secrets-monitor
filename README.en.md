# P2 - GCP IAM + Secrets + Monitoring

Read-only auditor for IAM, Secret Manager and Logging in Google Cloud. It only reads, it never changes anything unless you pass `--apply`.

## What it audits
- Accounts with Owner / Editor roles
- Service Accounts with broad roles
- Secrets without rotation
- Audit Logs / IAM-change alerts disabled

## Quick use
```bash
python src/audit_iam.py --project YOUR-GCP-PROJECT --check-only
python src/check_secrets.py --project YOUR-GCP-PROJECT --check-only
```
