# Mission Control Energy

## Global Solution 2026.1 – Soluções em Energias Renováveis e Sustentáveis

### Integrantes

- Arthur Maziviero Faria – RM: 573928
- Tommaso C. Nagliatti – RM: 572147

---

## Descrição do Projeto

O Mission Control Energy é um sistema desenvolvido em Python para simular o monitoramento energético de uma missão espacial experimental.

O sistema recebe dados informados pelo usuário e realiza análises automáticas relacionadas à temperatura, comunicação, bateria, geração solar e status dos módulos da missão.

Com base nesses dados, o programa gera alertas, calcula níveis de risco, sugere ações corretivas e apresenta um relatório final sobre a situação da missão.

O projeto foi desenvolvido para a disciplina **Soluções em Energias Renováveis e Sustentáveis** da **Global Solution 2026.1**, aplicando conceitos de energia, potência, sustentabilidade e monitoramento inteligente.

---

## Funcionalidades

- Cadastro de ciclos da missão pelo usuário;
- Monitoramento de temperatura;
- Monitoramento da comunicação;
- Monitoramento do nível de bateria;
- Monitoramento da geração de energia solar;
- Monitoramento do status dos módulos;
- Geração automática de alertas;
- Classificação de risco da missão;
- Recomendações automáticas de ação;
- Relatório final da operação.

---

## Parâmetros Monitorados

| Parâmetro | Descrição |
|------------|------------|
| Temperatura | Condição térmica dos sistemas da missão |
| Comunicação | Qualidade do sinal com a base terrestre |
| Bateria | Energia armazenada disponível |
| Geração Solar | Energia produzida pelos painéis solares |
| Status dos Módulos | Condição operacional dos sistemas |

---

## Tecnologias Utilizadas

- Python 3
- Estruturas Condicionais
- Estruturas de Repetição
- Funções
- Listas
- Entrada de Dados via Terminal

---

## Estrutura do Projeto

```text
mission-control-energy/
│
├── README.md
└── mission_control_energy.py

```

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/mission-control-energy.git
```

Acesse a pasta do projeto:

```bash
cd mission-control-energy
```

Execute o programa:

```bash
python mission_control_energy.py
```

---

## Exemplo de Funcionamento

O usuário informa:

```text
Temperatura: 38
Comunicação: 25
Bateria: 18
Geração Solar: 20
Status dos Módulos: 35
```

O sistema realiza a análise automática e exibe:

```text
Temperatura: CRÍTICO
Comunicação: CRÍTICO
Bateria: CRÍTICO
Geração Solar: CRÍTICO
Status dos Módulos: CRÍTICO

Ação: Ativar modo de economia de energia.
```

---

## Aplicação na Missão Espacial

O sistema simula o monitoramento energético de uma missão espacial experimental.

Através da análise contínua dos dados informados pelo operador, a solução auxilia na identificação de situações críticas relacionadas à disponibilidade de energia, eficiência dos sistemas e sustentabilidade da missão.

A utilização de geração solar e gerenciamento inteligente de baterias permite demonstrar conceitos de energias renováveis aplicados ao contexto aeroespacial.

---

## Vídeo de Demonstração

Link do vídeo:

```text
https://youtu.be/Qfa60Jr1SKA
```

---

## Repositório GitHub

Link do projeto:

```text
https://github.com/maziviero27/GS_SERS_Control_Energy.git
```

---

## Conclusão

O Mission Control Energy demonstra como sistemas computacionais podem auxiliar no monitoramento energético de missões espaciais, utilizando conceitos de sustentabilidade, geração de energia renovável e tomada de decisão automatizada.

A solução permite identificar riscos operacionais, gerar alertas automáticos e apoiar o gerenciamento eficiente dos recursos energéticos da missão.
