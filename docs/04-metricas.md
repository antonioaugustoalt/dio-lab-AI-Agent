# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

---

### 🧪 Teste 1: Recomendação Gamer (cenário padrão)
- **Pergunta:**  
  "Quero montar um PC gamer com orçamento de R$ 5000"

- **Resposta esperada:**  
  Configuração com foco em GPU (ex: RX 7600 ou RTX 4060), 16GB RAM, SSD NVMe, sem ultrapassar o orçamento

- **Resultado:**  
  [X] Correto  [ ] Incorreto

---

### 🧪 Teste 2: Recomendação para Programador
- **Pergunta:**  
  "Preciso de um PC para programação com orçamento de R$ 4000"

- **Resposta esperada:**  
  Priorizar CPU e RAM (ex: Ryzen 7 ou similar + 32GB RAM), podendo não incluir GPU dedicada

- **Resultado:**  
  [X] Correto  [ ] Incorreto

---

### 🧪 Teste 3: Compatibilidade de peças
- **Pergunta:**  
  "Monte um PC gamer com R$ 5000"

- **Resposta esperada:**  
  CPU e placa-mãe com o mesmo socket (ex: AM4 + B550), sem incompatibilidades

- **Resultado:**  
  [X] Correto  [ ] Incorreto

---

### 🧪 Teste 4: Falta de contexto
- **Pergunta:**  
  "Me recomenda um PC"

- **Resposta esperada:**  
  O agente solicita mais informações (perfil e orçamento)

- **Resultado:**  
  [X] Correto  [ ] Incorreto

---

### 🧪 Teste 5: Pergunta fora do escopo
- **Pergunta:**  
  "Qual o melhor celular custo-benefício?"

- **Resposta esperada:**  
  O agente informa que só trata de montagem de PCs

- **Resultado:**  
  [X] Correto  [ ] Incorreto

---

---

## Resultados

Após os testes, registre suas conclusões:

### O que funcionou bem:
- O agente montou configurações de PCs corretamente com base no perfil e orçamento  
- As recomendações seguiram as regras definidas (ex: priorização de GPU para gamer)  
- A compatibilidade entre CPU e placa-mãe foi mantida em todos os cenários  
- O agente respondeu corretamente aos edge cases (fora de escopo, falta de contexto e segurança)  
- Ambas as versões do código geraram respostas consistentes e corretas  

---

### O que pode melhorar:
- O tempo de resposta ainda é relativamente alto em ambas as versões  
- Necessidade de otimizar processamento e reduzir latência  
- Melhorar a lógica de decisão em cenários mais complexos  
- Implementar cache ou pré-processamento para ganho de performance  
- Avaliar uso de modelos mais rápidos ou especializados  

---

## Observações Técnicas

Foram testadas duas versões do sistema:

- **Versão 1:** Estrutura básica conforme apresentada inicialmente  
- **Versão 2:** Versão otimizada com melhorias sugeridas por IA  

### Resultados observados:
- Ambas as versões apresentaram **alta assertividade nas respostas**  
- A versão otimizada teve **melhor desempenho (menor tempo de resposta)**  
- Mesmo assim, foi identificada **lentidão considerável**, indicando possível gargalo  

---

### Modelo utilizado:
- `GPT-oss:20b`

### Considerações:
- O modelo apresenta boa qualidade, porém alto custo computacional  
- Pode não ser ideal para aplicações com necessidade de resposta rápida  
- Possíveis melhorias incluem:
  - Uso de modelos mais leves  
  - Redução do contexto enviado ao modelo  
  - Estratégia híbrida (regras + IA)  

---

## Conclusão Geral

O agente demonstrou ser **funcional, consistente e confiável** na recomendação de configurações de PCs.

As regras foram corretamente aplicadas e os resultados foram coerentes com os perfis definidos.

No entanto, **a performance ainda é um ponto crítico**, sendo necessário otimizar o tempo de resposta para tornar a solução mais viável em ambientes reais.

---

> [!TIP]
> Para melhorar significativamente a performance, considere pré-processar os dados e deixar a IA responsável apenas pela decisão final e explicação, reduzindo o custo e o tempo de resposta.

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
