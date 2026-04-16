---
name: mcp-prompt-runner
description: MCP Prompt Runner - Execute MCP YAML templates via qwen CLI/hooks system. Provides both direct worker.py invocation and OpenRouter/LiteLLM proxy patterns. Supports model selection (7b for simple tasks, 72b for complex). Includes sync and async patterns with comprehensive configuration reference.
version: 1.0.0
updated: 2025-10-28
allowed-tools: [Bash, WebFetch]
---

# MCP Prompt Runner - Integration Skill

**Version**: 1.0.0
**Updated**: 2025-10-28
**Purpose**: Enable seamless integration of Qwen models with MCP YAML templates and local/remote inference

---

## 📖 Overview

The Qwen MCP Bridge skill provides two integration patterns for using Alibaba's Qwen models within the MCP (Model Context Protocol) ecosystem:

1. **Option 1**: Direct hook call to `worker.py` with YAML template-based prompts
2. **Option 2**: qwen CLI via LiteLLM proxy for remote/local model serving

Choose based on your deployment needs:
- **Option 1** (Direct): For local development and immediate execution
- **Option 2** (Proxy): For distributed inference, scaling, and API integration

---

## 🚀 Quick Start

### Install and Configure

**Step 1: Set Environment Variables**

```bash
# Linux/macOS
export OPENROUTER_API_KEY="your-openrouter-api-key"
export QWEN_WORKER_PATH="/path/to/worker.py"
export LITELLM_PROXY_PORT=47821

# Windows (PowerShell)
$env:OPENROUTER_API_KEY = "your-openrouter-api-key"
$env:QWEN_WORKER_PATH = "C:\path\to\worker.py"
$env:LITELLM_PROXY_PORT = 47821

# Windows (Command Prompt)
set OPENROUTER_API_KEY=your-openrouter-api-key
set QWEN_WORKER_PATH=C:\path\to\worker.py
set LITELLM_PROXY_PORT=47821
```

**Step 2: Verify Installation**

```bash
# Check if qwen CLI is available
qwen --version

# Check if Python worker.py exists
python ${QWEN_WORKER_PATH} --test
```

---

## 📋 Model Selection Guide

### Model Sizing Strategy

**Qwen-7B** (Small/Fast)
- Best for: Simple tasks, quick prototyping, resource-constrained environments
- Latency: ~500ms on GPU, ~2-5s on CPU
- Memory: 14-16GB GPU VRAM (quantized: 8GB)
- Use cases:
  - Code completion
  - Simple transformations
  - Quick Q&A
  - Text classification
  - Structured data extraction

**Qwen-72B** (Large/Powerful)
- Best for: Complex reasoning, multi-step logic, quality output prioritized
- Latency: ~2-5s on GPU
- Memory: 160GB GPU VRAM (quantized: 40-80GB)
- Use cases:
  - Complex code generation
  - Architectural decisions
  - Multi-step reasoning
  - Content generation
  - Detailed analysis

### Decision Matrix

```
┌─────────────────────┬──────────────┬──────────────┐
│ Task Type           │ Recommended  │ Alternative  │
├─────────────────────┼──────────────┼──────────────┤
│ Quick inference     │ 7B (local)   │ 72B (remote) │
│ Code completion     │ 7B (local)   │ 72B (local)  │
│ Complex logic       │ 72B (remote) │ 7B (slow)    │
│ Multi-step tasks    │ 72B (remote) │ 7B iterative │
│ Prototyping         │ 7B (local)   │ 72B (test)   │
│ Production quality  │ 72B (remote) │ 7B (cascade) │
└─────────────────────┴──────────────┴──────────────┘
```

### Load Requirements

```yaml
model_memory_requirements:
  qwen_7b:
    full_precision: "16GB GPU / 32GB RAM"
    int8_quantized: "8GB GPU / 16GB RAM"
    int4_quantized: "6GB GPU / 12GB RAM"
    bfloat16: "8GB GPU / 16GB RAM"

  qwen_72b:
    full_precision: "160GB GPU / 320GB RAM"  # 8x H100 80GB
    int8_quantized: "80GB GPU / 160GB RAM"   # 4x H100 80GB
    int4_quantized: "40GB GPU / 80GB RAM"    # 2x H100 40GB
    bfloat16: "90GB GPU / 180GB RAM"

  inference_latency:
    local_7b_gpu: "400-600ms"
    local_7b_cpu: "2-5s"
    local_72b_gpu: "2-5s"
    remote_via_proxy: "100-200ms network + inference"
```

