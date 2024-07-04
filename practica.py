def calculadora (num1, num2):
    suma = num1 + num2
    resta= num1 - num2
    multiplicacion= num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division

print(calculadora(3, 4))

        
def cambia_a_minusculas(cadena):
   return cadena.lower()

print(cambia_a_minusculas("PALABRA"))