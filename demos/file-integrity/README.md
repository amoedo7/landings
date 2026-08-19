<div align="center">
  <img src="../../assets/github/multiplatform.svg" width="100%" alt="Herramientas multiplataforma DesarrollAMO" />

# 🔐 File Integrity · SHA-256

**Comprobá que un archivo sea exactamente el mismo, sin subirlo a ningún servicio.**

`Android / Termux` · `Linux` · `macOS` · `Windows` · `Python 3`
</div>

---

## Qué hace

Calcula la huella SHA-256 y el tamaño de un archivo. Las implementaciones Bash, PowerShell y Python comparten un contrato de salida común.

```json
{
  "schema": "desarrollamo.file-integrity.v1",
  "file": "documento.pdf",
  "bytes": 24819,
  "sha256": "...",
  "checked_at": "2026-08-19T00:00:00Z"
}
```

## Ejecutar

| Entorno | Comando |
|---|---|
| Android / Termux · Linux · macOS | `bash check-file.sh ./documento.pdf` |
| Windows PowerShell | `powershell -ExecutionPolicy Bypass -File .\check-file.ps1 .\documento.pdf` |
| Python 3 | `python check_file.py ./documento.pdf` |

## Autoprueba de contrato

```bash
python test_contract.py
```

La prueba crea un archivo temporal y comprueba que implementaciones distintas coincidan en:

`schema` · `sha256` · `bytes` · `file`

El repositorio también ejecuta esta validación en **Ubuntu, macOS y Windows** mediante GitHub Actions.

## Casos de uso

- verificar entregables entre dispositivos;
- validar copias y respaldos;
- comprobar descargas o transferencias;
- generar evidencia simple de integridad;
- comparar archivos sin transmitir su contenido.

```text
archivo local → SHA-256 + tamaño → evidencia verificable
```

**Contrato:** `desarrollamo.file-integrity.v1`

---

[← Volver a DesarrollAMO Labs](../README.md)
