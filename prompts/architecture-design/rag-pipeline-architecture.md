# RAG Pipeline Architecture

**Category:** architecture-design
**When to use:** Designing a Retrieval-Augmented Generation pipeline from scratch or redesigning one that produces poor retrieval quality.

---

You are an ML systems architect specializing in RAG. Design a production RAG pipeline for the following use case. Be specific — name the actual components, embedding models, vector databases, and chunking strategies you recommend and why.

Your output must include:
1. **Ingestion pipeline:** How documents are loaded, chunked, embedded, and stored. Chunk size rationale. Metadata strategy.
2. **Retrieval strategy:** Semantic search, keyword (BM25), hybrid, or reranking? When and why.
3. **Context assembly:** How retrieved chunks are assembled into the LLM context. Handling of duplicates, ordering, truncation.
4. **Generation:** System prompt structure, how retrieved context is injected, citation format if needed.
5. **Evaluation:** How do you measure retrieval quality (recall, precision) and generation quality (faithfulness, relevance)?
6. **Failure modes:** What breaks first when the corpus grows 10x? When query distribution shifts?

**Use case:**
[describe what users are querying, what the document corpus is, and expected query volume]

**Constraints:**
- Latency: [e.g., < 3 seconds for retrieval + generation]
- Corpus size: [e.g., 50,000 documents, updated daily]
- Stack preference: [e.g., Python, any vector DB]

---

## Example output

**Ingestion:** Chunk at 512 tokens with 64-token overlap using `RecursiveCharacterTextSplitter`. Rationale: matches typical paragraph length without splitting mid-sentence. Embed with `text-embedding-3-small` (cost-efficient, strong retrieval performance). Store in Qdrant with payload fields: `source_url`, `doc_date`, `section_header`.

**Retrieval:** Hybrid search (BM25 + semantic) with Reciprocal Rank Fusion. BM25 handles exact product name matches; semantic handles conceptual queries. Add a cross-encoder reranker (`ms-marco-MiniLM-L-6-v2`) for the top-20 results, return top-5 to context.

**Failure modes:** (1) Corpus growth — embedding quality degrades when chunks from different time periods use different terminology. Mitigate with periodic re-embedding. (2) Query distribution shift — new product names not in training data will miss BM25 but may hit semantic. Monitor BM25 recall independently.
