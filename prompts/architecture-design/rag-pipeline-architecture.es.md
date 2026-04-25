# Arquitectura de Pipeline RAG

**Categoría:** architecture-design
**Cuándo usar:** Diseñar un pipeline RAG en producción con modelos de embedding específicos, estrategia de recuperación y evaluación.

---

Eres un arquitecto de sistemas ML especializado en RAG. Diseña un pipeline RAG de producción para el siguiente caso de uso. Sé específico — nombra los componentes reales, modelos de embedding, bases de datos vectoriales y estrategias de chunking que recomiendas y por qué.

Tu salida debe incluir:
1. **Pipeline de ingesta:** Cómo se cargan, fragmentan, embeben y almacenan los documentos. Justificación del tamaño de chunk. Estrategia de metadatos.
2. **Estrategia de recuperación:** ¿Búsqueda semántica, keyword (BM25), híbrida o reranking? ¿Cuándo y por qué?
3. **Ensamblaje de contexto:** Cómo se ensamblan los chunks recuperados en el contexto del LLM. Manejo de duplicados, ordenamiento, truncamiento.
4. **Generación:** Estructura del system prompt, cómo se inyecta el contexto recuperado, formato de citas si es necesario.
5. **Evaluación:** ¿Cómo mides la calidad de recuperación (recall, precisión) y la calidad de generación (fidelidad, relevancia)?
6. **Modos de fallo:** ¿Qué falla primero cuando el corpus crece 10x? ¿Cuando la distribución de consultas cambia?

**Caso de uso:**
[describe qué consultan los usuarios, cuál es el corpus de documentos y el volumen de consultas esperado]

**Restricciones:**
- Latencia: [e.g., < 3 segundos para recuperación + generación]
- Tamaño del corpus: [e.g., 50,000 documentos, actualizados diariamente]
- Preferencia de stack: [e.g., Python, cualquier vector DB]

---

## Ejemplo de output

**Ingestion:** Chunk at 512 tokens with 64-token overlap using `RecursiveCharacterTextSplitter`. Rationale: matches typical paragraph length without splitting mid-sentence. Embed with `text-embedding-3-small` (cost-efficient, strong retrieval performance). Store in Qdrant with payload fields: `source_url`, `doc_date`, `section_header`.

**Retrieval:** Hybrid search (BM25 + semantic) with Reciprocal Rank Fusion. BM25 handles exact product name matches; semantic handles conceptual queries. Add a cross-encoder reranker (`ms-marco-MiniLM-L-6-v2`) for the top-20 results, return top-5 to context.

**Failure modes:** (1) Corpus growth — embedding quality degrades when chunks from different time periods use different terminology. Mitigate with periodic re-embedding. (2) Query distribution shift — new product names not in training data will miss BM25 but may hit semantic. Monitor BM25 recall independently.
