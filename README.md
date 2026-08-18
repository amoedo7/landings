# DesarrollAMO · Landings

Repositorio operativo para **landings, sitios simples, plantillas y recursos web reutilizables** del ecosistema DesarrollAMO.

## Estado

**Activo como infraestructura histórica/reutilizable.** No debe interpretarse como inventario completo de todos los sitios actualmente desplegados en Netlify.

## Estructura actual

- `clientes/` — proyectos o entregas guardadas dentro de este repositorio.
- `plantilla_base/` — base técnica histórica para landings.
- `branding/` — inicio de la fuente reutilizable de identidad DesarrollAMO.
- `index.html` — dashboard/entrada histórica del repositorio.

## Branding compartido

`branding/` centraliza progresivamente piezas que antes se copiaban entre proyectos:

- tokens de marca;
- firma HTML/CSS;
- documentación de uso;
- futura base para logos, footer, favicons, Open Graph y componentes.

La versión actual está marcada como provisional hasta contrastarla con los sitios de producción.

## Regla DesarrollAMO

Este repo debe contener **piezas reutilizables**, no secretos ni credenciales de clientes. Datos sensibles, claves de API, tokens, contraseñas y archivos `.env` nunca deben versionarse.

## Relación con el ecosistema

```text
landings
├── sitios / entregas históricas
├── plantilla_base
└── branding
        ↓
 futuros sitios y herramientas web DesarrollAMO
```

Sitio principal: https://desarrollamo.com.ar/

---

**DesarrollAMO** · tecnología, automatización e IA orientadas a convertir ideas en herramientas utilizables.
