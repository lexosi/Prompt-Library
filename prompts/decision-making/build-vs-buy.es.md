# Construir vs. Comprar

**Categoría:** decision-making
**Cuándo usar:** Decidir si construir una capacidad o comprarla, con costos ocultos y escenarios de fallo.

---

Eres un ingeniero principal asesorando sobre una decisión de construir vs. comprar. Dame una recomendación concreta — no un marco. Yo proveeré el contexto; tú provees el juicio.

**Capacidad en cuestión:**
[e.g., "base de datos vectorial para nuestro sistema RAG," "servicio de autenticación," "cola de trabajos"]

**Contexto:**
- Qué necesitamos que haga: [requisitos funcionales]
- Escala: [ahora y en 1–2 años]
- Equipo: [quién lo construiría o mantendría]
- Presupuesto: [presupuesto anual aproximado para este componente]
- Tiempo hasta que necesite funcionar: [fecha límite]
- Uso existente en otro lugar de la empresa: [¿hay algo similar ya en uso?]
- Sensibilidad de datos: [¿puede vivir en la nube de un proveedor o debe ser auto-alojado?]

**Responde esto específicamente:**
1. Construir o comprar — y ¿qué producto/librería específico si comprar?
2. El factor decisivo en este contexto que lo inclina hacia un lado.
3. El costo oculto de tu recomendación que debo planificar.
4. Cómo se ve la elección incorrecta 18 meses después — pinta el escenario.
5. Si elijo construir: ¿cuál es la versión mínima que debería reemplazar la solución interina?

---

## Ejemplo de output

**Recommendation:** Buy — use Qdrant (self-hosted, open-source).

**Decisive factor:** Your team of 3 doesn't have the bandwidth to build and maintain a vector index with production reliability, HNSW tuning, and backup/recovery. Qdrant's self-hosted option keeps your data on-premises (satisfying your compliance requirement) while eliminating 3–6 months of building what's already solved.

**Hidden cost:** Qdrant infrastructure management. Someone on your team needs to own the Qdrant cluster — updates, monitoring, disk management as your index grows. Budget 2–4 hours/week of DevOps time. This is dramatically less than building, but it's not zero.

**Wrong choice scenario (build):** 14 months from now, you've shipped a custom vector index that works for your current 100k documents. Your corpus triples to 300k. You need to re-implement HNSW tuning and sharding. One of the two engineers who built it has left. You spend 3 weeks on infrastructure work instead of product. Meanwhile Qdrant added the exact feature you needed natively.

**Minimum build version (if you choose build):** A wrapper around FAISS with a REST API, PostgreSQL for metadata, and daily backups. Nothing more — defer everything else until the FAISS approach actually hits its limits.
