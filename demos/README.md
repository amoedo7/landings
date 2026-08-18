# DesarrollAMO · Demos públicas

Piezas pequeñas, ejecutables y verificables. La idea es mostrar trabajo real antes que promesas.

## 1. Cross-device URL Check

Comprueba una URL y devuelve un contrato JSON común desde:

- Android / Termux;
- Linux / macOS;
- Windows;
- Python 3 multiplataforma.

➡️ [`cross-device-url-check/`](cross-device-url-check/)

## 2. File Integrity · SHA-256

Calcula hash y tamaño de archivos con el mismo schema desde Bash, PowerShell y Python. Incluye autoprueba de contrato.

➡️ [`file-integrity/`](file-integrity/)

## 3. Browser Data Toolbox

Herramienta visual sin backend para JSON, SHA-256, Base64 e inspección de URLs. Todo el procesamiento ocurre en el navegador.

➡️ [`browser-data-toolbox/`](browser-data-toolbox/)

---

## Criterio

Cada demo nueva debe resolver algo concreto, poder probarse y evitar dependencias innecesarias. Cuando una misma necesidad existe en varios dispositivos, buscamos conservar un contrato de salida común.
