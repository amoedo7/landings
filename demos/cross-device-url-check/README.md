<div align="center">
  <img src="../../assets/github/multiplatform.svg" width="100%" alt="Herramientas multiplataforma DesarrollAMO" />

# 🔗 Cross-device URL Check

**El mismo control HTTP en distintos sistemas, con una salida compatible.**

`Android / Termux` · `Linux` · `macOS` · `Windows` · `Python 3`
</div>

---

## Qué hace

Consulta una URL, registra el estado HTTP y mide el tiempo de respuesta. Cada implementación devuelve el mismo contrato JSON para que el resultado pueda integrarse con otras herramientas sin importar desde qué dispositivo se ejecutó.

```json
{
  "schema": "desarrollamo.url-check.v1",
  "url": "https://desarrollamo.com.ar",
  "status": 200,
  "ok": true,
  "elapsed_ms": 184,
  "checked_at": "2026-08-18T23:00:00Z"
}
```

## Ejecutar

| Entorno | Comando |
|---|---|
| Android / Termux · Linux · macOS | `bash check-url.sh https://desarrollamo.com.ar` |
| Windows PowerShell | `powershell -ExecutionPolicy Bypass -File .\check-url.ps1 https://desarrollamo.com.ar` |
| Python 3 | `python check_url.py https://desarrollamo.com.ar` |

Bash requiere `curl`. La versión Python no usa dependencias externas.

## Qué demuestra

```text
misma necesidad
      ↓
Bash · PowerShell · Python
      ↓
mismo schema JSON
      ↓
resultado integrable
```

Es un patrón útil para monitoreo, soporte y automatizaciones donde conviven distintos equipos.

**Contrato:** `desarrollamo.url-check.v1`

---

[← Volver a DesarrollAMO Labs](../README.md)
