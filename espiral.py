import pygame

class Espiral:
    def __init__(self, texto_ventana: str, color_fondo: tuple):
        # Inicializar Pygame
        pygame.init()
        # Establecer el tamaño de la ventana
        self.tamaño_ventana = (800, 800)
        #Booleano para saber si el juego esta en ejecuccion:
        self.running = True
        # Crear la ventana
        self.pantalla = pygame.display.set_mode(self.tamaño_ventana)
        # Establecer el color de fondo a verde
        pygame.display.set_caption(texto_ventana)
        #Fuente y tamaño que vamos a utilizar:
        self.fuente = pygame.font.Font(None, 15)
        self.numero_imprimir = 1
        # Cambiar color fondo aceptanndo solo una tupla RGB ej: (255, 255, 255)
        try:
            self.pantalla.fill(color_fondo)
        except:
            print("Error: solo acepta tupla con este formato rgb: (255, 255, 255")
        # Tamaño de bloque ancho-alto de la cuadricula 5x5:
        self.tamaño_bloque = self.tamaño_ventana[0]/20
        #Color triangulos => numeros pares y impar
        self.color_pares = (227, 90, 120)
        self.color_impar = (120, 227, 90)

    def Bucle_Juego(self):

        # Bucle de Pygame

        while (self.running == True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Actualizar pantalla
            pygame.display.flip()

        # Si running == False => Salir de Pygame
        pygame.quit()

    def Crear_Espiral(self):
        #Numero de pasos que se va a mover y pone un numero en cada paso:
        cantidad_pasos = 1
        #Empezamos posicion en el centro de pantalla que es la la mitad de ancho y alto - (la mitad de cada bloque):
        pos_actual = [self.tamaño_ventana[0]/2-(self.tamaño_bloque/2), self.tamaño_ventana[1]/2-(self.tamaño_bloque/2)]


        def Direccion(pos_actual, direccion):
        #Funcion derecha-arriba-izquierda-abajo == 0, 1, 2, 3 => direccion
            if direccion == 0:
                #Cogemos posicion actual y le sumamos a x  tamaño de bloque
                pos_actual[0] = pos_actual[0] + (self.tamaño_bloque)
            if direccion == 1:
                #Cogemos posicion actual y le restamos a y tamaño de bloque
                pos_actual[1] = pos_actual[1] - (self.tamaño_bloque)
            if direccion == 2:
                #Cogemos posicion actual y le restamos a x tamaño de bloque
                pos_actual[0] = pos_actual[0] - (self.tamaño_bloque)

            if direccion == 3:
                #Cogemos posicion actual y le sumamos a y tamaño de bloque
                pos_actual[1] = pos_actual[1] + (self.tamaño_bloque)
        
        la_direccion = 0 #Empezamos con direccion derecha
        iterador_pasos = 0 #Esto es un simple iterador para saber en que paso esta y tiene que tiene como maximo
        # => Cantidad de pasos
        #Dibujamos el primer cuadrado central QUE NO ES PAR:
        pygame.draw.rect(self.pantalla, self.color_impar, (pos_actual[0], pos_actual[1], self.tamaño_bloque, self.tamaño_bloque))
        #Añadimos 1 al numero a imprimir en pantalla:
        self.numero_imprimir = self.numero_imprimir + 1
        for i in range(32):
                if cantidad_pasos == 1:
                    for p in range(2): 
                        Direccion(pos_actual, la_direccion) #Cambia de direccion

                        # Si el numero es primo imprimimos en pantalla:
                        if self.Es_Primo(self.numero_imprimir) == True:

                            #Dibujamos un triangulo con el primer punto x, y por defecto, luego + ancho del bloque, y por ultimo x, y por defecto menos y que añadimos tamaño del bloque:
                            pygame.draw.polygon(self.pantalla, self.color_pares, [pos_actual, (pos_actual[0]+self.tamaño_bloque, pos_actual[1]), (pos_actual[0], pos_actual[1]+self.tamaño_bloque)])
                        else:
                            # No es par
                            pygame.draw.rect(self.pantalla, self.color_impar, (pos_actual[0], pos_actual[1], self.tamaño_bloque, self.tamaño_bloque))
                    
                        #Cambiamos de direccion:
                        la_direccion = la_direccion+1
                        #+1 numero
                        self.numero_imprimir = self.numero_imprimir + 1
                    cantidad_pasos = cantidad_pasos+1
                    self.numero_imprimir = 4
                else:

                    for pasos in range(cantidad_pasos):
                        Direccion(pos_actual, la_direccion)
                        # Si el numero es primo imprimimos en pantalla:
                        if self.Es_Primo(self.numero_imprimir) == True:

                            #Dibujamos un triangulo con el primer punto x, y por defecto, luego + ancho del bloque, y por ultimo x, y por defecto menos y que añadimos tamaño del bloque:
                            pygame.draw.polygon(self.pantalla, self.color_pares, [pos_actual, (pos_actual[0]+self.tamaño_bloque, pos_actual[1]), (pos_actual[0], pos_actual[1]+self.tamaño_bloque)])
                        else:
                            # No es par
                            pygame.draw.rect(self.pantalla, self.color_impar, (pos_actual[0], pos_actual[1], self.tamaño_bloque, self.tamaño_bloque))

                        self.numero_imprimir = self.numero_imprimir + 1
                
                    iterador_pasos = iterador_pasos + 1
                    #Cambiamos de direccion:
                    la_direccion = la_direccion+1
                    #Cuando cantidad de pasos sea = 2
                    #añadimos un paso mas y reiniciamos el iterador
                    if iterador_pasos == 2:
                        cantidad_pasos = cantidad_pasos+1
                        iterador_pasos = 0

                    if la_direccion == 4: # Si la direccion es 4 que no existe reseteamos a derecha => 0
                        la_direccion = 0

        pygame.display.flip() # Actualizamos pantalla

                
    def Es_Primo(self, numero):
        if numero < 2:
            return False

        for i in range(2, numero):
            if (numero%i == 0):
                return False

        return True





juego = Espiral("Espiral Ulam", (177, 242, 240))
juego.Crear_Espiral()
juego.Bucle_Juego()