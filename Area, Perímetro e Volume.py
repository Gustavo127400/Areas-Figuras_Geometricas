import math 
print('Seja bem-vindo ao programa do Gustavo!')
print('Siga-me nas redes sociais: @gustavosouzzaa___')
print('____________________________________________________________________________')
figura = input('Qual é a figura geométrica? ')
 #FIGURA GEOMÉTRICA | QUADRADO
if(figura == 'Quadrado'):
    medida = input('Qual medida? Área, Volume ou Perímetro? ')
    #MEDIDA | ÁREA
if(medida == 'Área'):
    b = float(input('Qual o valor da base? '))
    h = float(input('Qual o valor da altura? '))
    formula = b*h
    print('A área do quadrado é: ' +  str(formula))
#MEDIDA | VOLUME    
elif(medida == 'Volume'):
     b = float(input('Qual o valor da base? '))
     h = float(input('Qual o valor da altura? '))
     c = float(input('Qual o valor do comprimento? '))
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
      
else:
    #SE CASO NÃO HOUVER DADOS DE ENTRADA, CHAMARÁ ESSA CONDICIONAL 
        print('Medida não encontrada!')
        print('Área, Volume ou Perímetro') 
#FIGURA GEOMÉTRICA | TRIÂNGULO         
if (figura == 'Triângulo'):
    medida = input('Qual medida? Área, Volume ou Perímetro? ')
#MEDIDA | ÁREA
if(medida == 'Área'):
    b = float(input('Qual é o valor da base? '))
    h = float(input('Qual é o valor da altura? '))
    formula = (b * h) / 2
    print('A área do triângulo é: ' + str(formula))
    
elif(medida == 'Perímetro'):
#MEDIDA | PERÍMETRO
    l2 = float(input('Qual o valor da parte inferior? '))
    l3 = float(input('Qual o valor do lado esquerdo? '))
    l4 = float(input('Qual o valor do lado direito? '))
    formula = l1+l2+l3+l4
    print('O perímetro do triângulo é: ' + str(formula))
        #MEDIDA | VOLUME 
elif (medida == 'Volume'):
        b = float(input('Qual é o valor da base? '))
        h = float(input('Qual é o valor da altura? '))
        area2 = (b * h) / 2
        formula = area2 * h
        print('O volume do triângulo é: ' + str(formula))
    
else:
    #SE CASO NÃO HOUVER DADOS DE ENTRADA, CHAMARÁ ESSA CONDICIONAL 
        print('Medida não encontrada!')
        print('Área, Volume ou Perímetro') 
# FIGURA GEOMÉTRICA | ESFERA 
if(figura == 'Esfera'):
  medida = input('Qual medida? Área, Volume ou Circunferência? ')  
if(medida == 'Área'):
    raio  = float(input('Qual o valor do raio? '))
    formula = 4*math.pi*raio**2
    print('A área da esfera é: ' + str(formula))
elif(medida == 'Volume'):
    raio = float(input('Qual o valor do raio? ' ))
    formula = (4*math.pi*raio**3)/2
    print('O volume da esfera é: ' + str(formula))
elif(medida == 'Circunferência'):
     raio = float(input('Qual o valor do raio? ' ))
     formula = 2*math.pi*raio
     print('A circunferência da esfera é: ' + str(formula))
else: 
#SE CASO NÃO HOUVER DADOS DE ENTRADA, CHAMARÁ ESSA CONDICIONAL 
        print('Medida não encontrada!')
        print('Área, Volume ou Perímetro') 
# FIGURA GEOMÉTRICA | RETÂNGULO 
if(figura == 'Retângulo'):
    medida = input('Qual medida? Área, Volume ou Perímetro? ')
if(medida == 'Área'):
    b = int(input('Qual o valor da base? '))
    h = int(input('Qual o valor da altura? '))
    formula = b*h
    print('A área do retângulo é: ' +  str(formula))
elif(medida == 'Volume'):
    b = float(input('Qual o valor da base? '))
    h = float(input('Qual o valor da altura? '))
    c = float(input('Qual o valor do comprimento? '))
    formula = b*h*c
    print('O volume do retângulo é: ' + str(formula))
elif(medida == 'Perímetro'):
    b = int(input('Qual o valor da base? '))
    h = int(input('Qual o valor da altura? '))
    formula = 2 * (b+h)
    print('O perímetro do retângulo é: ' +  str(formula))
else: 
#SE CASO NÃO HOUVER DADOS DE ENTRADA, CHAMARÁ ESSA CONDICIONAL 
    print('Medida não encontrada!')
    print('Área, Volume ou Perímetro')   
        
#FIGURA GEOMÉTRICA | LOSANGO         
#if(figura == 'Losango'):
 #   medida = input('Qual medida? Área, Volume ou Perímetro ') 
#if(medida == 'Área'):
 # dMaior = int(input('Qual é o valor da diagonal maior')) 
  # formula = (dMaior*dMenor)/2
   #print('A área do Losango é:' + str(formula))
#else:
 #   print('')
#elif(medida == 'Volume'):
 #  r = input('O triângulo é um sólido tridimensional ou figura plana bidimensional?')
#if(r == 'Sólido tridimensional'):
 #   tipos == input('Prisma ou Pirâmide?')
#if(tipos == 'Prisma'):    
 #   dMenor = int(input('Qual é valor da diagonal menor?'))
  #  dMaior = int(input('Qual é o valor da diagonal maior'))
   # v = (dMaior*dMenor)/2
    #print('O prisma de um losango sólido tridimensional é: ' + str(v))
#elif(tipos == ' Pirâmide' ):
 #  dMenor = int(input('Qual é valor da diagonal menor?'))
  # v = (dMaior*dMenor)/3
   # print('A pirâmide do losango plano bidimensional é: '+ str(v))
#elif(r == 'Figura plana bidimensional'):
 #   print('Não há volume!')
#   print('Por favor insira:')
 #   print('Figura plana bidimensional ou Sólido tridimensional.')
