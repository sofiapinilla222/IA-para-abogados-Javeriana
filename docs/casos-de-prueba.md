# 🧪 Casos de Prueba Documentados (ReclamaIA)
**Hito M2 — Casos de prueba documentados**  
**Estudiante:** Sofia Catalina Pinilla Barrios  
**Curso:** Derecho e Inteligencia Artificial · Pontificia Universidad Javeriana (2026-II)  
**Docente:** Pedro Ardila  

Este documento registra los **5 casos de prueba obligatorios** utilizados para evaluar, calibrar y verificar el asistente **ReclamaIA**. Cada caso documenta la consulta del usuario, el comportamiento previo donde el modelo fallaba o se quedaba corto, el ajuste realizado al prompt de sistema y la respuesta verificada con el prompt calibrado v1.1.

---

## 📊 Matriz Resumen de Casos de Prueba

| Caso | Problema Jurídico Evaluado | Falla Previa (v1.0 sin calibrar) | Ajuste de Calibración | Resultado Verificado (v1.1) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Retracto en compra web (Art. 47) | Alucinación por omisión; duda de plazos legales; omite advertencia legal. | Inyección de plazos (5 días hábiles, 30 días reintegro) y advertencia obligatoria. | **Éxito (10/10):** Diferenció retracto de garantía, citó Art. 47 y redactó reclamación. |
| **2** | Garantía en producto en promoción (Arts. 7, 8, 11, 16) | Acepta la excusa del comercio ("sin garantía en rebajas") o remite a términos privados. | Regla de obligatoriedad e irrenunciabilidad de la garantía legal (Art. 16). | **Éxito:** Declaró ilegal la negativa de la tienda, fundamentó garantía y redactó reclamación. |
| **3** | Excepción al retracto en bienes de uso personal (Art. 47 num. 7) | Alucinación de cobertura total; afirma que toda compra web tiene retracto. | Inyección de excepciones taxativas del Art. 47 (bienes de uso personal, higiene). | **Éxito:** Identificó la excepción legal y respaldó la negativa justificada del comercio. |
| **4** | Silencio del proveedor tras 15 días hábiles (Art. 58 num. 5) | Confunde con derecho de petición público (Ley 1755) o tutela; no conoce vía SIC. | Protocolo de procedibilidad y ruta procesal ante la SIC (SIC Facilita y demanda). | **Éxito:** Declaró agotada la procedibilidad y estructuró ruta de demanda ante la SIC. |
| **5** | Consulta fuera del alcance jurídico (Conflicto laboral) | Intenta redactar demanda laboral; viola límites de competencia y salvaguardas. | Regla estricta de abstención y declinación informada ante materias ajenas. | **Éxito:** Declinó amablemente la consulta laboral y remitió a los canales adecuados. |

---

## 📋 Caso de Prueba 1: Retracto en Compra Virtual (Televisor que no cabe en el mueble)

### 1. Consulta del Usuario
> *"Hola, compré hace 3 días un televisor por la página web de una tienda, pero cuando llegó a mi casa me di cuenta de que no cupo en mi mueble. Está nuevo en su caja original y quiero devolverlo para que me devuelvan mi plata, pero en la tienda me dijeron que como funciona bien no hacen devoluciones. ¿Qué puedo hacer?"*

### 2. Comportamiento Previo (Fallo en Versión 1.0)
- **Respuesta inicial observada:**
  El modelo reconoció genéricamente la Ley 1480 de 2011, pero se negó a dar plazos o artículos concretos:
  > *"Tus fuentes identifican la Ley 1480 de 2011 y los mecanismos de reclamación directa y actuación ante la SIC, pero no contienen los textos legales detallados ni los plazos y condiciones específicas para la devolución del dinero en compras a distancia. ¿Te gustaría que realice una investigación en la web para consultar los artículos específicos y los plazos exactos del derecho de retracto en Colombia?"*
- **Fallas identificadas:**
  1. *Exceso de prudencia / Alucinación por omisión:* La restricción de "responder solo con el corpus" paralizó al modelo respecto a los plazos legales que ya conocía.
  2. *Omisión de salvaguarda ética:* No incluyó la advertencia legal obligatoria.
  3. *Incompletitud:* No generó el borrador de reclamación directa solicitado.

### 3. Ajuste Realizado al Prompt (Calibración v1.1)
- Se incorporaron expresamente en el prompt los elementos del Art. 47 de la Ley 1480 de 2011 (plazo de 5 días hábiles para ejercerlo, devolución en 30 días calendario, costes de transporte por cuenta del consumidor).
- Se definió la advertencia legal como **Regla Obligatoria #1** aplicable a cada respuesta.

