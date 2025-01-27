peso = input('informe seu peso: ')
altura = input('informe sua altura: ')

if peso.strip() != ' ' and altura.strip() !=' ':
     try:
          peso = float(peso)
          altura = float(altura)

          imc = peso / pow(altura, 2)

          print(f'Seu imc é {imc:.2f}')


          if imc < 18.5:
               print('Abaixo do peso')
          elif imc <= 18.5:
               print('Peso Normal')
          elif imc <= 25:
               print('Sobrepeso')
          elif imc <= 30:
               print('Obesidade Grau I')
          elif imc <= 35:
               print('Obesidade Grau II')
          else:
               print('Obesidade grau III ou Mórbida')

     except ValueError:
        print('Por favor, insira números válidos para peso e altura.')
     
else:

     print('Preenche todos os campos corretamente, sem deixar espaços em branco ou colocar letras!')
