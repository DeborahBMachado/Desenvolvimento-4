def calculadora(num1, num2, operacao):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtração":
        return num1 - num2
    elif operacao == "multiplicação":
        return num1 * num2
    elif operacao == "divisão":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero!"
    else:
        return 0

# Exemplo de uso:
resultado = calculadora(10, 5, "soma")
print(f"Resultado da soma: {resultado}")
