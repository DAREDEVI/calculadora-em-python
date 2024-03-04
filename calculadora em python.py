def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b

print("Escolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado: ", soma(num1, num2))
elif opcao == 2:
    print("Resultado: ", subtracao(num1, num2))
elif opcao == 3:
    print("Resultado: ", multiplicacao(num1, num2))
elif opcao == 4:
    print("Resultado: ", divisao(num1, num2))
else:
    print("Opção inválida")