---

## 🔌 Option 1: Direct Worker.py Invocation (Template-Based)

### Architecture

```
Your Code
    ↓
YAML Template (prompt-template.yaml)
    ↓
worker.py (Local execution)
    ↓
Qwen Model (via ollama/local inference)
    ↓
Result returned to caller
```

### Setup

**1. Locate or Create worker.py**

```python
# .claude/skills/qwen-mcp-bridge/worker.py
#!/usr/bin/env python3
"""
Qwen Worker: Direct inference execution with YAML template support
"""

import os
import sys
import json
import yaml
import asyncio
from typing import Optional, Dict, Any
from pathlib import Path

# Example implementation - adapt to your setup
class QwenWorker:
    def __init__(self, model: str = "qwen:7b"):
        self.model = model
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
    def run_sync(self, template_path: str, variables: Dict[str, Any]) -> str:
        """Synchronous template-based inference"""
        with open(template_path, 'r') as f:
            template = yaml.safe_load(f)
        
        prompt = self._render_template(template, variables)
        return self._invoke_model_sync(prompt)
    
    async def run_async(self, template_path: str, variables: Dict[str, Any]) -> str:
        """Asynchronous template-based inference"""
        with open(template_path, 'r') as f:
            template = yaml.safe_load(f)
        
        prompt = self._render_template(template, variables)
        return await self._invoke_model_async(prompt)
    
    def _render_template(self, template: Dict, variables: Dict[str, Any]) -> str:
        """Render YAML template with variables"""
        prompt = template.get('prompt', '')
        for key, value in variables.items():
            prompt = prompt.replace(f"{{{key}}}", str(value))
        return prompt
    
    def _invoke_model_sync(self, prompt: str) -> str:
        """Call Qwen model synchronously"""
        import requests
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt, "stream": False}
        )
        return response.json()['response']
    
    async def _invoke_model_async(self, prompt: str) -> str:
        """Call Qwen model asynchronously"""
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/generate",
                json={"model": self.model, "prompt": prompt, "stream": False}
            ) as resp:
                data = await resp.json()
                return data['response']

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", required=True)
    parser.add_argument("--variables", type=json.loads, default={})
    parser.add_argument("--model", default="qwen:7b")
    parser.add_argument("--async", action="store_true")
    
    args = parser.parse_args()
    
    worker = QwenWorker(model=args.model)
    
    if args.async:
        result = asyncio.run(worker.run_async(args.template, args.variables))
    else:
        result = worker.run_sync(args.template, args.variables)
    
    print(result)
```

**2. Create YAML Template**

```yaml
# .claude/skills/qwen-mcp-bridge/prompt-template.yaml
---
name: qwen-template
version: 1.0.0
type: mcp-template

# Template variables to be filled at runtime
variables:
  task_description: "string"
  context: "string"
  model_type: "string"  # 7b or 72b
  temperature: "float"  # 0.0-1.0

# System prompt (instructions for the model)
system: |
  You are a helpful AI assistant powered by Qwen.
  Task Type: {task_description}
  Model: {model_type}

# User prompt (actual question/task)
prompt: |
  Context:
  {context}
  
  Please help with the above task.

# Model parameters
parameters:
  temperature: {temperature}
  top_p: 0.9
  max_tokens: 2048
```

### Execution Examples

**Synchronous Execution (Blocking)**

```bash
# Direct bash invocation
python worker.py \
  --template ./prompt-template.yaml \
  --variables '{"task_description":"code review","context":"review auth.py","model_type":"7b","temperature":0.7}'

# With environment variables
export QWEN_MODEL="qwen:7b"
python worker.py \
  --template ./prompt-template.yaml \
  --variables '{"task_description":"fix bug","context":"FileNotFoundError in handler.py","model_type":"7b","temperature":0.3}' \
  --model "${QWEN_MODEL}"
```

**Asynchronous Execution (Non-blocking)**

```bash
# Python async wrapper
python -c "
import asyncio
import sys
from worker import QwenWorker

async def main():
    worker = QwenWorker(model='qwen:7b')
    result = await worker.run_async(
        './prompt-template.yaml',
        {
            'task_description': 'code generation',
            'context': 'Create authentication middleware',
            'model_type': '7b',
            'temperature': 0.5
        }
    )
    print(result)

asyncio.run(main())
"
```

