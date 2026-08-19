<div align="center">
  <img src="../../assets/github/multiplatform.svg" width="100%" alt="MiDispositivo · diagnóstico multiplataforma" />

  # MiDispositivo

  **Tu equipo, tu red y tu ubicación aproximada en un reporte claro.**

  `Android / Termux` · `Windows` · `macOS` · `Linux` · `JSON` · `HTML local`
</div>

---

## Qué hace

MiDispositivo genera un diagnóstico rápido del equipo donde se ejecuta y lo devuelve como JSON con un contrato común:

```text
DISPOSITIVO
├── sistema operativo
├── versión / arquitectura
├── CPU / hilos lógicos
├── memoria
└── disco

RED
├── IP local
├── gateway
└── DNS

ONLINE · opcional
├── IP pública
├── proveedor / ASN
└── ciudad / región / país aproximados por IP
```

La consulta online **no se ejecuta por defecto**. Si se activa, la ubicación es una estimación de la IP pública, no GPS exacto.

## Privacidad por diseño

Por defecto MiDispositivo:

- no consulta un servicio externo;
- no recopila dirección MAC;
- no recopila nombre de Wi-Fi / SSID;
- no solicita GPS;
- no sube un inventario del dispositivo a DesarrollAMO.

La información pública de IP/ubicación sólo se añade al usar `--online` o `-Online`.

---

## Android / Termux · Linux · macOS

```bash
bash midispositivo.sh
```

Con ubicación pública aproximada:

```bash
bash midispositivo.sh --online
```

Guardar reporte:

```bash
bash midispositivo.sh --output reporte.json
```

Requiere Python 3. En Termux:

```bash
pkg install python
```

## Python · multiplataforma

```bash
python midispositivo.py
```

```bash
python midispositivo.py --online --output reporte.json
```

No usa paquetes de Python externos.

## Windows · PowerShell nativo

```powershell
powershell -ExecutionPolicy Bypass -File .\midispositivo.ps1
```

Con IP pública y ubicación aproximada:

```powershell
powershell -ExecutionPolicy Bypass -File .\midispositivo.ps1 -Online -Output reporte.json
```

---

## Contrato

```json
{
  "schema": "desarrollamo.midispositivo.v1",
  "device": {
    "os": "Windows",
    "architecture": "AMD64",
    "logical_cores": 8
  },
  "network": {
    "local_ip": "192.168.1.42",
    "default_gateway": "192.168.1.1"
  },
  "online": {
    "enabled": false
  }
}
```

El objetivo es que Android, Windows, macOS y Linux puedan alimentar el mismo tipo de panel o proceso posterior.

---

## Visor visual

`viewer.html` convierte el JSON en un dashboard local con la identidad de DesarrollAMO.

1. generar `reporte.json`;
2. abrir `viewer.html` en el navegador;
3. seleccionar el archivo;
4. ver sistema, hardware, red y datos online opcionales en tarjetas.

También incluye un ejemplo incorporado para mostrar la interfaz sin revelar datos reales.

---

## Prueba automática

```bash
python test_schema.py
```

El smoke test verifica que el modo por defecto conserve el schema y las garantías básicas de privacidad.

---

## Para qué sirve

- soporte remoto inicial;
- inventario rápido antes de instalar software;
- diagnóstico de compatibilidad;
- entender la red básica de un cliente;
- generar un reporte portable sin capturas manuales;
- demostrar cómo una misma necesidad se resuelve en varios sistemas operativos.

---

<div align="center">

**DesarrollAMO Labs**  
*Un mismo problema. Distintos dispositivos. Un resultado compatible.*

[← Volver al catálogo](../README.md)

</div>
