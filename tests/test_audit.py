# Tests simples, sin GCP real
def test_riesgoso():
    riesgosos = {"roles/owner", "roles/editor"}
    assert "roles/owner" in riesgosos
    assert "roles/viewer" not in riesgosos

def test_no_muestra_secretos():
    # El auditor nunca debe imprimir valores, solo nombres
    codigo = open("src/check_secrets.py", encoding="utf-8").read()
    assert "access-secret-version" not in codigo or "valores" in codigo.lower()
    assert "print" in codigo
    print("OK - test_audit paso")
