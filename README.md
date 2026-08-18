# DesarrollAMO · Landings

Repositorio operativo para **landings, sitios simples, plantillas y recursos web reutilizables** del ecosistema DesarrollAMO.

## Estado

**Activo / reutilizable.** Desde agosto de 2026 también contiene la primera puerta de entrada visual al ecosistema.

### Portal del ecosistema

- `index.html` — portada pública inspirada en la arquitectura por “pisos” de EstructurAMO.
- `ecosistema.css` — identidad visual, responsive y componentes del portal.
- `ecosistema.js` — filtros de oficinas, enlaces y animaciones ligeras.
- `oficinas.html` — ficha pública de cada oficina con misión, entradas, entregables y forma de colaborar.

La portada está diseñada para explicar DesarrollAMO a una persona que llega por primera vez sin exigirle conocer DAMO, agentes, modelos o infraestructura.

## Estructura

```text
landings/
├── index.html                 portal DesarrollAMO
├── oficinas.html              mapa de capacidades
├── ecosistema.css             UI compartida del portal
├── ecosistema.js              interacción
├── branding/                  identidad reutilizable
├── clientes/                  proyectos/entregas históricas
└── plantilla_base/            base técnica histórica
```

## Oficinas representadas

La primera versión pública muestra:

- EstructurAMO
- IAMO / DAMO
- DesarrolloAMO
- WebAMO
- DatabaseAMO
- SecurityAMO
- InfraAMO
- OperAMO
- MarketingAMO
- ContaduríaAMO
- InvestigAMO
- CobrAMO
- RagtAMO
- VideAMO
- CamarAMO
- ChoferAMO

Las oficinas son **capacidades organizacionales**, no necesariamente repositorios independientes.

## Branding compartido

`branding/` centraliza progresivamente piezas que antes se copiaban entre proyectos:

- tokens de marca;
- firma HTML/CSS;
- documentación de uso;
- futura base para logos, footer, favicons, Open Graph y componentes.

La definición sigue marcada como provisional hasta reconciliar de forma explícita todos los activos de producción.

## Regla DesarrollAMO

Este repo debe contener **piezas reutilizables**, no secretos ni credenciales de clientes. Datos sensibles, claves de API, tokens, contraseñas y archivos `.env` nunca deben versionarse.

## Relación con el ecosistema

```text
EstructurAMO
     ↓
landings ──→ portal / oficinas / branding
     ↓
WebAMO + MarketingAMO + DesarrolloAMO
     ↓
clientes / productos / presencia pública
```

Sitio principal: https://desarrollamo.com.ar/

---

**DesarrollAMO** · Traducimos tus ideas a tecnología.
