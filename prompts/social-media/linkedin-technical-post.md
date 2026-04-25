# LinkedIn Technical Post

**Category:** social-media
**When to use:** Sharing a technical insight, lesson, or experience on LinkedIn to build credibility with developers and technical decision-makers.

---

Write a LinkedIn post about a technical topic. LinkedIn rewards authenticity and specificity — the posts that perform best are ones where the author clearly learned something real, not ones that summarize best practices.

Rules for this post:
- **First line is everything:** It must make someone stop scrolling. No "I'm excited to share..." No "Today I learned..." Open with the interesting thing.
- **Specific over general:** Name the actual error, the actual tool, the actual number. "reduced latency by 340ms" beats "improved performance."
- **One insight:** Don't try to say three things. One insight, fully developed.
- **Short paragraphs:** 1–2 sentences max. LinkedIn is read on mobile.
- **No hashtag spam:** Max 3 hashtags, at the end, relevant only.
- **End with a question:** Drives comments. Makes readers feel invited.
- Length: 150–250 words.

**Topic/insight:**
[what you want to write about]

**The most specific, concrete thing you can share:**
[a real example, number, or experience from your work]

**Target reader:**
[who you want to reach with this post]

---

## Example output

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
