
def tomar_numero(codigo, pos):
    resultado = codigo[pos]
    pos += 1

    while pos < len(codigo) and codigo[pos].isdigit():
        resultado += codigo[pos]
        pos += 1

    return int(resultado), pos

def interpretar(codigo):
    codigo = codigo.replace(" ", "")
    a, pos = tomar_numero(codigo, 0)

    sim = codigo[pos]
    pos += 1

    b, _ = tomar_numero(codigo, pos)

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
