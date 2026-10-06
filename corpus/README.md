# 📚 Corpus Normativo y Documental — ReclamaIA
**Hito M3 — Corpus conectado (RAG)**  
**Proyecto:** ReclamaIA — Asistente Jurídico de Protección al Consumidor en Colombia  
**Estudiante:** Sofia Catalina Pinilla Barrios  
**Curso:** Derecho e Inteligencia Artificial · Pontificia Universidad Javeriana (2026-II)  
**Docente:** Pedro Ardila  

---

## 📌 1. Descripción del Corpus
Este directorio almacena el corpus normativo y doctrinario oficial utilizado como fuente exclusiva de conocimiento para el sistema de Generación Aumentada por Recuperación (**RAG — Retrieval-Augmented Generation**).

El objetivo del corpus es garantizar que el asistente:
1. **Cita textualmente artículos y fuentes oficiales** (Ley 1480 de 2011 y guías SIC).
2. **Evite alucinaciones jurídicas** al limitar su contexto a disposiciones vigentes y verificables.
3. **Reconozca excepciones y términos procesales exactos** (plazo de 5 días de retracto, 30 días de reembolso, 15 días hábiles de respuesta a reclamaciones).

---

## 📂 2. Archivos del Corpus

| Archivo | Fuente Oficial | Contenido Principal | Formato |
| :--- | :--- | :--- | :---: |
| [`ley_1480_de_2011_consumidor.md`](ley_1480_de_2011_consumidor.md) | Congreso de la República / Secretaría del Senado | Estatuto del Consumidor: Arts. 1-5 (Principios y definiciones), Arts. 7-17 (Garantía legal), Arts. 46-51 (Retracto y ventas a distancia), Art. 58 num. 5 (Reclamación directa y vía SIC). | Markdown estructurado |
| [`guias_sic_proteccion_consumidor.md`](guias_sic_proteccion_consumidor.md) | Superintendencia de Industria y Comercio (SIC) | Guía de reclamación directa, plataforma *SIC Facilita*, demanda judicial de protección al consumidor y diferencias con denuncia administrativa. | Markdown estructurado |

---

## ⚖️ 3. Declaración de Datos Públicos y Ética (Parte 6 del Proyecto)
- **Carácter público de las fuentes:** Todos los documentos provienen de fuentes oficiales abiertas del Estado colombiano (Congreso de la República y Superintendencia de Industria y Comercio).
- **Protección de datos personales (Ley 1581 de 2012):** El corpus contiene únicamente textos normativos y guías públicas de libre consulta. No almacena ni procesa datos personales de terceros, expedientes judiciales reservados ni datos sensibles.

---

## ⚙️ 4. Estructura para Indexación RAG
Los archivos han sido formateados en Markdown con encabezados jerárquicos (`#`, `##`, `###`) para facilitar la partición por fragmentos (*chunking*) semánticos durante el proceso de vectorización con LangChain / LlamaIndex:
- **Tamaño de chunk recomendado:** 500 a 800 caracteres o por subtítulo de artículo.
- **Overlap recomendado:** 100 caracteres para preservar la continuidad contextual entre parágrafos y numerales.
- **Metadatos por chunk:** `{ "fuente": "Ley 1480 de 2011", "articulo": "Art. 47", "materia": "Derecho de Retracto" }`.
