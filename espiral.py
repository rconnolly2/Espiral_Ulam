import pygame

class Espiral:
    def __init__(self, texto_ventana: str, color_fondo: tuple):
        # Inicializar Pygame
        pygame.init()
        # Establecer el tamaño de la ventana
        self.tamaño_ventana = (500, 500)
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
        self.tamaño_bloque = self.tamaño_ventana[0]/5


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
        #Empezamos posicion en el centro de pantalla que es la la mitad de ancho y alto:
        pos_actual = [self.tamaño_ventana[0]/2, self.tamaño_ventana[1]/2]


        def Direccion(pos_actual, direccion):
        #Funciones derecha-arriba-izquierda-abajo == 0, 1, 2, 3 => direccion
            if direccion == 0:
                #Cogemos posicion actual y le sumamos a x  tamaño de bloque
                pos_actual[0] = pos_actual[0] + (self.tamaño_bloque)
                print("derecha")
            if direccion == 1:
                #Cogemos posicion actual y le restamos a y tamaño de bloque
                pos_actual[1] = pos_actual[1] - (self.tamaño_bloque)
                print("up")
            if direccion == 2:
                #Cogemos posicion actual y le restamos a x tamaño de bloque
                pos_actual[0] = pos_actual[0] - (self.tamaño_bloque)
                print("izquierda")

            if direccion == 3:
                #Cogemos posicion actual y le sumamos a y tamaño de bloque
                pos_actual[1] = pos_actual[1] + (self.tamaño_bloque)
                print("abajo")
        
        la_direccion = 0 #Empezamos con direccion derecha
        iterador_pasos = 0 #Esto es un simple iterador para saber en que paso esta y tiene que tiene como maximo
        # => Cantidad de pasos
        #Primer punto central:
        text_surface = self.fuente.render(str(self.numero_imprimir), True, (255, 255, 255))
        self.pantalla.blit(text_surface, pos_actual)
        pygame.display.flip()
        #Añadimos 1 al numero a imprimir en pantalla:
        self.numero_imprimir = self.numero_imprimir + 1
        for i in range(8):
                if cantidad_pasos == 1:
                    for p in range(2):
                        Direccion(pos_actual, la_direccion)
                        text_surface = self.fuente.render(str(self.numero_imprimir), True, (255, 255, 255))
                        self.pantalla.blit(text_surface, pos_actual)
                        pygame.display.flip()
                    
                        #Cambiamos de direccion:
                        la_direccion = la_direccion+1
                        #+1 numero
                        self.numero_imprimir = self.numero_imprimir + 1
                    cantidad_pasos = cantidad_pasos+1
                    self.numero_imprimir = 4
                else:

                    for pasos in range(cantidad_pasos):
                        print("Paso:  " + str(pasos))
                        Direccion(pos_actual, la_direccion)
                        text_surface = self.fuente.render(str(self.numero_imprimir), True, (255, 255, 255))
                        self.pantalla.blit(text_surface, pos_actual)
                        self.numero_imprimir = self.numero_imprimir + 1
                        pygame.display.flip()
                
                    iterador_pasos = iterador_pasos + 1
                    #Camabiamos de direccion:
                    la_direccion = la_direccion+1
                    #Cuando cantidad de pasos sea = 2
                    #añadimos un paso mas y reiniciamos el iterador
                    if iterador_pasos == 2:
                        cantidad_pasos = cantidad_pasos+1
                        iterador_pasos = 0

                    if la_direccion == 4: # Si la direccion es 4 que no existe reseteamos a derecha => 0
                        la_direccion = 0

                






juego = Espiral("Espiral Ulam", (255, 0, 0))
juego.Crear_Espiral()
juego.Bucle_Juego()