import math 
print('Seja bem-vindo ao programa do Gustavo!')
print('Siga-me nas redes sociais: @gustavosouzzaa___')
print('____________________________________________________________________________')
figura = input('Qual é a figura geométrica? ')
# FIGURA GEOMÉTRICA | QUADRADO
if(figura == 'Quadrado'):
    medida = input('Qual medida? Área, Volume ou Perímetro? ')
    #MEDIDA | ÁREA
    if(medida == 'Área'):
        b = int(input('Qual o valor da base? '))
        h = int(input('Qual o valor da altura? '))
        formula = b*h
        print('A área do quadrado é: ' +  str(formula))
    #MEDIDA | VOLUME    
    elif(medida == 'Volume'):
        b = int(input('Qual o valor da base? '))
        h = int(input('Qual o valor da altura? '))
        c = int(input('Qual o valor do comprimento? '))
        formula = b*h*c
        print('O volume do quadrado é: ' + str(formula))
    #MEDIDA | PERÍMETRO    
    elif(medida == 'Perímetro'):
        l1 = float(input('Qual o valor da parte superior? '))
        l2 = float(input('Qual o valor da parte inferior? '))
        l3 = float(input('Qual o valor do lado esquerdo? '))
        l4 = float(input('Qual o valor do lado direito? '))
        formula = l1+l2+l3+l4
        print('O Perímetro do quadrado é: ' + str(formula))
    #SE CASO NÃO HOUVER DADOS DE ENTRADA, CHAMARÁ ESSA CONDICIONAL   
    else:
        print('Medida não encontrada!')
        print('Área, Volume ou Perímetro') 
# FIGURA GEOMETRICA | TRIÂNGULO         
if(figura == 'Triângulo'):
    medida = input('Qual medida? Área, Volume ou Perímetro? ')
    if(medida == "Área"):
        b = int(input('Qual é o valor da base? '))
        h = int(input('Qual é o valor da altura? '))
        formula = (b*h)/2
        print('A área do triângulo é: ' + str(formula))
    elif(medida == "Perímetro"):
        l1 = float(input('Qual o valor da parte superior? '))
        l2 = float(input('Qual o valor da parte inferior? '))
        l3 = float(input('Qual o valor do lado esquerdo? '))
        l4 = float(input('Qual o valor do lado direito? '))
        formula = l1+l2+l3+l4
        print('O perímetro do triângulo é: ' + str(formula))
    elif(medida == 'Volume'):
        b = int(input('Qual é o valor da base? '))
        h = int(input('Qual é o valor da altura? '))
        area = (b*h)/2
        formula = area * h
        print('O volume do triângulo é: ' + str(formula)) 
    else:
        print('Medida não encontrada!')
        print(' Área, Volume ou Perímetro')
# FIGURA GEOMÉTRICA | ESFERA 
if(figura == 'Esfera'):
    medida = input('Qual medida? Área, Volume ou Perímetro? ')    
if(medida == 'Área'):
    raio  = int(input('Qual o valor do raio?' ))
    formula = 4*math.pi*raio**2
    print('A área da esfera é:' + str(formula))
elif(medida == 'Volume'):
    

# FIGURA GEOMÉTRICA | RETÂNGULO 
#(figura == 'Retângulo' or 'retangulo' or 'retângulo'): 
    b = int(input('Qual o valor da base? '))
    h = int(input('Qual o valor da altura? '))
    formula = b*h
    print('A área do retângulo é: ' +  str(formula))
# FIGURA GEOMÉTRICA | LOSANGO    
#(figura == 'Losango' or 'losango'):
    dMenor = int(input('Qual é valor da diagonal menor?'))
    dMaior = int(input('Qual é o valor da diagonal maior')) 
    formula = (dMaior*dMenor)/2
    print('A área do Losango é:' + str(formula))






