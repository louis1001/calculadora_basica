def interpretar(codigo):
    a = int(codigo[0])

    sim = codigo[1]

    b = int(codigo[2])

    if sim == "+":
        return a + b
    if sim == "-":
        return a - b
    if sim == "*":
        return a * b
    if sim == "/":
        return a / b

entrada = input("> ")

resultado = interpretar(entrada)
print("El resultado es: ", resultado)
