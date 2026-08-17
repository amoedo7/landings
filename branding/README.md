# DesarrollAMO Branding

Fuente reutilizable de identidad para los sitios y landings del ecosistema DesarrollAMO.

> Estado: **v1 provisional**. Se centraliza lo que ya existe en GitHub sin afirmar todavía que reproduce pixel-perfect el branding de producción. La identidad visual definitiva debe validarse contra `desarrollamo.com.ar` antes de marcarla como canónica.

## Objetivo

Evitar copiar y pegar branding diferente en cada proyecto.

Los proyectos pueden consumir estas piezas como referencia y mantener una firma visual consistente:

- `brand.json` — tokens y metadatos de marca.
- `amo-branding.html` — firma HTML mínima y accesible.
- `amo-branding.css` — estilos aislados para la firma.

## Uso básico

```html
<link rel="stylesheet" href="/branding/amo-branding.css">

<footer>
  <span>Proyecto desarrollado por</span>
  <!-- copiar aquí el contenido de amo-branding.html -->
</footer>
```

La firma está deliberadamente separada del texto del footer. Así cada proyecto puede decir `Desarrollado por`, `Tecnología por`, `Un proyecto de` o el copy que corresponda, sin duplicar la identidad de marca.

## Principios

1. **Una fuente de verdad.** Los cambios de identidad se realizan aquí y después se propagan.
2. **Sin dependencias.** HTML + CSS, para que funcione en sitios estáticos, React, Vite o cualquier landing simple.
3. **Accesible.** Texto real, foco visible y enlace con nombre comprensible.
4. **No invasivo.** Las clases usan el prefijo `amo-branding` para evitar colisiones.
5. **Versionable.** Los cambios incompatibles deben generar una nueva versión del componente.

## Siguiente evolución

Cuando auditemos el branding actualmente publicado en los sitios de producción, este directorio puede convertirse en el paquete oficial con:

- logo SVG oficial;
- paleta canónica light/dark;
- tipografías y escalas;
- favicon y Open Graph assets;
- footer completo;
- botones y badges;
- tokens CSS/JSON;
- ejemplos para HTML, React y Android;
- guía de uso y de no-uso de la marca.
