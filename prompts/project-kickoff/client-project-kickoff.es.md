# Kickoff de Proyecto con Cliente

**Categoría:** project-kickoff
**Cuándo usar:** Documento de contrato-de-entendimiento que previene scope creep antes de que comience el trabajo facturado.

---

Escribe un documento de kickoff de cliente que se compartirá con un cliente antes de que comience el trabajo facturado. Este documento es un contrato de entendimiento, no una especificación técnica. Debe ser claro para un lector no técnico.

El documento debe cubrir:

**RESUMEN DEL PROYECTO:** Qué estamos construyendo y por qué. Escrito para el cliente, no para el ingeniero. 2–3 oraciones.

**CÓMO SE VE EL ÉXITO:** Resultados específicos y observables desde la perspectiva del cliente. No "un sistema funcional" — "los usuarios pueden iniciar sesión, crear un perfil y recibir su primer informe en 5 minutos."

**ENTREGABLES:** Una lista explícita de lo que se entregará al final del proyecto. Formato: [ ] elemento — formato — criterio de aceptación.

**LO QUE NO ESTÁ INCLUIDO:** Elementos listados explícitamente que están fuera de alcance. Esta es la sección más importante — los clientes a menudo asumen que cosas están incluidas cuando no lo están.

**CRONOGRAMA:** Fase por fase con fechas. Incluye un hito que requiera revisión/aprobación del cliente en cada fase.

**RESPONSABILIDADES DEL CLIENTE:** Lo que el cliente debe proporcionar o decidir para que el trabajo proceda — assets, credenciales, aprobaciones, ventanas de retroalimentación.

**PLAN DE COMUNICACIÓN:** Con qué frecuencia los actualizarás, a través de qué canal, y qué desencadena una actualización no programada.

**PROCESO DE CAMBIOS:** Cómo se manejan los cambios de alcance — qué requiere un nuevo presupuesto, qué está cubierto.

**Nombre del proyecto:**
[nombre]
**Qué necesita construirse:**
[descripción]
**Tipo de cliente:** [técnico/no técnico]
**Duración del proyecto:** [estimación]

---

## Ejemplo de output

**PROJECT SUMMARY:** We're building an AI-powered customer support chatbot for your e-commerce store. It will handle your 50 most common support questions automatically, reduce your support ticket volume by an estimated 40%, and escalate complex issues to your human team.

**WHAT SUCCESS LOOKS LIKE:**
- Customers get an accurate answer to their question within 10 seconds, 24/7.
- Your support team receives only tickets the bot couldn't handle.
- The bot correctly handles 80%+ of conversations in our initial test period.

**DELIVERABLES:**
- [ ] Deployed chatbot widget — embedded on your website — passes 50-question accuracy test
- [ ] Admin panel — web interface — you can update bot responses without code
- [ ] Handoff integration — Zendesk — bot escalates to human with full conversation context

**WHAT'S NOT INCLUDED:** Mobile app integration, multi-language support, phone/voice channel, email automation, CRM integration beyond Zendesk.

**CLIENT RESPONSIBILITIES:** Provide 50 most common support questions with correct answers by Day 3. Provide Zendesk API credentials by Day 1. Designate one person to review bot responses during the test period.
