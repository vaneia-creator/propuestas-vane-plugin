---
name: crear-propuesta-cliente
description: Estudiar rápidamente un cliente desde sus redes, web o una descripción breve; entregar una auditoría útil; crear un prototipo web, estrategia de redes, campaña audiovisual o propuesta HTML dinámica; generar imágenes cuando hagan falta; publicar enlaces públicos sin login y recomendar automáticamente cuánto cobrar en la moneda del cliente. Usar cuando Vane quiera analizar un cliente, ofrecerle un servicio, crear una web, auditar redes, plantear vídeos, preparar una propuesta o calcular un precio.
---

# Crear propuesta de cliente

Resolver primero lo visible y útil. Evitar cuestionarios largos, planes exhaustivos y trabajo invisible. No preparar infraestructura que Vane no haya pedido.

## Entrada rápida

Si la conversación ya contiene un enlace, logo, archivo o descripción del cliente, aprovecharlo y no repetir la pregunta.

Si no existe información previa, hacer primero esta única pregunta:

**¿Tienes redes sociales, página web, información, imágenes, videos o logo del cliente para que pueda identificarlo?**

Según la respuesta:

- **Sí:** pedir en un solo mensaje el enlace o los archivos y preguntar: **¿Qué servicio quieres ofrecerle al cliente?**
- **No:** pedir en un solo mensaje una descripción breve con nombre o tipo de cliente, nicho, actividad, ubicación aproximada y preguntar: **¿Qué servicio quieres ofrecerle?**

No pedir formularios de onboarding. No volver a preguntar información visible en los enlaces o archivos.

Cuando sea posible identificar al cliente, ejecutar `scripts/init_client_project.py`. Si existe `client-brief.json`, continuar desde su estado sin reiniciar.

## Auditoría rápida

Leer `references/research-and-services.md`. Investigar desde el enlace o la descripción suministrada:

- ubicación y mercado;
- presencia digital;
- claridad de la oferta;
- reputación visible;
- competidores relevantes;
- problemas y oportunidades.

Usar investigación mínima suficiente: fuente principal del cliente y hasta dos competidores. Ampliar solo si una decisión concreta sigue sin evidencia.

Entregar inmediatamente:

1. hallazgos prioritarios;
2. qué está bien;
3. qué conviene cambiar;
4. oportunidades accionables;
5. información importante que todavía falta.

Distinguir hechos, inferencias y pendientes. No detener el trabajo por un dato menor.

Después de la auditoría, confirmar una sola decisión de ejecución adaptada al servicio. Ejemplos:

- redes: auditoría, optimización del perfil, estrategia, formatos o campaña;
- web: prototipo de una página;
- audiovisual: campaña, concepto, guion, piezas o pauta;
- combinación: cuál pieza ejecutar primero.

## Ejecución por servicio

### Página web

Crear **un solo prototipo**. No preguntar cuántas variantes hacer.

Analizar la identidad y construir directamente una primera versión funcional con:

- portada clara y visual;
- navegación simple;
- secciones ajustadas al negocio;
- llamadas a la acción;
- diseño editorial exclusivo;
- tarjetas dinámicas y animaciones premium discretas;
- responsive y movimiento reducido.

Preguntar por imágenes o videos solo si mejorarían de forma material el resultado. Indicar si conviene subirlos a la conversación o guardarlos en una carpeta del proyecto. Si todavía no existen, usar recursos temporales adecuados o generar imágenes originales sin bloquear el prototipo.

Usar Sites y publicar la primera versión funcional de inmediato. Entregar el enlace público y preguntar: **¿Quieres dejarla así o qué cambio hacemos?**

### Redes sociales

Analizar perfil, nombre visible, biografía, enlaces, identidad, contenido, formatos, frecuencia, llamadas a la acción y coherencia.

Entregar recomendaciones específicas y, según lo pedido, pilares, formatos, ejemplos, calendario breve o estrategia. Convertir la auditoría o estrategia en un HTML visual, dinámico y fácil de presentar. Publicarlo con enlace público.

### Vídeo y campañas

Proponer el giro creativo adecuado para ese cliente: idea central, audiencia, gancho, oferta, escenas, guion de muestra, formatos, CTA y variantes de pauta.

Codex puede crear conceptos, guiones, storyboards, imágenes de apoyo y piezas visuales. La grabación y edición final de videos debe realizarla Vane o su equipo fuera del plugin.

Indicar que los videos terminados se suban a una carpeta del proyecto o a la conversación. Incorporarlos después al sitio o enlazarlos desde la propuesta pública, comprobando que el cliente pueda abrirlos.

### Imágenes

