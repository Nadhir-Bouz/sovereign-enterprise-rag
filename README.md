# Sovereign Enterprise Document AI Platform (RAG)

An on-premise, privacy-focused Enterprise RAG platform designed to run 100% locally without external cloud dependencies.

## Project Vision
To provide enterprise document intelligence while preserving absolute data sovereignty and user privacy.

## Tech Stack (Phase 1)
- **Local AI Runtime**: Ollama
- **Target LLM**: Qwen 2.5 (3B)
- **Environment**: Local execution

---

## Phase 1 Execution & Proof of Work
- [x] Local AI Infrastructure & Core Setup
- [x] Downloaded and verified `qwen2.5:3b` running locally via Ollama CLI.
- [ ] Phase 2: Data Ingestion & Vector Database
- [ ] Phase 3: REST API & Backend Design
- [ ] Phase 4: Modern Enterprise UI
- [ ] Phase 5: Containerized Deployment

### Verification Commands Used
```bash
# Verify Ollama installation
ollama --version

# Run Qwen 2.5 3B model locally
ollama run qwen2.5:3b