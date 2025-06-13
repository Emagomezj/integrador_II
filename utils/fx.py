from os import system as sys
from utils.colors_fx import red,green,blue,res

def clear():
    sys('cls')

def exit_test(var):
    return str(var).lower() == 'e'

def parse_input(pars, frase = '', err = '', condition = lambda x: True):
    while True:
        try:
            var = input(frase)
            if(var == 'e' or var == 'E'):
                return var
            pars_var = pars(var)
            if(condition(pars_var)):
                return pars_var
            else:
                raise ValueError(err)
        except:
            if(err):
                red(err)
                print(chr(27)+"[0m")

def finish_indication():
    blue('\nPulse enter o ingrese cualquier tecla para salir', '')
    parse_input(str)

def bis(y):
    if (y%4==0 and y%100 != 0) or (y%400==0):
        return True
    else:
        return False 
def ag(yrs):
    ages = []
    for y in yrs:
        ages.append(2025-y)
    return ages