**In Claude Code Context (Hook Call)**

```python
# Inside .claude/hooks/ or skill implementation
import subprocess
import json
from pathlib import Path

def invoke_qwen_worker(
    template_path: str,
    variables: dict,
    model: str = "qwen:7b",
    async_mode: bool = False
) -> str:
    """
    Direct invocation of Qwen worker.py
    
    Args:
        template_path: Path to YAML template
        variables: Dict of template variables
        model: Model identifier (e.g., "qwen:7b", "qwen:72b")
        async_mode: If True, return immediately and monitor via polling
    
    Returns:
        Model output string
    """
    
    worker_path = Path(__file__).parent.parent / "skills" / "qwen-mcp-bridge" / "worker.py"
    
    cmd = [
        "python", str(worker_path),
        "--template", template_path,
        "--variables", json.dumps(variables),
        "--model", model
    ]
    
    if async_mode:
        cmd.append("--async")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"Worker error: {result.stderr}")
    
    return result.stdout.strip()

# Usage
output = invoke_qwen_worker(
    template_path=".claude/skills/qwen-mcp-bridge/prompt-template.yaml",
    variables={
        "task_description": "analyze code quality",
        "context": "Review authentication module",
        "model_type": "7b",
        "temperature": 0.7
    },
    model="qwen:7b"
)
print(output)
```

---

## 🌐 Option 2: OpenRouter + LiteLLM Proxy Pattern

### Architecture

```
Your Code
    ↓
LiteLLM Proxy (Port 47821)
    ↓
OpenRouter API
    ↓
Qwen Model (Remote inference)
    ↓
Result returned via HTTP
```

### Configuration Setup

**1. Install LiteLLM Proxy**

```bash
# Via pip
pip install litellm[proxy]

# Via conda
conda install -c conda-forge litellm
```

**2. Configure Environment**

Create `.env` or export variables:

```bash
# Required
export OPENROUTER_API_KEY="sk-or-v1-xxxxxxxxxxxxxxxxxxxx"

# LiteLLM Proxy Configuration
export LITELLM_PROXY_HOST="0.0.0.0"
export LITELLM_PROXY_PORT=47821
export LITELLM_LOG_LEVEL="INFO"

# Optional: Custom model mappings
export LITELLM_MODEL_LIST_CONFIG="./litellm-config.yaml"

# Optional: Enable caching
export LITELLM_CACHE="redis"
export REDIS_URL="redis://localhost:6379"
```

**3. LiteLLM Configuration File**

```yaml
# litellm-config.yaml
model_list:
  - model_name: "qwen-7b"
    litellm_params:
      model: "openrouter/alibaba/qwen-7b-instruct"
      api_key: "${OPENROUTER_API_KEY}"
      api_base: "https://openrouter.ai/api/v1"
      temperature: 0.7
      max_tokens: 2048
    
  - model_name: "qwen-72b"
    litellm_params:
      model: "openrouter/alibaba/qwen-72b-instruct"
      api_key: "${OPENROUTER_API_KEY}"
      api_base: "https://openrouter.ai/api/v1"
      temperature: 0.7
      max_tokens: 4096

router_settings:
  timeout: 600
  num_retries: 3
  redis_cache: false  # Set to true if Redis available
```

**4. Start LiteLLM Proxy**

```bash
# Option A: Command line
litellm_proxy \
  --host 0.0.0.0 \
  --port 47821 \
  --config ./litellm-config.yaml \
  --debug

# Option B: Via Python
python -m litellm.proxy.proxy \
  --host 0.0.0.0 \
  --port 47821 \
  --config ./litellm-config.yaml

# Option C: Docker (if using Docker)
docker run -p 47821:4000 \
  -e OPENROUTER_API_KEY="sk-or-v1-xxxx" \
  ghcr.io/berriai/litellm:latest-stable \
  litellm_proxy --config ./litellm-config.yaml
```

### Health Check

```bash
# Verify proxy is running
curl -X GET http://localhost:47821/health

# Expected response
# {"status": "healthy", "timestamp": "2025-10-28T..."}

# List available models
curl -X GET http://localhost:47821/v1/models \
  -H "Authorization: Bearer $(echo $OPENROUTER_API_KEY)"
```

### Execution Examples

**Synchronous HTTP Request**

