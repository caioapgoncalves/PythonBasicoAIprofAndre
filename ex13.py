def calculadora(a, b, operacao):
    if operacao == "+":
        return a+b
    elif operacao == "-":
        return a-b
    elif operacao == "*":
        return a*b
    elif operacao == "/":
        return a/b
    else:
        print("Operação inválida")

#testes
print(calculadora(10, 5, "+"))
print(calculadora(10, 5, "-"))
print(calculadora(10, 5, "*"))
print(calculadora(10, 5, "/"))