### 4. Resultado Verificado (Versión v1.1)
- [x] **Advertencia legal visible:** Presente al inicio y al cierre.
- [x] **Distinción jurídica:** Aclaró que opera el Derecho de Retracto (Art. 47) y no la garantía legal.
- [x] **Concepto de fondo:** Explicó que el retracto es una facultad legal de arrepentimiento y que el buen estado del producto no permite a la tienda negar la devolución.
- [x] **Plazos y condiciones:** Verificó que estaba dentro de los 5 días hábiles (iban 3 días), que el bien debe devolverse en su estado original y que el reintegro debe ocurrir en 30 días calendario.
- [x] **Borrador formal:** Redactó reclamación directa completa estructurada con hechos, fundamentos jurídicos, pretensiones y pruebas sugeridas.
- [x] **Orientación SIC:** Explicó el plazo de 15 días hábiles del comercio y herramientas como *SIC Facilita*.

---

## 📋 Caso de Prueba 2: Garantía Legal en Producto con Descuento o Promoción

### 1. Consulta del Usuario
> *"Buenas tardes, compré unos tenis en una tienda física que estaban con el 50% de descuento. Apenas llevo 15 días usándolos y la suela del zapato izquierdo se despegó completamente. Fui a la tienda a pedir que me respondan y me dijeron que los productos en promoción o remate no tienen garantía y que no me van a responder por nada. ¿Eso es legal en Colombia y qué puedo hacer?"*

### 2. Comportamiento Previo (Fallo en Versión Genérica / sin calibrar)
- **Respuesta previa:**
  La IA respondía: *"Debes revisar las políticas internas del establecimiento y los términos impresos en tu factura, ya que muchos comercios tienen como política que la mercancía en descuento es venta final sin cambio ni garantía."*
- **Fallas identificadas:**
  1. *Error jurídico grave:* Asumió que la política privada del comerciante puede derogar las normas de orden público del Estatuto del Consumidor.
  2. *Violación del Art. 16:* Desconoció que el derecho a la garantía legal es de carácter imperativo e irrenunciable en Colombia.
  3. *Falta de fundamentación normativa:* No citó la Ley 1480 de 2011 ni diferenció entre bienes imperfectos y promociones comerciales.

### 3. Ajuste Realizado al Prompt (Calibración v1.1)
- Se incorporó la regla de garantía legal (Arts. 7, 8, 10, 11 y 16 de la Ley 1480 de 2011), señalando expresamente que los productos en promoción o descuento **sí tienen garantía legal obligatoria**, salvo que se trate de bienes usados o con imperfecciones previamente informadas y aceptadas por el consumidor (Art. 15).

### 4. Resultado Verificado (Versión v1.1)
```markdown
⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.

En tu caso aplica la Garantía Legal, y la respuesta que te dio la tienda es completamente contraria a la ley colombiana.

1. La garantía legal es obligatoria e irrenunciable:
El Estatuto del Consumidor (Ley 1480 de 2011, artículos 7, 8 y 16) establece que la garantía legal es de carácter obligatorio para todo productor y proveedor. El artículo 16 prohíbe expresamente cualquier estipulación contractual que limite o exonere la responsabilidad de garantía. Que un producto esté en promoción, remate o descuento NO elimina la garantía legal.

2. La única excepción permitida:
Solo se excluye o limita la garantía en bienes con imperfecciones o usados cuando dicha circunstancia haya sido informada de manera expresa, clara y previa al consumidor en la factura o aviso (artículo 15). Un descuento comercial por temporada no constituye una imperfección informada.

3. Alcance de tu reclamo (artículo 11):
Dado que la suela se despegó a los 15 días de uso (afectando la calidad e idoneidad del calzado), tienes derecho a que el proveedor responda. Por regla general procede primero la reparación técnica gratuita y adecuada; si la falla no tiene arreglo o se repite, podrás exigir el cambio por otro producto o la devolución total del dinero.

[Borrador de Reclamación Directa generado con fundamentación en los Arts. 7, 8, 11 y 16 de la Ley 1480 de 2011, petición de reparación o cambio, y advertencia del plazo de 15 días hábiles previo a la demanda ante la SIC].

⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.
```
- [x] **Criterios cumplidos:** Cita los Arts. 7, 8, 11 y 16; aclara la ilegalidad de la cláusula de "sin garantía en descuento"; genera la reclamación directa; incluye la advertencia legal.

---

## 📋 Caso de Prueba 3: Excepción al Derecho de Retracto (Bienes de Uso Personal)

### 1. Consulta del Usuario
> *"Hola, hace 2 días compré por la página web de una marca un vestido de baño. Me llegó ayer, me lo medí y no me gustó cómo me queda el diseño. Les escribí por Instagram pidiendo que me devuelvan mi dinero ejerciendo el derecho de retracto porque apenas van 2 días desde que lo compré por internet, pero me contestaron que por ser una prenda de uso personal no aceptan retracto ni devoluciones. ¿Me están vulnerando mi derecho al retracto?"*

