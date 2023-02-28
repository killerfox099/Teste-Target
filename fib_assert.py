#Funções utilizadas

def fibonacci(num):
  lista = [0,1]
  for i in range(num):
    lista.append(lista[i] + lista[i+1])
  return lista

def fib_assert(num):
  list_fib = fibonacci(num)
  if num in list_fib:
    return True
  return False

#Código fonte
while True:
  print("*** Bem-vindo(a) ao reconhecedor FIB master ***")
  
  number_fib = 0
  while True:
    value = input("Insira um numero inteiro para sabermos se ele esta na sequencia de fibonacci ou não: ")
    try:
      number_fib = int(value)
      break
    except ValueError:
      print("Algo que voce digitou nao estava de maneira coerente com o sistema, tente novamente.\nDica: O sistema aceitara apenas numeros inteiros. Ex: 0, 1, 2, 3...\n\n")
  
  if fib_assert(number_fib) == True:
    print("\nParabens! Voce acabou de achar um numero da sequencia de Fibonacci. Que explendido! ", end = '' )
  else:
    print("Não foi dessa vez que encontramos um numero da sequencia de Fibonacci. Mas não desanime! ", end = '')
  stop = input("Gostaria de tentar mais uma vez (S/N)? ").upper()
  if stop == 'S':
    pass
  elif stop == 'N':
    print("\nTudo bem então, o programa está sendo finalizado. Obrigado Por usar FIB master.")
    break
  else:
    print("\nErro de entrada, o programa será finalizado. Obrigado por usar FIB master.")
  break