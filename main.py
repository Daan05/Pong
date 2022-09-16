import pygame, sys
from ball import *
from thingie import *

pygame.init()

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800, 500))

ball = Ball(400, 250, 10)
left_thing = Thing(0, 190)
right_thing = Thing(780, 190)

def main():
     quit = False

     left_rect = pygame.Rect(left_thing.x, left_thing.y, left_thing.width, left_thing.height)
     right_rect = pygame.Rect(right_thing.x, right_thing.y, right_thing.width, right_thing.height)

     # game loop
     while not quit:

          # Update screen each frame
          pygame.display.update()

          # Check for events
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                         right_rect.y -= 5
                    if event.key == pygame.K_DOWN:
                         right_rect.y += 5
                    if event.key == pygame.K_w:
                         left_rect.y -= 5
                    if event.key == pygame.K_s:
                         left_rect.y += 5

          # Clear screen, then draw stuff
          screen.fill(BLACK)
          pygame.draw.circle(screen, WHITE, (ball.x, ball.y), ball.radius)
          pygame.draw.rect(screen, WHITE, left_rect)
          pygame.draw.rect(screen, WHITE, right_rect)

     return

if __name__ == "__main__":
     main()