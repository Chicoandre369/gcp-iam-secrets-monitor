#!/usr/bin/env python3
"""P2 - Auditor read-only de IAM en GCP. No cambia nada. No muestra secretos."""
import argparse
import json
import subprocess
import sys

RIESGOSOS = {
    "roles/owner",
    "roles/editor",
    "roles/iam.organizationAdmin",
    "roles/iam.securityAdmin",
    "roles/iam.serviceAccountKeyAdmin",
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if r.returncode != 0:
        print(f"[ERROR] {' '.join(cmd)}")
        print(r.stderr[:2000])
        return None
    return r.stdout

def main():
    ap = argparse.ArgumentParser(description="Audita IAM en GCP (read-only)")
    ap.add_argument("--project", required=True, help="ID del proyecto GCP, ej: mi-proyecto-lab")
    ap.add_argument("--check-only", action="store_true", default=True)
    args = ap.parse_args()

    print(f"[*] Auditando IAM - proyecto: {args.project} - modo: check-only")
    out = run(["gcloud", "projects", "get-iam-policy", args.project, "--format=json"])
    if out is None:
        print("[WARN] No se pudo leer la política IAM. ¿Hiciste gcloud auth login y tienes permisos?")
        return 1

    policy = json.loads(out)
    hallazgos = []
    for b in policy.get("bindings", []):
        rol = b.get("role", "")
        miembros = b.get("members", [])
        if rol in RIESGOSOS:
            for m in miembros:
                hallazgos.append(f"[WARN] {m} tiene rol riesgoso {rol}")
                print(f"[WARN] {m} tiene rol riesgoso {rol}")
        if rol == "roles/owner" and len(miembros) > 2:
            print(f"[WARN] Demasiados Owners: {len(miembros)}")

    if not hallazgos:
        print("[OK] No se encontraron roles Owner/Editor en bindings revisados")
    else:
        print(f"[*] Hallazgos: {len(hallazgos)} - revisa y aplica mínimo privilegio")

    print("[OK] Auditoría terminada, no se cambió nada")
    return 0

if __name__ == "__main__":
    sys.exit(main())
