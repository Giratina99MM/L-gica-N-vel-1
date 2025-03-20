#13 - Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias
print("Idade em anos")
idade1 = int(input())
print("Idade em meses")
idade2 = int(input())
print("Idade em dias")
idade3 = int(input())
print(idade1 * 365 + idade2 * 30 + idade3 * 1)
