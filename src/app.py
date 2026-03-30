import json
import pandas as pd
import os
import requests
import streamlit as st

#========CONFIGURAÇÕES========
OLLAMA_URL = "http://localhost:11434/api/generate"  # URL do Ollama
MODELO = "gpt-oss:20b"

#========IMPORTANDO DADOS=======
from pathlib import Path
import pandas as pd
import json

# Base do projeto (pasta source)
BASE_DIR = Path(__file__).resolve().parent

# Caminho da pasta data
DATA_DIR = BASE_DIR.parent / 'data'

#========IMPORTANDO DADOS=======

perfil = pd.read_csv(DATA_DIR / 'profiles.csv')
gabinetes = pd.read_csv(DATA_DIR / 'cases.csv')
build = pd.read_csv(DATA_DIR / 'build_rules.csv')
compatibilidade = pd.read_csv(DATA_DIR / 'compatibility.csv')

with open(DATA_DIR / 'configuration_weights.json', 'r', encoding='utf-8') as f:
    configuration = json.load(f)

cpus = pd.read_csv(DATA_DIR / 'cpus.csv')
gpus = pd.read_csv(DATA_DIR / 'gpus.csv')
fontes = pd.read_csv(DATA_DIR / 'psu.csv')
ram = pd.read_csv(DATA_DIR / 'ram.csv')
storage = pd.read_csv(DATA_DIR / 'storage.csv')

# =========== MONTAR CONTEXTO ===========
perfil_exemplo = perfil.iloc[0]  # só pra dar estrutura/base

contexto = f"""
Você é um especialista em montagem de PCs.

Sua tarefa:
- Interpretar a mensagem do usuário
- Identificar automaticamente:
  - perfil de uso
  - orçamento
  - objetivo
  - prioridade

Use os perfis abaixo como base:

=== PERFIS DISPONÍVEIS ===
{perfil.to_string(index=False)}

=== REGRAS DE MONTAGEM ===
{build.to_string(index=False)}

=== COMPATIBILIDADE ===
{compatibilidade.to_string(index=False)}

=== GABINETES DISPONÍVEIS ===
{gabinetes.to_string(index=False)}

=== CPUs DISPONÍVEIS ===
{cpus.to_string(index=False)}

=== GPUs DISPONÍVEIS ===
{gpus.to_string(index=False)}

=== MEMÓRIAS RAM DISPONÍVEIS ===
{ram.to_string(index=False)}

=== STORAGE DISPONÍVEIS ===
{storage.to_string(index=False)}

=== FONTES DE ALIMENTAÇÃO DISPONÍVEIS ===
{fontes.to_string(index=False)}

=== PESOS DE CONFIGURAÇÃO ===
{json.dumps(configuration, indent=2, ensure_ascii=False)}
"""

#===========SYSTEM PROMPT/INSTRUCTIONS===========
INSTRUCTIONS = f"""Você é um especialista em montagem de computadores (PC Builder Expert).

Sua função é analisar o perfil do usuário, orçamento e opções disponíveis para recomendar a melhor configuração possível de PC peça por peça.

REGRAS:
1. NUNCA ultrapasse o orçamento do usuário.
2. SEMPRE garanta compatibilidade entre CPU e placa-mãe (mesmo socket).
3. EVITE gargalos (CPU muito fraca para GPU ou vice-versa).
4. SIGA o perfil do usuário:
   - gamer → priorizar GPU
   - programador → priorizar CPU e RAM
   - editor → equilíbrio + RAM alta
   - ia_dev → GPU NVIDIA obrigatória
   - office → evitar GPU dedicada

5. REGRAS TÉCNICAS:
   - RAM mínima: 16GB (32GB para edição/IA)
   - Sempre preferir SSD NVMe quando possível
   - Fonte deve suportar consumo com margem de segurança (~40%)
   - GPU deve representar ~30% a 50% do orçamento (para gamers)

6. EXPLIQUE suas escolhas de forma clara e técnica, mas sem ser excessivamente longo.
7. Caso falte alguma informação na solicitação do usuário(como o orçamento por exemplo), sempre peça a informação antes de responde-la ativamente

8. FORMATO DA RESPOSTA (OBRIGATÓRIO):

Monte a resposta exatamente neste formato:

--- CONFIGURAÇÃO RECOMENDADA ---

CPU: ...
GPU: ...
RAM: ...
Armazenamento: ...
Placa-mãe: ...
Fonte: ...
Gabinete: ...

Preço total: R$ ...

--- JUSTIFICATIVA ---

Explique de forma objetiva:
- Por que essa GPU foi escolhida
- Por que essa CPU é adequada
- Como o conjunto está equilibrado
- Se existe margem para upgrade futuro
- E qualquer outra consideração relevante
"""

#========CHAMAR OLLAMA========
def perguntar(msg):
    prompt = f"""
    {INSTRUCTIONS}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    })

    data = r.json()

    return data.get('response', str(data))

#========INTERFACE SIMPLES========
st.title("PC Builder Expert")

if pergunta := st.chat_input("Faça sua pergunta sobre a montagem do PC:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))
