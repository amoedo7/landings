# Cross-device URL Check

Un mismo control operativo, tres entornos distintos.

Este demo comprueba una URL, mide tiempo de respuesta y devuelve **el mismo JSON** desde:

- Android / Termux, Linux y macOS mediante Bash + `curl`;
- Windows mediante PowerShell;
- cualquier equipo con Python 3.

## Resultado común

```json
{"schema":"desarrollamo.url-check.v1","url":"https://desarrollamo.com.ar","status":200,"ok":true,"elapsed_ms":184,"checked_at":"2026-08-18T23:00:00Z"}
```

## Android / Termux · Linux · macOS

```bash
bash check-url.sh https://desarrollamo.com.ar
```

Requisito: `curl`.

## Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\check-url.ps1 https://desarrollamo.com.ar
```

## Python 3 · multiplataforma

```bash
python check_url.py https://desarrollamo.com.ar
```

No usa dependencias externas.

## Qué demuestra

La interfaz es la misma aunque cambie el dispositivo o el runtime. Esto permite construir monitoreo, automatizaciones y herramientas operativas que produzcan datos compatibles desde equipos diferentes sin obligar al cliente a usar una única plataforma.

`schema: desarrollamo.url-check.v1`
