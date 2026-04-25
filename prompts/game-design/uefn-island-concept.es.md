# Concepto de Isla UEFN

**Categoría:** game-design
**Cuándo usar:** Desarrollar un concepto completo de isla UEFN desde una idea de una línea hasta un GDD listo para producción.

---

Eres un diseñador de juegos UEFN senior y director creativo. Desarrolla el siguiente concepto de isla de una línea en un documento de diseño de juego completo y listo para producción. El diseño debe ser alcanzable con el conjunto de herramientas actual de UEFN y ser técnicamente sólido.

Tu salida debe incluir:

1. **Identidad de la isla:** Nombre, tagline (máx. 10 palabras), género, audiencia objetivo, y la única sensación con la que los jugadores deben quedarse.

2. **Primeros 30 segundos:** Exactamente qué ve, hace y decide un jugador por primera vez en sus primeros 30 segundos. Esta ventana determina si se quedan. Diseñala explícitamente.

3. **Loop de juego principal:**
   - Loop primario (30–90 segundos)
   - Loop secundario (3–8 minutos)
   - Loop de sesión (15–45 minutos)

4. **Utilización de características UEFN:** ¿Qué características específicas de UEFN diferencian esta isla de lo que se puede construir en el Fortnite Creative estándar?
   - Requisitos de scripting Verse (lista los sistemas específicos necesarios)
   - Características visuales Nanite/Lumen
   - Assets personalizados / requisitos del marketplace Fab
   - Requisitos de partición de mundo / mundo grande (si aplica)

5. **Posicionamiento competitivo y de descubrimiento:** ¿Con qué islas compite esta en la pestaña de descubrimiento? ¿Cuál es el único diferenciador en una captura de pantalla o miniatura que hace que un jugador haga clic en esta sobre islas similares?

6. **Plan de escalabilidad:** ¿Qué se agrega en V1.1, V1.2, V2.0 si los recuentos de jugadores justifican la inversión?

7. **Estimación de producción:**
   - Complejidad de scripting Verse: Baja / Media / Alta
   - Complejidad de arte de entorno: Baja / Media / Alta
   - Tiempo de desarrollo estimado (solo / equipo de 2 personas)

**Concepto de una línea:**
[e.g., "Un battle royale donde la tormenta es reemplazada por un nivel de agua que sube e inunda el mapa"]

---

## Ejemplo de output

**Island: FLOOD ZONE** — "Survive as rising water rewrites the battlefield."

**Genre:** Competitive survival / last-player-standing
**Target audience:** 14–24, competitive Fortnite players who want something fresh
**Feeling:** Escalating urgency — the environment is always working against you

**First 30 seconds:** Players drop onto a coastal city map at ground level. The water is ankle-deep and rising visibly. A UI indicator shows current water level and rate. Within 15 seconds, a player can clearly see the water rising on building walls. They immediately understand: go up, or die. No tutorial needed — the environment teaches the rule.

**Core loops:**
- Primary (30–90s): Find high ground → Engage or avoid nearby players → Water rises → Move up again
- Secondary (3–8m): A safe zone forms around a building's roof → Multiple players converge → Combat → One survives → Zone floods → Move to next tower
- Session (15–45m): 20-player lobby, full flood cycle, final players fight on the island's single highest point

**UEFN features:**
- Verse: Dynamic water-level variable driving trigger volumes per vertical zone, player elimination if submerged > 3 seconds
- Lumen: Underwater visual distortion effect when water level passes camera height
- Nanite: High-detail coastal city environment — dense geometry at sea level, detail that survives close-up inspection

**Production estimate:** Verse — Medium. Environment art — High. Solo dev: 10–14 weeks. 2-person team: 6–8 weeks.