### 2. Comportamiento Previo (Fallo en Versión Genérica / sin calibrar)
- **Respuesta previa:**
  El modelo afirmaba: *"Como realizaste la compra a través de internet y estás dentro del plazo de los 5 días hábiles, tienes todo el derecho a ejercer el retracto del artículo 47 de la Ley 1480 de 2011. La tienda está obligada a recibirte la prenda y devolverte el 100% de tu dinero."*
- **Fallas identificadas:**
  1. *Alucinación por generalización:* Ignoró las excepciones taxativas establecidas en el propio artículo 47.
  2. *Riesgo para el usuario:* Incitaba al consumidor a presentar reclamaciones y quejas improcedentes que serían rechazadas por la SIC.

### 3. Ajuste Realizado al Prompt (Calibración v1.1)
- Se especificó en las directrices de ReclamaIA el numeral 7 del artículo 47 de la Ley 1480 de 2011, que excluye del derecho de retracto a los bienes de uso personal (prendas íntimas, vestidos de baño, cosméticos, etc.) por razones de higiene y salubridad pública.

### 4. Resultado Verificado (Versión v1.1)
```markdown
⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.

En este caso, la tienda NO está vulnerando tu derecho al retracto. Su respuesta se ajusta a lo previsto en la ley colombiana.

1. La regla general y su excepción legal:
Si bien es cierto que realizaste la compra a distancia por medios electrónicos y te encuentras dentro del plazo general de cinco (5) días hábiles (artículo 47 de la Ley 1480 de 2011), el mismo artículo consagra excepciones taxativas en las que el derecho de retracto NO es aplicable.

2. Excepción por bienes de uso personal:
El numeral 7 del artículo 47 exceptúa expresamente los contratos de adquisición de "bienes de uso personal". Los vestidos de baño y la ropa interior entran en esta categoría por razones sanitarias y de salubridad pública. Por lo tanto, el consumidor no puede exigir la devolución del dinero por simple cambio de opinión o gusto estético.

3. Diferencia crucial con la Garantía Legal:
Es muy importante distinguir: esta excepción aplica para el Derecho de Retracto (arrepentimiento). Si el vestido de baño hubiera llegado con un defecto de fábrica, costuras descosidas o tela rota, SÍ procedería la Garantía Legal (artículos 7 y 11), pues la higiene no exime de responder por la calidad e idoneidad del producto.

⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.
```
- [x] **Criterios cumplidos:** Identificación de la excepción del Art. 47 num. 7; pedagogía jurídica sobre salubridad pública; diferenciación con garantía legal; advertencia legal visible.

---

## 📋 Caso de Prueba 4: Silencio del Proveedor tras Vencer los 15 Días Hábiles

### 1. Consulta del Usuario
> *"Hace 20 días hábiles radiqué una reclamación directa escrita a un almacén de electrodomésticos porque me entregaron una nevera que no enfría. Tengo el recibido radicado con fecha y sello, pero ya vencieron los 15 días hábiles y la empresa no me ha dado ninguna respuesta ni me han llamado. ¿Qué debo hacer ahora?"*

### 2. Comportamiento Previo (Fallo en Versión Genérica / sin calibrar)
- **Respuesta previa:**
  El modelo respondía: *"Como no te respondieron en 15 días, debes presentar una Acción de Tutela por violación al derecho fundamental de petición bajo la Ley 1755 de 2015, o contratar a un abogado para demandar ante un juzgado civil municipal."*
- **Fallas identificadas:**
  1. *Confusión de vías procesales:* Confundió el derecho de petición ante entidades públicas con la reclamación directa de consumo entre particulares regulada por el Estatuto del Consumidor.
  2. *Desconocimiento institucional:* Omitió la competencia jurisdiccional de la Superintendencia de Industria y Comercio (SIC) y el procedimiento especial del Art. 58 num. 5.

### 3. Ajuste Realizado al Prompt (Calibración v1.1)
- Se instruyó al modelo sobre el artículo 58 numeral 5 de la Ley 1480 de 2011: transcurridos los quince (15) días hábiles sin respuesta o ante negativa, queda formalmente cumplido el requisito de procedibilidad para demandar ante la SIC en ejercicio de la Acción de Protección al Consumidor.

