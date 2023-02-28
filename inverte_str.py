def inversion(word):
  tam = len(word) -1
  invert = ""
  while tam != -1:
    invert += word[tam]
    tam -= 1
  return invert

while True:
  word = input("insira uma string: ")
  print("A palavra digitada ao contrario fica da seguinte maneira: %s" % inversion(word))
  try_again = input("\nDeseja inserir outra palavra (S/N)? ").upper()
  if try_again == "N":
    print("\nO programa esta sendo finalizado.")
    break