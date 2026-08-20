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
- [x] Installed Ollama and verified runtime setup.
- [x] Downloaded and executed `qwen2.5:3b` locally offline.
- [x] Tested native REST API endpoints via cURL/Postman (`http://localhost:11434/api/generate`).
- [x] Created custom `Modelfile` with system prompts tuned for strict, non-hallucinating enterprise RAG answers.
- [x] Verified zero internet connectivity requirement (air-gapped execution).
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

### Phase 1 API Verification

**Testing Local REST API via cURL:**
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:3b",
  "prompt": "Summarize the concept of Open-Source software in 2 sentences.",
  "stream": false
}'

**Building & Testing Custom Sovereign Modelfile: **
# Create custom model from Modelfile configuration
ollama create enterprise-assistant -f ./Modelfile

# Execute interactive test session with system rules applied
ollama run enterprise-assistant "What are your operational rules?"