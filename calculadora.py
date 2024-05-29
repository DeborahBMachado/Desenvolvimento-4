#função para desenvolvimento de uma calculadora
def calculadora():
  a = float(input("Digite o primeiro numero: \n"))
  b = float(input("Digite o segundo numero: \n"))
  #instruções para definição das operações
  operacao = input("""Digite a operação desejada conforme abaixo:
+ para adicao
- para subtracao
* para multiplicacao
/ para divisao\n""")
    #estruturas condicionais para os cálculos dependendo da operação escolhida
  if operacao == "+":
    print("{} + {} = ".format(a, b))
    print(a + b)

  elif operacao == "-":
      print("{} - {} = ". format(a, b))
      print(a - b)
    
  elif operacao == "*":
      print("{} * {} = ". format(a, b))
      print(a * b)

  elif operacao == "/":
    print("{} / {} = ". format(a, b))
    print(a / b)
  
  else:
    print("Operacao invalida")
 
calculadora() # chamada da função
