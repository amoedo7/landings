<div align="center">

# 🧰 Browser Data Toolbox

**Una mini herramienta de DesarrollAMO Labs para trabajar con datos sin salir del navegador.**

`JSON` · `SHA-256` · `Base64` · `URL Inspector`

</div>

---

## Qué podés hacer

| Herramienta | Función |
|---|---|
| **JSON** | validar, formatear y minificar |
| **SHA-256** | calcular la huella de un texto mediante Web Crypto |
| **Base64** | codificar y decodificar texto UTF-8 |
| **URL Inspector** | separar protocolo, host, puerto, ruta, query y fragmento |

## Ejecutar

No hay instalación.

1. descargá [`index.html`](index.html);
2. abrilo en un navegador moderno;
3. empezá a usarlo.

También puede servirse con cualquier servidor estático.

```bash
python -m http.server 8080
```

Después abrí `http://localhost:8080`.

## Privacidad por diseño

El procesamiento de esta demo ocurre **en el navegador**. El archivo no necesita backend para analizar el contenido introducido.

- sin cuenta;
- sin base de datos;
- sin dependencias externas para procesar los datos;
- SHA-256 mediante Web Crypto;
- responsive para celular y escritorio.

## Qué demuestra

Una herramienta pequeña no tiene por qué sentirse improvisada. El objetivo de esta demo es combinar:

**función real + interfaz cuidada + infraestructura mínima.**

---

[← Volver a DesarrollAMO Labs](../README.md)
