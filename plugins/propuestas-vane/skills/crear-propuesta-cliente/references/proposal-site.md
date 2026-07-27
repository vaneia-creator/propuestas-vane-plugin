# Sitios públicos de propuesta

## Rutas

Crear solo las rutas necesarias:

- `/`: propuesta final o pieza principal;
- `/prototipo`: prototipo web cuando aplique;
- `/auditoria`: auditoría visual cuando aplique;
- `/estrategia`: estrategia cuando aplique;
- `/cuestionario`: formulario solo si se solicita;
- `/admin` y `/admin/respuestas`: panel protegido solo si se necesitan respuestas.

Todas las rutas destinadas al cliente deben abrir sin login. Aplicar `noindex, nofollow` si se desea que sean públicas pero no indexadas.

## Construcción rápida

Usar Sites y reutilizar `assets/proposal-template.html`. Construir primero una portada funcional y publicarla cuando tenga navegación, contenido esencial, responsive básico y enlaces válidos. Añadir después secciones o recursos mediante nuevas versiones.

No construir autenticación, almacenamiento o panel administrativo para una web, auditoría o propuesta que no recopile respuestas.

## Identidad

Usar teal `#0F766E`, tinta `#0D231C`, menta `#CDEFE3`, papel `#F5F7F3` y un acento del cliente. Mantener composición editorial, tarjetas dinámicas, profundidad sutil, firma de Vane, “smile”, destello, animaciones discretas y soporte para movimiento reducido.

Usar la pila manuscrita segura de la plantilla o una fuente aportada expresamente para un proyecto. No empaquetar fuentes privadas.

## Imágenes y videos

Generar imágenes originales cuando resuelvan un vacío visual no factual. Para personas, productos, instalaciones o identidad reales, usar archivos autorizados del cliente.

Copiar recursos aprobados dentro del sitio o usar una URL pública estable. Comprobar reproducción y acceso desde una sesión sin autenticar. Optimizar archivos grandes antes de publicar.

## Cuestionario opcional

Si el sitio recopila respuestas, usar almacenamiento persistente y validación del servidor. No usar `localStorage`.

Solo entonces proteger las rutas administrativas con contraseña fuerte, secretos privados y cookie `HttpOnly`, `Secure` y firmada. La contraseña nunca debe aparecer en HTML, código público o repositorio.

## Información prohibida

No publicar costos internos, márgenes, horas, contraseñas, notas privadas ni información confidencial.
