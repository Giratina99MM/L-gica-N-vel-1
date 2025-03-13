#8. Implemente um programa que na primeira linha faça um print perguntando o nome do usuário e, na linha 2, chame a função input() para capturar o valor do teclado e armazenar na memória do computador.

#Depois de concluído o exercício anterior, pode surgir uma dúvida, como recuperar o valor da memória? Para isso, teremos que usar algo como uma caixa que chamaremos de variável. Essa variável pode ter qualquer nome desde que não começe com números e não tenha caracteres especiais.

#Veja um exemplo ao criar uma variavel para armazenar o nome de uma pessoa em Python, simplesmente digitamos o nomeDaVariavel + símbolo de atribuição + valor

#Exemplo de 5 variaveis com valores diferentes:
#nome1 = “João”
#nome2 = “Márcio”
#nome3 = “Jeferson”
#nome4 = “Frederico”
#nome5 = “Gilmar”
#Observe que os nomes acima estão entre aspas, isso sempre é necessário quando vamos armazenar uma frase a uma variável. Em outros casos como números, não usaremos as aspas e colocaremos o valor diretamente.
#Exemplo de algumas variáveis em Python com valores diferentes:

#numero1 = 5
#numero2 = 9
#idade = 20
#residencia = 16
#cep = 26290876

print("Qual o seu nome?")
input()
#No exercício 8, usamos a variável input() e ela liberou o teclado para o usuário digitar um valor. Quando pressionamos enter, o valor foi pra memória, mas como podemos acessála?
#Para isso, crie uma variável e com o símbolo de atribuição = coloque o input() como exemplificado abaixo
#nome = input()
nome = input()

#O código acima, libera o teclado para o usuário digitar seu nome e guarda esse valor numa variável que é como uma caixinha para guardar quase qualquer coisa.

#Se em algum momento do software quisermos mostrar o valor guardado dentro dessa variável, podemos usar a função já conhecida print() e, dentro dos parênteses, colocar a variável criada antes nome

#Exemplo:

#print(nome)
