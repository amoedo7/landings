# DesarrollAMO · Landings

Repositorio activo para **presencia web, componentes reutilizables y demos funcionales** de DesarrollAMO.

## Qué queremos demostrar

Este repositorio está orientado a clientes y personas que quieren evaluar qué puede construir DesarrollAMO.

La prioridad es mostrar:

- herramientas que se pueden abrir o ejecutar;
- código pequeño pero útil;
- soluciones compatibles con distintos dispositivos;
- contratos de salida consistentes;
- pruebas automáticas cuando aportan confianza;
- productos desplegados sólo cuando existe respaldo real.

## Demos funcionales

| Demo | Qué hace | Entornos |
|---|---|---|
| [Cross-device URL Check](demos/cross-device-url-check/) | estado HTTP + tiempo de respuesta con JSON común | Android/Termux, Linux, macOS, Windows, Python |
| [File Integrity · SHA-256](demos/file-integrity/) | hash + tamaño de archivo con contrato común | Android/Termux, Linux, macOS, Windows, Python |
| [Browser Data Toolbox](demos/browser-data-toolbox/) | JSON, SHA-256, Base64 e inspección de URL | navegador moderno |

➡️ **[Abrir catálogo completo de demos](demos/)**

## Validación automática

El workflow `.github/workflows/demos-ci.yml` ejecuta la prueba de contrato de File Integrity en:

- Ubuntu;
- macOS;
- Windows.

La prueba verifica que implementaciones distintas devuelvan el mismo hash, tamaño, nombre de archivo y schema.

## Estructura

```text
landings/
├── index.html
├── ecosistema.css
├── demos/
│   ├── README.md
│   ├── cross-device-url-check/
│   ├── file-integrity/
│   └── browser-data-toolbox/
├── branding/
├── clientes/
├── plantilla_base/
└── .github/workflows/demos-ci.yml
```

## Seguridad

Este repo no debe contener secretos ni credenciales de clientes. Tokens, contraseñas, claves de API, archivos `.env` y datos sensibles nunca deben versionarse.

## Producción

Sitio principal: https://desarrollamo.com.ar/

El contenido de este repositorio no debe asumirse automáticamente como la fuente de producción del dominio principal hasta que esa relación esté documentada y verificada.

---

**DesarrollAMO** · Software · automatización · sistemas
