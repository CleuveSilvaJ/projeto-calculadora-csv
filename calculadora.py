def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero não é permitida."
    return a / b

print("Bem-vindo à Calculadora Simples!")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

if escolha == '1':
    print(f"Resultado da soma: {somar(num1, num2)}")
elif escolha == '2':
    print(f"Resultado da subtração: {subtrair(num1, num2)}")
elif escolha == '3':
    print(f"Resultado da multiplicação: {multiplicar(num1, num2)}")
elif escolha == '4':
    print(f"Resultado da divisão: {dividir(num1, num2)}")
else:
    print("Escolha inválida.")
