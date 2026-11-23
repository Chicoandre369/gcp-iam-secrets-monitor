#!/usr/bin/env python3
"""P2 - Auditor de Secret Manager. Nunca imprime valores de secretos."""
import argparse
import subprocess
import sys
import json

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if r.returncode != 0:
        print(r.stderr[:2000])
        return None
    return r.stdout

def main():
    ap = argparse.ArgumentParser(description="Audita Secret Manager sin mostrar valores")
    ap.add_argument("--project", required=True)
    ap.add_argument("--check-only", action="store_true", default=True)
    args = ap.parse_args()
    print(f"[*] Auditando Secret Manager - proyecto: {args.project}")
    out = run(["gcloud", "secrets", "list", "--project", args.project, "--format=json"])
    if out is None:
        print("[WARN] No se pudo listar secretos. ¿Secret Manager API habilitada?")
        return 1
    secrets = json.loads(out)
    if not secrets:
        print("[OK] No hay secretos en este proyecto")
        return 0
    for s in secrets:
        nombre = s.get("name", "sin-nombre")
        # Nunca imprimimos valores, solo nombre y metadata
        print(f"[*] Secreto encontrado: {nombre} - revisa rotación y etiquetas")
        # Opcional: verificar versiones
        v = run(["gcloud", "secrets", "versions", "list", nombre, "--project", args.project, "--format=json"])
        if v:
            vers = json.loads(v)
            print(f"    Versiones: {len(vers)}")
    print("[OK] Auditoría terminada, no se mostró ningún valor secreto")
    return 0

if __name__ == "__main__":
    sys.exit(main())
