import pygame, sys
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/snow1.png")
        self.position = (x, y)
        self.name = 'Tortuga'
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)



class Game():
     runners = []
     __startLine = 5
     __finishLine = 620
     
     def __init__(self):
         self.__screen = pygame.display.set_mode((640, 480))
         self.__background = pygame.image.load('images/background.png')
         pygame.display.set_caption('Carrera de bichos')
         
         firstRunner = Runner(self.__startLine,240)
         firstRunner.name = 'Speedy'
         self.runners.append(firstRunner)
             
     def competir(self):
         gameOver = False
         while not gameOver:
             for event in pygame.event.get(): # recorrer donde almacena los eventos
                 if event.type == pygame.QUIT: #cerrar pantalla
                    gameOver = True
         
             self.__screen.blit(self.__background, (0, 0))  #una vez proceses los eventos en la pantalla, me mueves lo que tengas(), a donde te diga
             self.__screen.blit(self.runners[0].custome, self.runners[0].position)
    
             pygame.display.flip() #refresca la pantalla
             
         pygame.quit()
         sys.exit()
         
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()