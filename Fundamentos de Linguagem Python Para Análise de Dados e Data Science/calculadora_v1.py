# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

menu = int(input("\nSelecione o número da operação desejada:\n\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n\nDigite sua opção (1/2/3/4): "))

if menu == 1:
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))
    resultado = num1 + num2
    print("\n\n\n"f"{num1} + {num2} = {resultado}")
elif menu == 2:
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("\n\n\n"f"{num1} - {num2} = {resultado}")
elif menu == 3:
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"\n\n\n""{num1} * {num2} = {resultado}")
elif menu == 4:
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("\n\n\n"f"{num1} / {num2} = {resultado}")
    else:
        print("\nErro: Divisão por zero não é permitida.")
else:
    print("\nOpção inválida. Por favor, selecione uma opção válida (1/2/3/4).")
