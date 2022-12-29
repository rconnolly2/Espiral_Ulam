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
        # Cambiar color fondo aceptanndo solo una tupla RGB ej: (255, 255, 255)
        try:
            self.pantalla.fill(color_fondo)
        except:
            print("Error: solo acepta tupla con este formato rgb: (255, 255, 255")

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


juego = Espiral("Espiral Ulam", (255, 0, 0))
juego.Bucle_Juego()