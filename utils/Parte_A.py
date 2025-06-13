####################################### FUNCIONES ###############################################
def ingresar_dnis():
    dnis = []
    cont = 0
    print("Ingrese DNIs uno por uno - debe ingresar al menos dos -. Escriba 'fin' para terminar:")
    while True:
        entrada = input("DNI: ")
        if entrada.lower() == 'fin':
            if(cont >= 2):
                break
            else:
                return 'e'
        elif entrada.isdigit():
            dnis.append(entrada)
            cont += 1
        elif entrada.lower() == 'e':
            return 'e'
        else:
            print("Por favor, ingrese solo números.")
    return dnis

def obtener_conjuntos(dnis):
    conjuntos = []
    for dni in dnis:
        conjuntos.append(set(dni))
    return conjuntos

def operaciones_conjuntos(conjuntos):
    print("\nOperaciones entre Conjuntos:")
    union = set.union(*conjuntos)
    interseccion = set.intersection(*conjuntos)
    diferencia = conjuntos[0] - conjuntos[1]
    diferencia_simetrica = conjuntos[0] ^ conjuntos[1]

    print(f"Unión: {sorted(union)} / Los digitos que aparecen en ambos conjuntos")
    print(f"Intersección: {sorted(interseccion)}")
    print(f"Diferencia (Conjunto A - Conjunto B): {sorted(diferencia)} / Los digitos que estan en A y no en B")
    print(f"Diferencia simétrica (A Δ B): {sorted(diferencia_simetrica)}")

def frecuencia_digitos(dnis):
    print("\nFrecuencia de cada dígito:")
    for i, dni in enumerate(dnis):
        print(f"\nDNI {dni} (Conjunto {chr(ord('A') + i)}):")
        frecuencias = {}
        for digito in dni:
            if digito in frecuencias:
                frecuencias[digito] += 1
            else:
                frecuencias[digito] = 1
        for digito in sorted(frecuencias):
            print(f"Dígito {digito}: {frecuencias[digito]} vez/veces")

def suma_digitos(dnis):
    print("\nSuma total de los dígitos por DNI:")
    for i, dni in enumerate(dnis):
        suma = sum(int(d) for d in dni)
        print(f"DNI {dni} (Conjunto {chr(ord('A') + i)}): Suma = {suma}")





