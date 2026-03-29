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

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [ ] Correto  [ ] Incorreto

---

Resultados

Após os testes, registre suas conclusões:

O que funcionou bem:

O agente conseguiu montar configurações de PCs corretamente com base no perfil e orçamento
As recomendações respeitaram as regras definidas (priorização de GPU para gamer, CPU para programador, etc.)
A compatibilidade entre CPU e placa-mãe foi mantida em todos os testes
O agente lidou corretamente com edge cases (fora de escopo, falta de contexto e segurança)
As duas versões do código (básica e otimizada) responderam corretamente às solicitações

O que pode melhorar:

O tempo de resposta ainda é relativamente alto em ambas as versões
Necessidade de otimização no processamento e/ou escolha de modelo mais eficiente
Melhorar a priorização dinâmica das peças para cenários mais complexos
Implementar cache ou pré-processamento para reduzir latência
Avaliar integração com modelos mais rápidos ou especializados
Observações Técnicas

Foram testadas duas versões do sistema:

Versão 1: Estrutura básica conforme apresentada inicialmente
Versão 2: Versão otimizada com melhorias sugeridas por IA

Ambas as versões apresentaram alta assertividade nas respostas, porém:

A versão otimizada teve melhor desempenho (menor tempo de resposta)
Ainda assim, foi observada lentidão considerável, indicando gargalo no processamento ou no modelo utilizado
Modelo utilizado:
GPT-oss:20b
Considerações:
O modelo utilizado possui bom nível de qualidade, porém apresenta custo computacional elevado
Para uso em produção, pode ser interessante avaliar:
Modelos mais leves (melhor latência)
Abordagens híbridas (regra + IA)
Redução de contexto enviado ao modelo
 Conclusão Geral

O agente demonstrou ser funcional e confiável para recomendação de PCs, com boa aderência às regras e aos perfis definidos.

Entretanto, a performance ainda é um ponto crítico, sendo recomendadas otimizações futuras para tornar a solução viável em cenários reais (tempo de resposta menor e melhor experiência do usuário).

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
