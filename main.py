from utils.colors_fx import blue, green, red
from utils.fx import clear, parse_input, exit_test, finish_indication
from components.Parte_B import par_impar, gz, bisiesto, producto_cartesiano
from components.Parte_A import ingresar_dnis, operaciones_conjuntos, frecuencia_digitos, suma_digitos, obtener_conjuntos
from constants.constants import yrs

def main():
    while True:
        clear()
        blue('Por favor indique que parte del trabajo desea probar: ')
        print('1. Parte A\n2. Parte B\nE. Salir')
        parte = parse_input(int,'', 'Debe ingresar una opción válida', lambda x: x in [1,2])
        if(exit_test(parte)): return
        while parte == 2:
            clear()
            print('Indique con un número entre 1 y 4 que ejercicio quiere probar. Ingrese E para salir')
            print('1. Contar pares e impares \n2. Grupo Z \n3. ¿Hay año bisiesto? \n4. Producto y edades\n5. Ver Parte A')
            opts = list(range(1,6))
            opt = parse_input(int,'','Ingrese una opción válida', lambda x: x in opts)
            if(exit_test(opt)): break 
            match opt:
                case 1: par_impar(yrs)
                case 2: gz(yrs)
                case 3: bisiesto(yrs)
                case 4: producto_cartesiano(yrs)
                case 5: parte = 1
        else:
            dnis = ingresar_dnis()
            if(exit_test(dnis)): 
                print('Redirigiendo al menú principal')
                finish_indication()
            else:
                conjuntos = obtener_conjuntos(dnis)
                print("\nConjuntos de dígitos únicos:")
                for i, c in enumerate(conjuntos):
                    print(f"Conjunto {chr(ord('A') + i)} → {sorted(c)}")

                operaciones_conjuntos(conjuntos)
                frecuencia_digitos(dnis)
                suma_digitos(dnis)
                finish_indication()

main()