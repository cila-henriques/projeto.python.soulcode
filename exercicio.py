# Exercícios

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero = int(input("Insira o número: ")) 

if numero % 2 == 0:
    print("Par")
else: 
    print("Ímpar")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input("QUal é a sua idade: ")) 

if idade >= 0 and idade <=12:
    print("Criança")
elif idade >= 13 and idade <=18:
    print("Adolescente")
else:
    print("Adulto")

 #3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
 
 
 
 # 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

Exercícios
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

Crie uma docstring para a função exibir_nome_do_programa()
Crie uma docstring para a função exibir_opcoes()
Crie uma docstring para a função finalizar_app()
Crie uma docstring para a função opcao_invalida()
Crie uma docstring para a função exibir_subtitulo(texto)
Crie uma docstring para a função cadastrar_novo_restaurante()
Crie uma docstring para a função listar_restaurantes()
Crie uma docstring para a função alternar_estado_restaurante()
Crie uma docstring para a função escolher_opcao()
Crie uma docstring para a função main()

1 - Crie um código que mostre na tela a mensagem Estou criando meu primeiro código.


2 - Crie um código que mostre na tela a mensagem Olá meu nome é (Coloque seu nome).


3 - Elabora um código que mostre em uma linha a mensagem Olá usuário  e na outra linha a mensagem  Seja bem vindo.


4 - Mostre para o usuário a mensagem Estou realizando o curso da SoulCode.


5 - Crie um algoritmo que mostre na para o usuário a mensagem Estou aprendendo como mostrar mensagem para o usuário.


Atividades - Variáveis - Tipo de Dados


1 - Crie uma variável do tipo inteiro com o nome de numero


2 - Crie uma variável do tipo real com o nome de numero_virgula.

    1. Imprima a frase Escola de Dados da Alura!.
       print('Escola de Dados da Alura!')

Imprima seu nome e seu sobrenome seguindo a estrutura abaixo:
Nome: [seu nome]
Sobrenome: [seu sobrenome]
print('Nome: [seu nome]')
print('Sobrenome: [seu sobrenome]')
print('Nome: Mirla')
print('Sobrenome: Borges')



3. Imprima o seu primeiro nome letra a letra. Por exemplo, meu nome é Mirla, então eu obtenho a seguinte saída:
M
I
R
L
A
print('M')
print('I')
print('R')
print('L')
print('A')


4. Imprima o dia do seu nascimento em formato dia mês ano. Lembrando que os valores de dia e ano não podem estar entre aspas. Supondo uma data de aniversário dia 28 de fevereiro de 2003, o formato deve estar como no exemplo abaixo:
28 fevereiro 2003
print(28, 'fevereiro', 2003)

5.Imprima, em um único print, o atual ano que você está fazendo esse curso. O valor do ano deve ser um dado numérico e a saída do print deve ser a seguinte 
Ano atual: [ano]
print('Ano atual:',2023)
----------------------------------------------------------------------------------------------------------------------------------------------



projeto = ['01', '2']
i == 0
print('`Projeto 01: ', projeto)

for projetos in projeto: 
    print( f'Projeto 0 {i = i + 1}:', projetos)
    
