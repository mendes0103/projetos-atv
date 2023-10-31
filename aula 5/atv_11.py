import os 
os.system("cls")
print("calculo sa sobra de um saco de raçao apos 5 dias")
peso_kg= float(input("digite o peso do saco de raçao em kilos: "))
gato1= float(input("digite a quantidade fornecida ao primeiro gato: "))
gato2= float(input("digite a quantidade de raçao fornecida ao segundo gato: "))
consumo= (gato1 + gato2) * 5
resta= peso_kg * 1000 - consumo
print (f"sobrara no saco {resta} gramas")