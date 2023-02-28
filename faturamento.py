import json

faturamento = json.loads(dados)

last_day = 0 #ultimo dia do mes
day_zero = 0 #quantidade de dias que houve faturamento zero (feriados e fim de semana)
less_fact = 100000000000000 #valor da menor apuracao diaria do mes
more_fact = 0 #valor da maior apuracao diaria do mes
day_less = 0 #dia que menos apurou no mes
day_nice = 0 #dia que mais apurou no mes
all = 0 #soma de todos os valores do mes
for day in faturamento:
  
  if day['valor'] == 0:
    day_zero += 1
    last_day = day['dia']
    
  else:
    if day['valor'] < less_fact:
      less_fact = day['valor']
      day_less = day['dia']
      
    if day['valor'] > more_fact:
      more_fact = day['valor']
      day_nice = day['dia']
      
    last_day = day['dia']
    all += day['valor']

media = all/(last_day - day_zero)

print("O menor valor obtido foi de %.2f no dia %d" % (less_fact, day_less))
print("O maior valor obtido foi de %.2f no dia %d" % (more_fact, day_nice))

cont_super = 0 #contador de dias que houve superfaturamento em relacao a media mensal

for day in faturamento:
  if day['valor'] > media:
    cont_super += 1

print("Por %d dias, o faturamento diario foi maior do que a media mensal" % cont_super)
