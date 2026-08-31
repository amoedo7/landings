# Recuperación de landings

Este procedimiento cubre únicamente la superficie pública mantenida por `amoedo7/landings`. No autoriza cambios en pagos, StoreAMO, firmas, secretos ni otras piezas del ecosistema.

## Objetivo

Volver a una revisión conocida y verificable cuando una publicación, demo o cambio de contenido cause una regresión observable.

## Recuperación

1. Identificar el último commit de `main` que haya pasado `bash scripts/autocheck.sh` y el workflow `demos-ci`.
2. Comparar el cambio defectuoso contra ese commit y revertir sólo los commits responsables; no reescribir historial compartido.
3. Ejecutar `bash scripts/autocheck.sh` sobre el candidato de recuperación.
4. Publicar/conservar el rollback sólo cuando el gate determinista pase.
5. Comprobar por separado la URL o despliegue externo afectado. Un CI verde no demuestra accesibilidad externa.
6. Registrar en GitHub el commit restaurado, el gate ejecutado y cualquier comprobación externa disponible.

## Límites de evidencia

- Si `demos-ci` o el AutoCheck no llegan a ejecutarse, el estado es `UNKNOWN`, no `PASS`.
- Si no se puede comprobar el despliegue externo, registrar esa dimensión como `UNKNOWN` aunque el repositorio esté saludable.
- No afirmar restauración de producción sólo por haber revertido código.

## Escalado

Si la recuperación requiere cambiar credenciales, DNS, hosting, pagos, StoreAMO o cualquier frontera fuera de `landings`, detener el cambio local y abrir/usar el scope correspondiente con sus propios gates.
