# Base de Conhecimento

## Dados Utilizados

| Arquivo             | Formato | Utilização no Agente                                                        |
| ------------------- | ------- | --------------------------------------------------------------------------- |
| `cpus.csv`          | CSV     | Selecionar processadores com base em desempenho, consumo e custo-benefício  |
| `gpus.csv`          | CSV     | Definir placa de vídeo conforme perfil (gamer, IA, edição) e orçamento      |
| `ram.csv`           | CSV     | Escolher memória adequada (capacidade e frequência) conforme uso            |
| `storage.csv`       | CSV     | Determinar tipo e capacidade de armazenamento (NVMe, SATA)                  |
| `motherboards.csv`  | CSV     | Garantir compatibilidade com CPU e suporte a upgrades                       |
| `psu.csv`           | CSV     | Dimensionar fonte com base no consumo total e margem de segurança           |
| `cases.csv`         | CSV     | Selecionar gabinete considerando airflow e perfil do usuário                |
| `profiles.csv`      | CSV     | Definir prioridades de hardware conforme tipo de usuário                    |
| `build_rules.csv`   | CSV     | Aplicar regras de decisão (ex: mínimo de RAM, preferência por NVIDIA, etc.) |
| `compatibility.csv` | CSV     | Validar compatibilidade entre CPU e placa-mãe                               |
| `config.json`       | JSON    | Controlar pesos de decisão e regras globais do sistema                      |


> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
