# Threat Model P2
- Activo: IAM, secretos, logs en GCP
- Amenaza: cuenta con Owner/Editor, secreto sin rotación, logs desactivados
- Mitigación: auditoría read-only, mínimo privilegio, alertas IAM, rotación
- Alcance: solo tu proyecto lab, con tu autorización