```bash
# Direct curl invocation
curl -X POST http://localhost:47821/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-7b",
    "messages": [
      {"role": "user", "content": "Explain quantum computing"}
    ],
    "temperature": 0.7,
    "max_tokens": 2048
  }'

# With environment variables
PROXY_URL="${LITELLM_PROXY_HOST}:${LITELLM_PROXY_PORT}"
curl -X POST "http://${PROXY_URL}/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-72b",
    "messages": [
      {"role": "system", "content": "You are a code review expert"},
      {"role": "user", "content": "Review this Python function for security issues"}
    ],
    "temperature": 0.3,
    "max_tokens": 1024
  }'
```

**Python Client (Synchronous)**

```python
#!/usr/bin/env python3
"""
Qwen LiteLLM Proxy Client - Synchronous
"""

import os
import requests
import json
from typing import Optional, Dict, Any

class QwenProxyClient:
    def __init__(
        self,
        proxy_url: str = "http://localhost:47821",
        timeout: int = 600
    ):
        self.proxy_url = proxy_url
        self.timeout = timeout
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY', '')}"
        }
    
    def chat_completion(
        self,
        model: str,
        messages: list,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Synchronous chat completion request
        
        Args:
            model: Model name (qwen-7b or qwen-72b)
            messages: List of message dicts with 'role' and 'content'
            temperature: Temperature parameter (0.0-1.0)
            max_tokens: Maximum output tokens
            **kwargs: Additional parameters (top_p, frequency_penalty, etc.)
        
        Returns:
            Response dict with 'choices', 'usage', etc.
        """
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs
        }
        
        response = requests.post(
            f"{self.proxy_url}/v1/chat/completions",
            headers=self.headers,
            json=payload,
            timeout=self.timeout
        )
        
        response.raise_for_status()
        return response.json()
    
    def simple_completion(
        self,
        model: str,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 2048
    ) -> str:
        """
        Simple text completion (returns just the text)
        
        Args:
            model: Model name
            prompt: Input prompt
            temperature: Temperature parameter
            max_tokens: Maximum output tokens
        
        Returns:
            Generated text string
        """
        
        response = self.chat_completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response['choices'][0]['message']['content']

# Usage Example
if __name__ == "__main__":
    client = QwenProxyClient()
    
    # Single turn conversation
    response = client.chat_completion(
        model="qwen-7b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Write a Python function to reverse a string"}
        ],
        temperature=0.5,
        max_tokens=512
    )
    
    print("Response:", response['choices'][0]['message']['content'])
    print("Tokens used:", response['usage'])
    
    # Simple completion
    output = client.simple_completion(
        model="qwen-72b",
        prompt="Explain neural networks in one paragraph",
        temperature=0.7
    )
    
    print("Output:", output)
```

**Python Client (Asynchronous)**

```python
#!/usr/bin/env python3
"""
Qwen LiteLLM Proxy Client - Asynchronous
"""

import os
import asyncio
import aiohttp
from typing import Optional, Dict, Any, List

class QwenAsyncProxyClient:
    def __init__(
        self,
        proxy_url: str = "http://localhost:47821",
        timeout: int = 600
    ):
        self.proxy_url = proxy_url
        self.timeout = timeout
        self.api_key = os.getenv('OPENROUTER_API_KEY', '')
    
    async def chat_completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 2048,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Asynchronous chat completion request
        """
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.proxy_url}/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            ) as resp:
                return await resp.json()
    
    async def batch_completions(
        self,
        model: str,
        prompts: List[str],
        temperature: float = 0.7
    ) -> List[str]:
        """
        Run multiple completions in parallel
        """
        
        tasks = [
            self.chat_completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            for prompt in prompts
        ]
        
        results = await asyncio.gather(*tasks)
        return [r['choices'][0]['message']['content'] for r in results]

# Usage Example
async def main():
    client = QwenAsyncProxyClient()
    
    # Single async completion
    response = await client.chat_completion(
        model="qwen-7b",
        messages=[
            {"role": "user", "content": "What is machine learning?"}
        ],
        temperature=0.7
    )
    print("Response:", response['choices'][0]['message']['content'])
    
    # Batch processing
    prompts = [
        "Explain AI in one sentence",
        "What is deep learning?",
        "Define neural networks"
    ]
    
    results = await client.batch_completions(
        model="qwen-72b",
        prompts=prompts
    )
    
    for prompt, result in zip(prompts, results):
        print(f"\nPrompt: {prompt}")
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

### OpenRouter Model Mappings

Available Qwen models via OpenRouter:

```yaml
qwen_models:
  qwen_7b_instruct:
    model_id: "alibaba/qwen-7b-instruct"
    openrouter_path: "openrouter/alibaba/qwen-7b-instruct"
    context_window: 2048
    supports_vision: false
    pricing:
      input: "$0.07/1M tokens"
      output: "$0.14/1M tokens"
  
  qwen_14b_chat:
    model_id: "alibaba/qwen-14b-chat"
    openrouter_path: "openrouter/alibaba/qwen-14b-chat"
    context_window: 2048
    supports_vision: false
    pricing:
      input: "$0.15/1M tokens"
      output: "$0.30/1M tokens"
  
  qwen_72b_instruct:
    model_id: "alibaba/qwen-72b-instruct"
    openrouter_path: "openrouter/alibaba/qwen-72b-instruct"
    context_window: 4096
    supports_vision: false
    pricing:
      input: "$0.81/1M tokens"
      output: "$1.63/1M tokens"
