import pygame, sys, random
from ball import *
from thingie import *

pygame.font.init()

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width = 800
height = 500
screen = pygame.display.set_mode((width, height))

ball = Ball(400, 250, 10)
left_thing = Thing(0, 190)
right_thing = Thing(780, 190)

font1 = pygame.font.SysFont('freesanbold.ttf', 50)

def main():
     quit = False

     score_1 = 0
     score_2 = 0

     score_to_win = 5

     # Text stuff
     text1 = font1.render(str(0), True, WHITE)
     textRect1 = text1.get_rect()
     textRect1.center = (60, 60)

     text2 = font1.render(str(0), True, WHITE)
     textRect2 = text1.get_rect()
     textRect2.center = (width - 60, 60)

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
          if key_input[pygame.K_UP] and right_rect.y >0:
               right_rect.y -= 5
          if key_input[pygame.K_DOWN] and right_rect.y<height-right_rect.height:
               right_rect.y += 5
          if key_input[pygame.K_w] and left_rect.y >0:
               left_rect.y -= 5
          if key_input[pygame.K_s] and left_rect.y<height-left_rect.height:
               left_rect.y += 5

          # Clear screen, then draw stuff
          screen.fill(BLACK)
          pygame.draw.circle(screen, WHITE, (ball.x, ball.y), ball.radius)
          pygame.draw.rect(screen, WHITE, left_rect)
          pygame.draw.rect(screen, WHITE, right_rect)


     
          ball.x += ball.vel_x
          ball.y += ball.vel_y
          
          if check_collision_x(ball, left_rect, right_rect, width):
               ball.vel_x *=-1-random.random()/5
               ball.vel_y *= 1+random.random()/5
          
          if check_collision_y(ball, height):
               ball.vel_y *=-1
          
          if check_point(ball, width) == 1:
               #player1
               ball.x = 400
               ball.y= 250
               score_1 += 1
               text2 = font1.render(str(score_1), True, WHITE)
               ball.vel_x = 4
               ball.vel_y = 1

          if check_point(ball, width) == 2:
               #player2
               ball.x = 400
               ball.y= 250
               score_2 += 1
               text1 = font1.render(str(score_2), True, WHITE)
               ball.vel_x = 4
               ball.vel_y = 1

          screen.blit(text1, textRect1)
          screen.blit(text2, textRect2)

          if score_1 == score_to_win or score_2 == score_to_win:
               if score_1 == score_to_win:
                    winner = 1
               else:
                    winner=2
          
               text3 = font1.render(f"Player {winner} heeft gewonnen" , True, WHITE)
               textRect3 = text3.get_rect()
               textRect3.center = (width/2, height/2)
               ball.x = -ball.radius
               restart = False

               while not restart:
                    pygame.display.flip()
                    for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                              pygame.quit()
                              sys.exit()
                         if event.type == pygame.MOUSEBUTTONDOWN:
                              restart = True

                    screen.blit(text3, textRect3)

               ball.x = 400
               ball.y = 250
               score_1 = 0
               score_2 = 0
               text1 = font1.render(str(score_2), True, WHITE)
               text2 = font1.render(str(score_1), True, WHITE)

     return

def check_collision_x(ball, left, right, width):
     # Check collision left
     if ball.x < left.width and ball.y > left.y and ball.y < left.y + left.height:
          return True
     # Check collision right
     if ball.x > width-right.width and ball.y > right.y and ball.y < right.y + right.height:
          return True
     return False

def check_collision_y(ball, height):
     # Check collision top
     if ball.y < ball.radius:
          return True
     # Check collision bottom
     if ball.y > height - ball.radius:
          return True
     return False

def check_point(ball, width):
     # Check right 
     if ball.x > width - ball.radius:
          return 2
     # Check left
     if ball.x <0 + ball.radius:
          return 1
     return 0


if __name__ == "__main__":
     main()