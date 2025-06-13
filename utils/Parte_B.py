from utils.colors_fx import blue, green, red
from utils.fx import clear, parse_input, exit_test, finish_indication, bis,ag



def par_impar(yrs = []):
    if len(yrs)==0: return
    cont = [0,0]
    for y in yrs:
        cont = [cont[0]+1, cont[1]] if y%2 == 0 else [cont[0], cont[1]+1]
    clear()
    blue('La cantidad de años pares e impares son: ')
    blue('Pares: ', '')
    green(cont[0])
    blue('Impares: ', '')
    green(cont[1])
    finish_indication()

def gz(yrs = []):
    clear()
    if len(yrs)==0: return
    yrs.sort()
    if yrs[0] < 2000:
        green('Grupo Z')
    else:
        blue('Hay integrantes que nacieron antes del 2000')
    finish_indication()

def bisiesto(yrs = []):
    clear()
    if len(yrs) == 0: return
    for y in yrs:
        if bis(y):
            green('Tenemos un año especial')
            finish_indication()
            return
    green('No hay año especial')
    finish_indication()

def producto_cartesiano(yrs = []):
    if len(yrs) == 0: return
    resultado=[]
    ages = ag(yrs)
    for i in yrs:
        for j in ages:
            resultado.append((i,j))
    clear()
    blue('El producto cartesiano entre años y edades es: ')
    green(resultado)
    finish_indication()