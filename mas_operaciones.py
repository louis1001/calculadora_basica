
def tomar_numero(codigo, pos):
    resultado = codigo[pos]
    pos += 1

    if resultado == "(":
        resultado, pos = tomar_expresiones(codigo, pos)
        pos += 1
        return resultado, pos

    while pos < len(codigo) and codigo[pos].isdigit():
        resultado += codigo[pos]
        pos += 1

    return int(resultado), pos

def tomar_expresiones(codigo, pos):
    resultado, pos = tomar_producto(codigo, pos)

    operadores = ["+", "-"]

    while pos < len(codigo) and (codigo[pos] in operadores):
        sim = codigo[pos]
        pos+=1

        siguiente_numero, pos = tomar_producto(codigo, pos)

        if sim == "+":
            resultado = resultado + siguiente_numero
        if sim == "-":
            resultado = resultado - siguiente_numero

    return resultado, pos

def tomar_producto(codigo, pos):
    resultado, pos = tomar_numero(codigo, pos)

    operadores = ["*", "/"]

    while pos < len(codigo) and (codigo[pos] in operadores):
        sim = codigo[pos]
        pos+=1

        siguiente_numero, pos = tomar_numero(codigo, pos)

        if sim == "*":
            resultado = resultado * siguiente_numero
        if sim == "/":
            resultado = resultado / siguiente_numero

    return resultado, pos

def interpretar(codigo):
    codigo = codigo.replace(" ", "")
    
    resultado, _ = tomar_expresiones(codigo, 0)
    return resultado

entrada = input("> ")

resultado = interpretar(entrada)
print("El resultado es: ", resultado)






