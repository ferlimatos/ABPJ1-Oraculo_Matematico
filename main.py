# Ler nome do usuário
nome = input('Informe seu nome completo: ')
print(f'Olá, {nome}!')

# Receber informações do salário e gastos
renda_mensal = float(input('Qual é o valor líquido de seu salário? '))
total_agua = float(input('Qual é o valor total da conta de água esse mês? '))
total_energia = float(input('Qual é o valor total da conta de energia esse mês? '))
total_aluguel = float(input('Qual é o valor do aluguel? '))
total_cartao = float(input('Qual é o valor da fatura de seu cartão esse mês? '))

# Soma das despesas
gastos_total = total_agua + total_energia + total_aluguel + total_cartao

# Mostrar total de gastos
print(f'O valor total de seus gastos nesse mês é de R$ {gastos_total:.2f}.') # :.2f formata o número para duas casas decimais

# Cálculo do saldo final
saldo_final = renda_mensal - gastos_total

# Verificação do orçamento
if saldo_final >= 0:
    print(f"Parabéns! Seu orçamento está positivo. Você tem R$ {saldo_final:.2f} sobrando.")
else:
    valor_que_falta = abs(saldo_final) # Extrai o valor absoluto do saldo negativo
    print(f"Atenção! Seu orçamento estourou. Você precisa de mais R$ {valor_que_falta:.2f} para quitar suas contas.")

# Aprendizado
# Aplicação de estruturas condicionais (if/else) para tomada de decisão.
# Documentação de projetos e criação de fluxogramas para planejar a lógica antes do código.
# Aprendi a usar a função abs() para transformar números negativos em valores absolutos e melhorar a compreensão do usuário.
# Apliquei f-strings para exibir os valores com duas casas decimais, garantindo o formato correto de Real (R$).
