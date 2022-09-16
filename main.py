import pygame, sys
pygame.init()

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 500))

def main():
     quit = False

     # game loop
     while not quit:

          for event in pygame.event.get():
               if event.type == pygame.QUIT: sys.exit()
               
     return

if __name__ == "__main__":
     main()