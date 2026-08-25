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
- [x] Implemented & verified Python API integration test for custom enterprise model.
- [x] Verified zero internet connectivity requirement (air-gapped execution).
- [ ] Phase 2: Data Ingestion & Vector Database
- [ ] Phase 3: REST API & Backend Design
- [ ] Phase 4: Modern Enterprise UI
- [ ] Phase 5: Containerized Deployment

### Phase 1 Verification Commands Used
**1.CLI Verification & Model Execution**
```bash
# Verify Ollama installation
ollama --version

# Run Qwen 2.5 3B model locally
ollama run qwen2.5:3b
```

**2.Testing Local REST API via cURL:**
```bash
# Verify base model response using the native cURL generate endpoint
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:3b",
  "prompt": "Summarize the concept of Open-Source software in 2 sentences.",
  "stream": false
}'
```

**3.Building & Testing Custom Sovereign Modelfile:**
```bash
# Create custom model from Modelfile configuration
ollama create enterprise-assistant -f ./Modelfile

# Execute interactive test session with system rules applied
ollama run enterprise-assistant "What are your operational rules?"
```

**4.Python API Integration Test (api_test.py):**
```python
# Send structured system/user messages via Python to validate custom model behavior
import json
import requests

url = "http://localhost:11434/api/chat"

payload = {
    "model": "enterprise-assistant",
    "messages": [
        {"role": "system", "content": "You are a concise enterprise assistant."},
        {"role": "user", "content": "What is our primary directive?"},
    ],
    "stream": False,
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print("API Response Success!\n")
    print(data["message"]["content"])
else:
    print(f"Error: {response.status_code} - {response.text}")
```