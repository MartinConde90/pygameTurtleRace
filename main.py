import pygame, sys
import random


class Runner():
    __customes =('turtle', 'fish', 'prawn', 'moray', 'octopus')
    
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))                       
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)



class Game():
     runners = []
     __posY = (160, 200, 240, 280)
     __names = ('Speedy', 'Lucera', 'Alonso', 'Torcuata')
     __startLine = -5
     __finishLine = 620
     
     def __init__(self):
         self.__screen = pygame.display.set_mode((640, 480))
         self.__background = pygame.image.load('images/background.png')
         pygame.display.set_caption('Carrera de bichos')
         
         for i in range(4):
             theRunner = Runner(self.__startLine,self.__posY[i])
             theRunner.name = self.__names[i]
             self.runners.append(theRunner)
     
    
     
     def competir(self):# lo que hace es escuchar a ver si el jugador hace algo
         gameOver = False
         while not gameOver:
             for event in pygame.event.get(): # recorrer donde almacena los eventos
                 if event.type == pygame.QUIT: #cerrar pantalla
                    gameOver = True
             
             for activeRunner in self.runners:
                 activeRunner.avanzar()             
                 if activeRunner.position[0] >= self.__finishLine:
                     print('{} ha ganado'.format(activeRunner.name))
                     gameOver = True
         
             self.__screen.blit(self.__background, (0, 0))  #una vez proceses los eventos en la pantalla, me mueves lo que tengas(), a donde te diga
                     
            
             for runner in self.runners:# refresca la pantalla
                 self.__screen.blit(runner.custome, runner.position)
    
             pygame.display.flip() #refresca la pantalla
             
         # con esto el juego se cierra cuando hay un ganador   
         pygame.quit()
         sys.exit()
'''         
         while True: #aunque haya un ganador, no se quita hasta que lo cierres tu, sigue generando eventos
              for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()
         
'''

if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()