Usar generación de imágenes cuando haga falta un recurso original para un prototipo, campaña, portada, storyboard o publicación. Pedir una imagen al usuario solo cuando deba representar fielmente al cliente, una persona, un producto o un local real.

No detener un prototipo por falta de una imagen decorativa. Generar una alternativa o usar un placeholder elegante y reemplazable.

## Propuesta final

Cuando haya una o varias piezas aprobadas, reunirlas en una propuesta HTML dinámica basada en `assets/proposal-template.html`.

Incluir solo lo que corresponda:

- contexto y oportunidad;
- auditoría;
- solución;
- estrategia;
- prototipo web;
- campaña o piezas audiovisuales;
- entregables;
- límites;
- próximos pasos;
- enlaces a páginas, videos y recursos creados.

Usar tarjetas, transiciones, animaciones discretas y poco texto por bloque. Mantener la identidad teal de Vane con un acento del cliente. No redistribuir fuentes privadas.

Publicar también la propuesta final. Entregar un enlace público que el cliente pueda abrir sin cuenta, contraseña ni inicio de sesión.

## Publicación

Leer `references/proposal-site.md`.

Publicar sin pedir una aprobación separada cuando Vane haya solicitado crear una web, auditoría HTML o propuesta. La publicación es la forma normal de previsualización y puede actualizarse después.

La propuesta, prototipos, auditorías, estrategias, videos autorizados y cuestionario deben ser públicos para cualquiera que tenga el enlace. Usar `noindex, nofollow` cuando convenga evitar indexación.

Solo `/admin` y `/admin/respuestas`, si llegan a necesitarse, deben requerir contraseña. No crear panel, login, D1 ni cuestionario salvo que el proyecto realmente los necesite.

Nunca publicar precios internos, contraseñas, márgenes, horas ni notas privadas.

## Velocidad obligatoria

- Empezar a investigar o construir después de la entrada rápida; no redactar primero un plan largo.
- Agrupar búsquedas y llamadas independientes.
- Limitar la auditoría inicial a la evidencia necesaria para decidir.
- Reutilizar la plantilla y componentes existentes.
- Para web, construir primero la portada funcional; añadir el resto sobre esa base.
- No crear múltiples conceptos salvo petición expresa.
- No construir paneles, bases de datos, cuestionarios o rutas administrativas por defecto.
- Mostrar un hallazgo o resultado concreto durante el trabajo; no permanecer en silencio mientras se estructura todo.
- Si una herramienta o enfoque no produce progreso en aproximadamente dos minutos, informar el bloqueo y cambiar a una alternativa más simple.
- Preferir una primera versión pública, correcta y editable a una versión enorme que tarde demasiado en aparecer.
- Probar únicamente lo crítico antes de la primera publicación: carga, móvil básico, enlaces principales y acceso público. Completar el control exhaustivo al cerrar la versión final.

## Precio recomendado obligatorio

Después de entregar o publicar la primera ejecución, calcular automáticamente cuánto puede cobrar Vane por ese trabajo. No esperar a que ella lo pida y no retrasar el prototipo para realizar el cálculo.

Leer `references/pricing.md`. Detectar el país y la moneda desde los enlaces, la ubicación investigada o la descripción. Preguntar el país únicamente si no se puede determinar y es indispensable para escoger la moneda.

Investigar referencias actuales del mercado local y entregar en números:

- alcance valorado y supuestos;
- rango habitual del mercado;
- precio bajo;
- **precio recomendado**;
- precio alto;
- costos externos o inversión estimada;
- moneda del cliente y equivalente en USD;
- fuentes y fecha del tipo de cambio.

Usar estimaciones razonables cuando falten horas o costos menores, declarando los supuestos en lugar de abrir otro cuestionario. Guardar el resultado en `private/pricing.md`.

Mantener el precio privado para Vane. No ponerlo en la propuesta pública salvo petición explícita.

## Control

Actualizar `client-brief.json` con uno de estos estados:

`intake_complete`, `audit_delivered`, `execution_selected`, `prototype_published`, `final_proposal_published`, `priced`.

Ejecutar `scripts/validate_client_brief.py` antes de una publicación final. Leer `references/quality-checklist.md` para cerrar la entrega, sin convertir la comprobación en un bloqueo para el primer prototipo.

## Recursos

- `scripts/init_client_project.py`: crear el expediente y copiar la plantilla.
- `scripts/validate_client_brief.py`: validar estado y privacidad.
- `references/research-and-services.md`: investigación rápida y ramas de servicio.
- `references/proposal-site.md`: diseño, publicación pública y seguridad opcional.
- `references/pricing.md`: estimación privada.
- `references/quality-checklist.md`: revisión esencial y final.
- `assets/proposal-template.html`: base visual reutilizable.
