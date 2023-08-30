def ohce(palabra):
    palabra = palabra.lower().replace(" ", "")
    reversa = palabra[::-1]
    if palabra == reversa:
        return reversa + "\n" + "¡Bonita palabra!"
    return reversa