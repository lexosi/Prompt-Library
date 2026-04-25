# Post Técnico en LinkedIn

**Categoría:** social-media
**Cuándo usar:** Post de LinkedIn de 150-250 palabras con una primera línea específica e insight concreto.

---

Escribe una publicación de LinkedIn sobre un tema técnico. LinkedIn recompensa la autenticidad y la especificidad — las publicaciones que mejor funcionan son aquellas donde el autor claramente aprendió algo real, no las que resumen mejores prácticas.

Reglas para esta publicación:
- **La primera línea es todo:** Debe hacer que alguien deje de desplazarse. No "Estoy emocionado de compartir..." No "Hoy aprendí..." Abre con la cosa interesante.
- **Específico sobre general:** Nombra el error real, la herramienta real, el número real. "reducida la latencia en 340ms" supera a "rendimiento mejorado."
- **Un solo insight:** No intentes decir tres cosas. Un insight, completamente desarrollado.
- **Párrafos cortos:** Máximo 1–2 oraciones. LinkedIn se lee en móvil.
- **Sin spam de hashtags:** Máximo 3 hashtags, al final, solo relevantes.
- **Terminar con una pregunta:** Impulsa comentarios. Hace que los lectores se sientan invitados.
- Longitud: 150–250 palabras.

**Tema/insight:**
[sobre qué quieres escribir]

**La cosa más específica y concreta que puedes compartir:**
[un ejemplo real, número o experiencia de tu trabajo]

**Lector objetivo:**
[a quién quieres llegar con esta publicación]

---

## Ejemplo de output

My Rust agent was processing 8,000 events/sec at 340ms p99. I needed 50,000 events/sec at under 50ms.

The profiling output was a surprise: 60% of the time was in JSON deserialization — not the business logic, not the network, not the database.

I tried two things that didn't work:
— Switching from `Vec<u8>` to `Bytes` for zero-copy reads: 15% improvement
— Adding `rayon` for parallel processing: made it worse (queue contention)

What worked: switching from `serde_json` to `simd-json` for deserialization, then restructuring the batch processing to avoid per-event allocations.

Result: 52,000 events/sec at 38ms p99. Same hardware.

The lesson isn't "use SIMD." The lesson is: profile before you optimize. I was convinced the bottleneck was the network layer until the profiler proved me wrong.

If you've hit similar throughput walls in Rust — what did you find at the bottom of the call graph?

#rust #systemsprogramming #performance
