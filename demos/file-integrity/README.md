# File Integrity · SHA-256

Una misma verificación de integridad para **Android/Termux, Linux, macOS y Windows**.

La herramienta calcula el SHA-256 y tamaño de un archivo y devuelve el mismo contrato JSON desde Bash, PowerShell o Python.

## Contrato

```json
{"schema":"desarrollamo.file-integrity.v1","file":"documento.pdf","bytes":24819,"sha256":"...","checked_at":"2026-08-19T00:00:00Z"}
```

## Android / Termux · Linux · macOS

```bash
bash check-file.sh ./documento.pdf
```

## Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\check-file.ps1 .\documento.pdf
```

## Python 3 · multiplataforma

```bash
python check_file.py ./documento.pdf
```

## Autoprueba

```bash
python test_contract.py
```

La prueba crea un archivo temporal y verifica que dos implementaciones distintas produzcan el mismo hash, tamaño, nombre y schema.

## Para qué sirve

- comprobar que un archivo llegó sin cambios;
- validar copias y respaldos;
- verificar entregables entre dispositivos;
- generar evidencia simple de integridad sin subir el archivo a ningún servicio.

No transmite el contenido del archivo: sólo calcula datos localmente.
