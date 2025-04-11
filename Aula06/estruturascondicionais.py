# Estruturas condicionais
nota = float(input("Qual é a sua nota: "))
if nota <= 0 or nota > 10:
    print("Nota inválida")
elif nota >= 9:
    print("Aprovado")
elif nota >= 7:
    print("Recuperação")
else: 
    print("Reprovado")
 