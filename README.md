# DesarrollAMO · Landings

Repositorio activo para **presencia web, componentes reutilizables y demos funcionales** de DesarrollAMO.

## Objetivo público

Este repositorio está orientado a clientes y personas que quieren evaluar qué puede construir DesarrollAMO.

La prioridad es mostrar:

- cosas que se pueden abrir;
- código que se puede ejecutar;
- productos desplegados;
- capacidades respaldadas por implementaciones;
- ejemplos compatibles con distintos dispositivos cuando tenga sentido.

Las reglas completas están en [`PUBLIC_POSITIONING.md`](PUBLIC_POSITIONING.md).

## Estructura actual

```text
landings/
├── index.html                  portal público orientado a clientes
├── ecosistema.css              interfaz responsive
├── demos/
│   └── cross-device-url-check/ primera demo multiplataforma
├── branding/                   identidad web reutilizable
├── clientes/                   proyectos/entregas históricas
├── plantilla_base/             base técnica histórica
└── PUBLIC_POSITIONING.md       criterio de publicación pública
```

## Demo funcional: URL Check

El primer ejemplo nuevo implementa la misma tarea y el mismo contrato JSON en tres runtimes:

- Bash + curl para Android/Termux, Linux y macOS;
- PowerShell para Windows;
- Python 3 como alternativa multiplataforma.

```json
{"schema":"desarrollamo.url-check.v1","url":"https://desarrollamo.com.ar","status":200,"ok":true,"elapsed_ms":184}
```

Abrir: [`demos/cross-device-url-check/`](demos/cross-device-url-check/)

## Branding compartido

`branding/` centraliza progresivamente tokens, estilos y piezas reutilizables. La estética debe acompañar a la evidencia funcional, no sustituirla.

## Seguridad

Este repo no debe contener secretos ni credenciales de clientes. Tokens, contraseñas, claves de API, archivos `.env` y datos sensibles nunca deben versionarse.

## Producción

Sitio principal: https://desarrollamo.com.ar/

El contenido de este repositorio no debe asumirse automáticamente como la fuente de producción del dominio principal hasta que esa relación esté documentada y verificada.

---

**DesarrollAMO** · Software · automatización · sistemas
