#funcoes utilizadas

def percent_calc(cem, num):
  percent = (100*num)/cem
  return percent

#codigo fonte

state = ["SÃO PAULO", "RIO DE JANEIRO", "MINAS GERAIS", "ESPIRITO SANTO", "OUTROS ESTADOS"]
values = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
all = 180759.98

print("Olá, de acordo com os dados oferecidos ao software o percentual de valores de cada estado ficou da seguinte maneira:\n\n")

for i in range(5):
  if(i == 4):
    print("Para %s o percentual foi de %.2f por cento.\n" % (state[i], percent_calc(all, values[i])))
  else:
    print("Para o Estado de %s o percentual foi de %.2f por cento.\n" % (state[i], percent_calc(all, values[i])))