```

---

## 📊 Comparison: Option 1 vs Option 2

```
┌──────────────────────┬─────────────────────┬──────────────────────┐
│ Aspect               │ Option 1 (Worker)   │ Option 2 (Proxy)     │
├──────────────────────┼─────────────────────┼──────────────────────┤
│ Setup Complexity     │ Simple              │ Moderate             │
│ Latency              │ Low (local)         │ ~100-200ms (network) │
│ Scalability          │ Single instance     │ Multi-instance proxy │
│ Cost                 │ Hardware only       │ OpenRouter API fees  │
│ Local/Remote         │ Local only          │ Both                 │
│ Model Size Limit     │ Hardware capacity   │ OpenRouter limits    │
│ Async Support        │ Yes (via asyncio)   │ Yes (aiohttp)        │
│ Sync Support         │ Yes (subprocess)    │ Yes (requests)       │
│ Caching              │ DIY                 │ Built-in (optional)  │
│ Load Balancing       │ N/A                 │ Via Proxy            │
│ Development          │ More control        │ Less ops burden      │
│ Production           │ Complex deployment  │ Simplified           │
└──────────────────────┴─────────────────────┴──────────────────────┘
```

---

## 🔧 Advanced Configuration

### Custom Model Parameters

**Option 1: Worker.py Parameters**

```python
class QwenWorker:
    def __init__(self, model: str = "qwen:7b", **params):
        self.model_params = {
            "temperature": params.get("temperature", 0.7),
            "top_p": params.get("top_p", 0.9),
            "top_k": params.get("top_k", 40),
            "repetition_penalty": params.get("repetition_penalty", 1.0),
            "length_penalty": params.get("length_penalty", 1.0),
            "num_beams": params.get("num_beams", 1),
            "num_return_sequences": params.get("num_return_sequences", 1),
        }
```

**Option 2: Proxy Request Parameters**

```python
# Extended parameters for LiteLLM proxy
response = client.chat_completion(
    model="qwen-7b",
    messages=[...],
    # Core parameters
    temperature=0.7,
    max_tokens=2048,
    top_p=0.9,
    top_k=40,
    # Advanced parameters
    frequency_penalty=0.0,
    presence_penalty=0.0,
    repetition_penalty=1.0,
    # Model-specific
    use_cache=True,
    return_logprobs=False
)
```

### Caching Strategy

**For Option 1 (Worker.py)**

```python
from functools import lru_cache
import hashlib

