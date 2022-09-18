# Enrique Cuevas Arias
# 19310400
# Sistemas Expertos

pos = 0
juego = 0


print("Bienvenido al Adivina quien version Avatar La leyenda de Aang")
print("Espero que te diviertas")
print("")
print("")
print("Instrucciones: Responder tribu o nacion dependiendo de tu personaje (todo minusculas)\ndespues solamente responder si o no como estan mostrados aqui (todo minusculas)")
print("Empecemos")
print("")
print("")
while(juego == 0):
    
    while (pos == 0):
       print("¿Tu personaje es de una tribu o una nacion? ")
       region = input()
       if region == "tribu":
        print("Perfecto entonces tu personaje pertenece a la tribu del agua o a la tribu del aire")
        pos = 1
       if region == "nacion":
        print("Perfecto entonces tu personaje pertenece a la nacion del fuego o a la nacion de la tierra")
        pos = 8
       if (region != 'tribu' and region != 'nacion'):  print("Respuesta invalida intentalo de nuevo") 
       

    while(pos == 1):
       print("¿La tribu de su personaje se le considera que esta extinta? ")
       extinta = input()
       if extinta == "si":
        print("Esto me indica que su personaje pertenece a la tribu del aire")
        pos = 2
       if extinta == "no":
        print("Esto me indica que su personaje pertenece a la tribu del agua")
        pos = 3
       if (extinta != 'si' and extinta != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 2):
       print("¿Tu personaje es humano?")
       humano = input()
       if humano == "si":
         print("Su personaje es un monje")
         pos = 4
       if humano == "no":
         print("Su personaje es una de las mascotas del Avatar")
         pos = 5 
       if (humano != 'si' and humano != 'no'):  print("Respuesta invalida intentalo de nuevo") 

    while(pos == 3):
       print("¿Su personaje pertenece al equipo avatar?")
       Equipo_avatar = input() 
       if Equipo_avatar == "si":
        print("Entonces su personaje acompaña al Avatar durante todo su viaje")
        pos = 6
       if Equipo_avatar == "no":
        print("Entonces su personaje conoce al Avatar pero no es parte de su equipo")
        pos = 7       
       if (Equipo_avatar != 'si' and Equipo_avatar != 'no'):  print("Respuesta invalida intentalo de nuevo") 

    while(pos == 4):
       print("¿Su personaje es el avatar?")
       avatar = input() 
       if avatar == "si":
        print("Entonces su personaje es el Avatar Aang")
        print("")
        pos = 15
       if avatar == "no":
        print("Entonces su personaje es el monje Gyatso")
        print("")
        pos = 15       
       if (avatar != 'si' and avatar != 'no'):  print("Respuesta invalida intentalo de nuevo")
    
    while(pos == 5):
       print("¿Su personaje tiene 6 patas?")
       patas = input() 
       if patas == "si":
        print("Entonces su personaje es Appa")
        print("")
        pos = 15 
       if patas == "no":
        print("Entonces su personaje es Momo")
        print("")
        pos = 15       
       if (patas != 'si' and patas != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 6):
       print("¿Su personaje es maestro agua?")
       agua = input() 
       if agua == "si":
        print("Entonces su personaje es Katara")
        print("")
        pos = 15 
       if agua == "no":
        print("Entonces su personaje es Sokka")
        print("")
        pos = 15       
       if (agua != 'si' and agua != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 7):
       print("¿Su personaje le debe la vida al espiritu de la luna?")
       luna = input() 
       if luna == "si":
        print("Entonces su personaje es la princesa Yue")
        print("")
        pos = 15
       if luna == "no":
        print("Entonces su personaje es Hakoda")
        print("")
        pos = 15       
       if (luna != 'si' and luna != 'no'):  print("Respuesta invalida intentalo de nuevo")

##################################################################################################################################################

    while(pos == 8):
       print("¿La nación de tu personaje fue la que empezo la guerra?")
       guerra = input() 
       if guerra == "si":
        print("Esto me indica que su personaje pertenece a la nacion del fuego")
        pos = 9
       if guerra == "no":
        print("Esto me indica que su personaje pertenece a la nacion de la tierra")
        pos = 10       
       if (guerra != 'si' and guerra != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 9):
       print("¿Su personaje es hombre?")
       hombre = input() 
       if hombre == "si":
        print("Esto quiere decir que su personaje ha convivido con el Avatar")
        pos = 11
       if hombre == "no":
        print("Esto quiere decir que su personaje es parte del equipo que manda el señor del fuego para capturar al Avatar")
        pos = 12       
       if (hombre != 'si' and hombre != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 10):
       print("¿Su personaje es maestro tierra?")
       tierra = input() 
       if tierra == "si":
        print("Entonces su personaje es amigo del avatar")
        pos = 13
       if tierra == "no":
        print("Entonces su personaje conoce al avatar")
        pos = 14       
       if (tierra != 'si' and tierra != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 11):
       print("¿Su personaje le gusta el te, el paisho, y de seguro huele a Hotcakes?")
       gustos = input() 
       if gustos == "si":
        print("Su personaje es el General/tio Iroh")
        print("")
        pos = 15
       if gustos == "no":
        print("Su personaje es el principe Zuko")
        print("")
        pos = 15      
       if (gustos != 'si' and gustos != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 12):
       print("¿Su personaje es maestro fuego?")
       fuego = input() 
       if fuego == "si":
        print("Su personaje es la princesa Azula")
        print("")
        pos = 15
       if fuego == "no":
        print("Su personaje es Mai novia del principe Zuko")
        print("")
        pos = 15      
       if (fuego != 'si' and fuego != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 13):
       print("¿Su personaje invento el metal control?")
       metal = input() 
       if metal == "si":
        print("Su personaje es Toph")
        print("")
        pos = 15
       if metal == "no":
        print("Su personaje es Bumi")
        print("")
        pos = 15      
       if (metal != 'si' and metal != 'no'):  print("Respuesta invalida intentalo de nuevo")

    while(pos == 14):
       print("¿Su personaje es un guerrero entrenado?")
       guerrero = input() 
       if guerrero == "si":
        print("Su personaje es Suki")
        print("")
        pos = 15
       if guerrero == "no":
        print("Su personaje es el rey de Ba Sing Se")
        print("")
        pos = 15      
       if (guerrero != 'si' and guerrero != 'no'):  print("Respuesta invalida intentalo de nuevo")                      

    if pos == 15 :
      print("He acertado a tu personaje")
      res = input()

      if res == "si":
        print("He acertado, suerte a la proxima")
      if res == "no":
        print("Me has vencido") 
        
      print("¿quieres jugar otra vez?") 
      vjuego = input()
      if vjuego == "si":
        print("Muy bien empecemos de nuevo")
        print("")
        pos = 0
      if vjuego == "no":
        print("Hasta pronto")
        juego = 1