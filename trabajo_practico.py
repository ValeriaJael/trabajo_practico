#Nombre:Valeria Jael Bela
#Al principio quise que le pida el nombre al usuario
nombre = input("Ingrese un nombre por favor, para iniciciar un juego")
def saludar(nombre):
    print(f"hola{nombre}")
saludar(nombre)
#aquí hice tres funciones una que pide el nombre del usuario, otra donde hay una calculadora para el usuario y la ultima es de numeros pares o impares.
def es_par (calculadora):
          if calculadora % 2 == 0:
             print(f"El numero es par {calculadora}")
          else:
            print(f"EL numero es impar {calculadora} ")

def calculadora (num):
         suma= num +2
         resta= num - 2
         mult = num * 2
         divi= num / 2
         return suma, resta, mult, divi

#Aqui hay un while con opciones para que el usuario eliga
opcion = int (input("Eliga una opcion del juego de 1 al 5, la primera es para numeros impares o pares, la segunda para calcular numeros, la tercera para lista de frutas, la cuarta opcion es para cambiar mayusculas a minusculas y la ultima pra salir del juego"))
while 6>opcion:
   if opcion == 1:
       print("Juego de impar o par") 
       print("En este juego cada números que pongas, el programa te va a decir si impar o par ")

       calculadora = int(input("Ingrese un numero para inciar este juego"))

       par = es_par (calculadora)
       print(par)    
   elif opcion == 2:
      print("Juego de la calculadora")
      print("En este juego cada número que pongas va hacer multiplicado por dos, dividido por dos, sumado por dos y restado por dos")
      num = int(input("Ingrese un numero"))

      res =  calculadora(num)
      print(res)
   elif opcion == 3:
        print("Juego de la fruta")
        listadefrutas=["mango", "manzana", "pera", "Kiwi"]
        print("Aqui tiene las frutas en orden por separado")
        for lista in listadefrutas:
           print(f"Aca la lista {lista}")
        print("TU podras quitar y poner una fruta nueva")
        quitar = input("quite una fruta por favor")
        listadefrutas.remove(quitar)
        agregue = input("Agregue una fruta por favor")
        listadefrutas.append(agregue)
        print("Hora le mostraremos como quedo la lista ordenada")
        listadefrutas.sort()
        print(listadefrutas) 
   elif opcion == 4:
        print("Aqui cada texto que ponga en mayusculas sera cambiado por minusculas")
        texto = input("Ingrese un texto para iniciar el juego")
        def cambiar_a_mayusculas(texto_de_usuario):
           return texto_de_usuario.lower()
        cambiar = cambiar_a_mayusculas(texto)
        print(cambiar) #tuve que dejar esta función aquí porque sino no funcionaba
   elif opcion == 5:
        print("Gracias por jugar <3")
        print("Saliste del juego")
        break
   opcion = int (input("Eliga una opcion del juego"))







      
      

      


