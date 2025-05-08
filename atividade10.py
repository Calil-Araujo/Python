codigos_brutos = ["abc123", "def456", 123456, "ghi789", "abc123", None, "jkl012", "GHI789", "", "mino345"]

codigos_validos = set()

codigos_invalidos = []

for codigo in codigos_brutos:
    try:
        
        codigo_processado = codigo.upper()

        codigos_validos.add(codigo_processado)

        if codigo_processado == "":
            codigos_validos.remove(codigo)
            codigos_invalidos.append(codigo)

    except TypeError:
        codigos_invalidos.append(codigo)
    except AttributeError:
        codigos_invalidos.append(codigo)

print(f"-"*60)
print(f"Códigos validos: {codigos_validos}")
print(f"Códigos invalidos: {codigos_invalidos}")
print(f"-"*60)