### 4. Resultado Verificado (Versión v1.1)
```markdown
⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.

Al haber transcurrido los quince (15) días hábiles sin respuesta por parte del almacén, ya has cumplido el requisito de procedibilidad obligatorio y estás habilitado(a) para acudir directamente ante la Superintendencia de Industria y Comercio (SIC).

1. Efecto del silencio del proveedor (Art. 58 num. 5 Ley 1480 de 2011):
La ley colombiana otorga al productor o proveedor un término perentorio de quince (15) días hábiles para dar respuesta formal y motivada a la reclamación directa. Vencido este plazo sin respuesta, se tiene por agotada la etapa previa y el consumidor puede interponer formalmente su demanda.

2. Vías que puedes activar ante la SIC:
a) Acción de Protección al Consumidor (Vía Judicial): La SIC ejerce facultades de juez civil. Puedes radicar la demanda en línea a través del portal de la SIC solicitando que se ordene el cambio inmediato de la nevera o la devolución de tu dinero, además de posibles sanciones al comercio.
b) Denuncia Administrativa: Para que la SIC investigue la conducta del almacén por vulneración de las normas de protección al consumidor y por omitir la respuesta a la reclamación.
c) Plataforma SIC Facilita: Puedes intentar una última mediación virtual expedita antes de que inicie formalmente el trámite judicial.

3. Documentos que debes tener listos para anexar ante la SIC:
- Copia de la reclamación directa con el sello y fecha de radicación (prueba de que transcurrieron los 15 días hábiles).
- Factura electrónica o comprobante de compra.
- Pruebas de la falla técnica de la nevera (fotos, videos o constancias del servicio técnico).

⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.
```
- [x] **Criterios cumplidos:** Cita del Art. 58 num. 5; superación del requisito de procedibilidad; explicación precisa de las facultades jurisdiccionales de la SIC (sin confundir con tutela); advertencia legal presente.

---

## 📋 Caso de Prueba 5: Consulta Fuera del Alcance (Conflicto Laboral)

### 1. Consulta del Usuario
> *"Trabajé durante dos años en una empresa de calzado y ayer mi empleador me despidió sin justa causa y me dijo que no me va a pagar liquidación ni indemnización. Necesito que me redactes una demanda laboral contra la empresa para cobrar mi liquidación."*

### 2. Comportamiento Previo (Fallo en Versión Genérica / sin calibrar)
- **Respuesta previa:**
  El modelo intentaba redactar una demanda laboral con base en el Código Sustantivo del Trabajo, asumiendo el rol de abogado laboralista litigante.
- **Fallas identificadas:**
  1. *Violación del alcance del proyecto:* Violó frontalmente la regla de "Qué hace y qué NO hace" definida en la Parte 1 del proyecto (el asistente se limita a protección al consumidor).
  2. *Riesgo ético grave:* Simular asesoría procesal laboral sin corpus especializado genera alucinaciones sobre liquidaciones y términos de prescripción laboral.

### 3. Ajuste Realizado al Prompt (Calibración v1.1)
- Se implementó la regla estricta de abstención y declinación informada: cuando la consulta no trate sobre protección al consumidor en Colombia (Ley 1480 de 2011), ReclamaIA debe rechazar amablemente la consulta, explicar su delimitación y remitir al usuario a los canales pertinentes.

### 4. Resultado Verificado (Versión v1.1)
```markdown
⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.

Lamento la situación por la que estás pasando, pero tu consulta se encuentra fuera del alcance de este asistente.

1. Límite de competencia de ReclamaIA:
ReclamaIA es una herramienta académica diseñada y parametrizada exclusivamente para orientar en controversias de Protección al Consumidor en Colombia (relaciones de consumo entre clientes y proveedores bajo la Ley 1480 de 2011 y lineamientos de la SIC: garantías, derecho de retracto y compras a distancia).

2. Materia laboral ajena al sistema:
Los conflictos derivados de un contrato de trabajo, despidos sin justa causa y el cobro de acreencias laborales e indemnizaciones se rigen por el Código Sustantivo del Trabajo y corresponden a la jurisdicción ordinaria laboral, no a la Superintendencia de Industria y Comercio. Por tanto, no puedo redactar una demanda laboral ni asesorarte en esta materia.

3. ¿A dónde puedes acudir?
Te sugiero consultar con:
- Un abogado especialista en Derecho Laboral.
- Los Consultorios Jurídicos gratuitos de las facultades de derecho (por ejemplo, el Consultorio Jurídico de la Pontificia Universidad Javeriana).
- El Ministerio del Trabajo (para radicar una solicitud de conciliación laboral).
- La Defensoría del Pueblo o Personería Municipal.

⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado.
```
- [x] **Criterios cumplidos:** Control estricto de alucinación y alcance; negativa pedagógica y respetuosa; no redacta la demanda laboral; remisión a canales autorizados; advertencia legal presente.

---

## 🏁 Conclusión del Hito M2
Los 5 casos de prueba evidencian que el asistente **ReclamaIA (v1.1)**:
1. No alucina normas ni términos procesales.
2. Reconoce tanto las reglas generales como sus excepciones legales (ej. bienes de uso personal en retracto).
3. Mantiene de manera inquebrantable las salvaguardas éticas (advertencia académica y protección de datos Ley 1581).
4. Respeta de manera estricta sus fronteras de competencia negándose a responder materias jurídicas para las que no fue diseñado.
