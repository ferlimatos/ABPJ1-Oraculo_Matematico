# Oráculo Financeiro

## Descrição do projeto
O **Oráculo Financeiro** é uma aplicação em Python desenvolvida para auxiliar no planejamento financeiro doméstico. O programa permite que o usuário registre sua renda mensal e categorize seus principais gastos (água, energia, aluguel e cartão), fornecendo um diagnóstico sobre a saúde financeira do mês.

Este é o meu primeiro projeto da disciplina de Python Iniciante integrante da minha jornada no curso técnico de Desenvolvimento Web e Mobile da Escola do Futuro José Luiz Bittencourt, em Goiânia.

## Objetivo
O objetivo é desenvolver um sistema simples e funcional que aplique conceitos básicos de lógica de programação, como entrada de dados, cálculos matemáticos e estruturas condicionais, resultando em uma ferramenta útil para controle de orçamento pessoal.

## Tecnologias Utilizadas
- Linguagem: Python 3.x
- Ferramentas: VS Code
- Modelagem: Draw.io (para o fluxograma)

## Estrutura do Projeto
- `main.py` → Arquivo principal com a lógica do programa.
- `README.md` → Documentação completa do projeto.
- `Oráculo Financeiro.drawio.png` → Imagem do fluxograma da aplicação.

## Como Executar o Projeto
1.  Certifique-se de ter o **Python 3.x** instalado.
2.  Faça o download ou clone este repositório.
3.  Navegue até a pasta do projeto.
4.  Execute o comando: `python main.py`.

## Funcionalidades
- Entrada de dados para renda e quatro categorias de gastos (água, energia, aluguel e cartão).
- Cálculo automático do gasto total e do saldo final.
- Diagnóstico em tempo real: alerta se o orçamento está positivo ou estourado.

## Lógica e Variáveis
O sistema utiliza as seguintes variáveis para o processamento:
| Variável | Descrição | Tipo de Dado |
| :--- | :--- | :--- |
| `nome` | Nome do usuário | `string` |
| `renda_mensal` | Salário ou ganhos totais do mês | `float` |
| `total_agua` | Gasto com fatura de água | `float` |
| `total_energia` | Gasto com fatura de luz | `float` |
| `total_aluguel` | Valor fixo de moradia | `float` |
| `total_cartao` | Despesas variadas no crédito | `float` |
| `gastos_total` | A soma de todas as despesas acima | `float` |
| `saldo_final` | O que sobra após o pagamento das contas | `float` |
| `valor_que_falta` | Armazena o valor positivo da dívida após o processamento da função abs() | `float` |

### Fórmulas de Processamento:
* **Cálculo de Despesas:** `gastos_total = total_agua + total_energia + total_aluguel + total_cartao`
* **Cálculo de Saldo:** `saldo_final = renda_mensal - gastos_total`
* **Tratamento de Dados:** `valor_que_falta = abs(saldo_final)` 

### Regras de Decisão:
* **Se** `saldo_final >= 0`: Exibir que o orçamento está positivo.
* **Se** `saldo_final < 0`: Exibir alerta de orçamento estourado.

## Fluxograma do Projeto:
Para facilitar a compreensão do sistema, elaborei este fluxograma que detalha o caminho que a informação percorre:

![Fluxograma](Oráculo%20Financeiro.drawio.png)

## Aprendizados
- Manipulação de variáveis e tipos de dados em Python.
- Aplicação de estruturas condicionais (`if/else`) para tomada de decisão.
- Documentação de projetos e criação de fluxogramas para planejar a lógica antes do código.
- Aprendi a usar a função abs() para transformar números negativos em valores absolutos e melhorar a compreensão do usuário.
- Apliquei f-strings para exibir os valores com duas casas decimais, garantindo o formato correto de Real (R$).

## Autores
**Fernanda Matos** – Desenvolvimento Web e Mobile – Python Iniciante.
