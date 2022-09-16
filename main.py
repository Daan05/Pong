import pygame, sys
from ball import *
from thingie import *

pygame.init()

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

ball = Ball(400, 250, 10)
left_thing = Thing(0, 190)
right_thing = Thing(780, 190)

def main():
     quit = False

     clock = pygame.time.Clock()

     left_rect = pygame.Rect(left_thing.x, left_thing.y, left_thing.width, left_thing.height)
     right_rect = pygame.Rect(right_thing.x, right_thing.y, right_thing.width, right_thing.height)

     # game loop
     while not quit:

          # Set FPS to 60
          clock.tick(FPS)

          # Update screen each frame
          pygame.display.update()

          # Check for events
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

          key_input = pygame.key.get_pressed()
          if key_input[pygame.K_UP]:
               right_rect.y -= 5
          if key_input[pygame.K_DOWN]:
               right_rect.y += 5
          if key_input[pygame.K_w]:
               left_rect.y -= 5
          if key_input[pygame.K_s]:
               left_rect.y += 5

          # Clear screen, then draw stuff
          screen.fill(BLACK)
          pygame.draw.circle(screen, WHITE, (ball.x, ball.y), ball.radius)
          pygame.draw.rect(screen, WHITE, left_rect)
          pygame.draw.rect(screen, WHITE, right_rect)
     
          ball.x += ball.vel_x
          ball.y += ball.vel_y
          #if ball.x > width-ball.radius:
               #ball.vel_x *= -1
          #if ball.x <0+ball.radius:
               #ball.vel_x *= -1

          #if ball.y > height-ball.radius:
               #ball.vel_y *=-1
          #if ball.y <0+ball.radius:
               #ball.vel_y *=-1
          
          if check_collision_x(ball, left_rect, right_rect, width):
               ball.vel_x *=-1
          
          if check_collision_y(ball, height):
               ball.vel_y *=-1
          
          if check_point(ball, width) == 1:
               #player1
               print("point  1")

          if check_point(ball, width) == 2:
               #player2
               print("point  2")
          



     return

def check_collision_x(ball, left, right, width):
     #check collision left side
     if ball.x < left.width and ball.y > left.y and ball.y < left.y+left.height:
          return True
     if ball.x > width-right.width and ball.y > right.y and ball.y < right.y+right.height:
          return True
     return False

def check_collision_y(ball, height):
     #check collision left side
     if ball.y < ball.radius:
          return True
     if ball.y > height-ball.radius:
          return True
     return False

def check_point(ball, width):    
     if ball.x > width-ball.radius:
          return 1
     if ball.x <0+ball.radius:
          return 2
     return 0


if __name__ == "__main__":
     main()