class CachedQwenWorker(QwenWorker):
    def __init__(self, *args, cache_size=128, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_size = cache_size
    
    @lru_cache(maxsize=128)
    def run_cached(self, prompt_hash: str, prompt: str) -> str:
        """Cache results based on prompt hash"""
        return self._invoke_model_sync(prompt)
    
    def run_with_cache(self, prompt: str) -> str:
        """Run with caching enabled"""
        prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
        return self.run_cached(prompt_hash, prompt)
```

**For Option 2 (Proxy with Redis)**

```yaml
# litellm-config.yaml with Redis caching
router_settings:
  timeout: 600
  redis_cache: true
  redis_host: "localhost"
  redis_port: 6379
  redis_db: 0
  cache_ttl: 3600  # Cache for 1 hour

# Start Redis
redis-server --port 6379
```

---

## 🚨 Error Handling and Troubleshooting

### Common Issues and Solutions

**Issue 1: Connection Refused (Proxy)**

```python
# Problem: Cannot connect to LiteLLM proxy
# Solution: Check proxy is running and port is correct

import socket

def check_proxy_health(host: str = "localhost", port: int = 47821):
    """Verify proxy is accessible"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

if not check_proxy_health():
    print("Proxy not running on port 47821")
    print("Start it with: litellm_proxy --port 47821")
```

**Issue 2: Authentication Failed (OpenRouter API Key)**

```python
# Problem: 401 Unauthorized
# Solution: Verify API key is set and valid

import os
api_key = os.getenv('OPENROUTER_API_KEY')
if not api_key or not api_key.startswith('sk-or-v1'):
    raise ValueError("Invalid or missing OPENROUTER_API_KEY")
```

**Issue 3: Out of Memory (Local Worker)**

```python
# Problem: Model too large for available GPU
# Solutions:
# 1. Use smaller model (7b instead of 72b)
# 2. Enable quantization (int8 or int4)
# 3. Use proxy instead (offload to OpenRouter)

# Check available memory
import torch
print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
print(f"Available: {torch.cuda.mem_get_info()[0] / 1e9:.1f} GB")

# Load with quantization
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  # 4-bit quantization
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen-7B",
    quantization_config=bnb_config
)
```

**Issue 4: Slow Response Time**

```python
# Problem: Inference is too slow
# Solutions:
# 1. Reduce max_tokens
# 2. Increase temperature (less decoding)
# 3. Switch to smaller model
# 4. Use OpenRouter proxy (faster with GPU cluster)

# Benchmark different configs
import time

configs = [
    {"model": "qwen:7b", "max_tokens": 512, "temp": 0.7},
    {"model": "qwen:7b", "max_tokens": 2048, "temp": 0.7},
    {"model": "qwen:7b", "max_tokens": 512, "temp": 0.3},
]

for config in configs:
    start = time.time()
    # Run inference
    latency = time.time() - start
    print(f"{config}: {latency:.2f}s")
```

---

## 📈 Performance Tuning

### Batch Processing

**Option 1: Sequential Batching (Worker)**

```python
def batch_process_sequential(
    worker: QwenWorker,
    prompts: list,
    template_path: str
) -> list:
    """Process multiple prompts sequentially"""
    results = []
    for prompt in prompts:
        result = worker.run_sync(
            template_path,
            {"prompt": prompt}
        )
        results.append(result)
    return results
```

**Option 2: Parallel Batching (Proxy)**

```python
async def batch_process_parallel(
    client: QwenAsyncProxyClient,
    prompts: list,
    model: str = "qwen-7b"
) -> list:
    """Process multiple prompts in parallel"""
    return await client.batch_completions(
        model=model,
        prompts=prompts
    )

# Usage
import asyncio
prompts = ["prompt 1", "prompt 2", "prompt 3", ...]
results = asyncio.run(batch_process_parallel(client, prompts))
```

### Rate Limiting

```python
from ratelimit import limits, sleep_and_retry

class RateLimitedClient:
    @sleep_and_retry
    @limits(calls=10, period=60)  # 10 calls per minute
    def chat_completion(self, model: str, messages: list):
        """Rate-limited completion request"""
        # Your request logic here
        pass
```

---

## 🔐 Security Considerations

### API Key Management

**DO:**
- ✅ Store API keys in environment variables
- ✅ Use `.env` files (git-ignored)
- ✅ Rotate keys regularly
- ✅ Use least-privilege API keys
- ✅ Log key access

**DO NOT:**
- ❌ Hardcode keys in source files
- ❌ Commit `.env` files to git
- ❌ Share keys across teams
- ❌ Log full API keys
- ❌ Use keys in client-side code

### Input Validation

```python
def validate_prompt(prompt: str, max_length: int = 8192) -> bool:
    """Validate user input before sending to model"""
    if not prompt or len(prompt) == 0:
        raise ValueError("Prompt cannot be empty")
    if len(prompt) > max_length:
        raise ValueError(f"Prompt exceeds {max_length} character limit")
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be string")
    return True
```

### Output Sanitization

```python
import re

def sanitize_output(text: str) -> str:
    """Remove sensitive information from model output"""
    # Remove email addresses
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)
    # Remove API keys
    text = re.sub(r'sk-[A-Za-z0-9]{20,}', '[API_KEY]', text)
    # Remove phone numbers
    text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', text)
    return text
```

---

## 📝 Complete Integration Example

### End-to-End Workflow (Option 2 Recommended)

```python
#!/usr/bin/env python3
"""
Complete Qwen Integration Example with Error Handling
"""

import os
import json
import asyncio
import logging
from typing import Optional, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QwenIntegration:
    def __init__(self, proxy_url: str = "http://localhost:47821"):
        self.proxy_url = proxy_url
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.validate_config()
    
    def validate_config(self):
        """Verify all configuration is set"""
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not set")
        logger.info(f"Configuration validated: proxy={self.proxy_url}")
    
    async def process_task(
        self,
        task_description: str,
        context: str,
        model: str = "qwen-7b"
    ) -> dict:
        """
        Process a task using Qwen
        
        Args:
            task_description: Description of the task
            context: Relevant context for the task
            model: Model to use (qwen-7b or qwen-72b)
        
        Returns:
            dict with task_id, result, and metadata
        """
        
        import aiohttp
        import uuid
        import time
        
        task_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        
        try:
            logger.info(f"[{task_id}] Starting task: {task_description}")
            
            # Validate inputs
            if len(context) > 8192:
                context = context[:8192]
                logger.warning(f"[{task_id}] Context truncated to 8192 chars")
            
            # Build request
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": f"Task: {task_description}"},
                    {"role": "user", "content": context}
                ],
                "temperature": 0.7,
                "max_tokens": 2048
            }
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            
            # Send request
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.proxy_url}/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=600)
                ) as resp:
                    if resp.status != 200:
                        error = await resp.text()
                        raise RuntimeError(f"API error: {resp.status} - {error}")
                    
                    result = await resp.json()
            
            elapsed = time.time() - start_time
            
            logger.info(f"[{task_id}] Task completed in {elapsed:.2f}s")
            
            return {
                "task_id": task_id,
                "status": "success",
                "model": model,
                "result": result['choices'][0]['message']['content'],
                "tokens_used": result['usage']['total_tokens'],
                "elapsed_seconds": elapsed
            }
        
        except Exception as e:
            logger.error(f"[{task_id}] Task failed: {str(e)}")
            return {
                "task_id": task_id,
                "status": "failed",
                "error": str(e),
                "elapsed_seconds": time.time() - start_time
            }

# Usage
async def main():
    integration = QwenIntegration()
    
    result = await integration.process_task(
        task_description="Code Review",
        context="Review this authentication function for security issues",
        model="qwen-72b"
    )
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📚 Reference Documentation

### Template Files

- **YAML Template**: `.claude/skills/qwen-mcp-bridge/prompt-template.yaml`
- **Agent Template**: `.claude/skills/agent/prompt-template.yaml`

### Configuration Examples

See `.claude/mcp-configs/` for:
- `litellm-config.yaml` - Full proxy configuration
- `openrouter-integration.md` - Integration guide
- `.env.template.openrouter` - Environment variables template

### Related Skills

- **mcp-builder**: Building custom MCP servers
- **fastapi-implement**: API implementation patterns
- **python-implement**: Python code generation

---

## 🎯 When to Use This Skill

**Use Option 1 (Worker.py) when:**
- ✅ Running local development
- ✅ Need immediate inference
- ✅ Hardware available for model hosting
- ✅ Latency critical (network-free)
- ✅ Cost optimization needed

**Use Option 2 (Proxy) when:**
- ✅ Scaling to multiple concurrent requests
- ✅ Don't have local GPU resources
- ✅ Need model flexibility/switching
- ✅ Production deployment needed
- ✅ Prefer managed inference

---

## Version History

| Version | Date       | Changes                                                                      |
| ------- | ---------- | ---------------------------------------------------------------------------- |
| 1.0.0   | 2025-10-28 | Initial release. Option 1 (Worker.py) and Option 2 (Proxy) fully documented |

---

**Created By**: ai-agents development team
**Purpose**: Enable Qwen model integration with MCP YAML templates
**License**: MIT (see LICENSE file for details)

**Support**: For issues or questions, refer to:
- Qwen Documentation: https://github.com/QwenLM
- OpenRouter: https://openrouter.ai
- LiteLLM: https://docs.litellm.ai
