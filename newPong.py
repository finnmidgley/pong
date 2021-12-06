import random
import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

font = pygame.font.SysFont(None,40)


sizex = 700
sizey = 500

width = 16
height = 90
                        #variable assignment 
halfwid = 8
halfhei = 45
speed = 5


p1Score = 0
p2Score = 0


ball_size = 30
ball_rad = ball_size/2
xvelo = 1
yvelo = 1

ball_pos_x = sizex/2
ball_pos_y = sizey/2




screen = pygame.display.set_mode((sizex,sizey))
pygame.display.set_caption('Pong')

x = 60
y = 10
x2 = 620
y2 = 10
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if ball_pos_x <= -30:
        pygame.time.delay(1500)
        ball_pos_x = sizex/2
        ball_pos_y = sizey/2
##        yvelo = -yvelo
##      xvelo = -xvelo                  #checks if point have been scored then increases score
        p2Score+=1

    if ball_pos_x == 700:
        pygame.time.delay(1000)
        ball_pos_x = sizex/2
        ball_pos_y = sizey/2
##        yvelo = -yvelo
##      xvelo = -xvelo
        p1Score += 1
                

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y > 0:
        y -= speed

    if keys[pygame.K_s] and y < sizey - height:
        y += speed
                                                        #paddle movement and stops out of bounds

    if keys[pygame.K_UP] and y2 > 0:
        y2 -= speed

    if keys[pygame.K_DOWN] and y2 < sizey - height:
        y2 += speed       


    ball_pos_x += xvelo
    ball_pos_y += yvelo

##    if ball_pos_x + ball_size > sizex: or #ball_pos_x < 0:
##        xvelo = - xvelo                                       #bounces ball of left or right wall

    if ball_pos_y + ball_size > sizey or ball_pos_y < 0:
        yvelo = - yvelo                                         #bounces ball of top and bottom wall


    if (ball_pos_x <= x+width) and (ball_pos_y + ball_rad > y  and ball_pos_y + ball_rad < y + height) and xvelo < 0 and ball_pos_x > x:
        xvelo = - xvelo

    if (ball_pos_x + ball_size >= x2) and (ball_pos_y + ball_rad > y2  and ball_pos_y + ball_rad < y2 + height) and xvelo > 0 and ball_pos_x < x2:
        xvelo = - xvelo



##    if (ball_pos_x - ball_size <= x+halfwid) and (ball_pos_y > y - halfhei and ball_pos_y < y + halfhei) and xvelo < 0:
##        xvelo = - xvelo        
        
        
        

    p1ScoreImg = font.render(str(p1Score),True,white) #text
    p2ScoreImg = font.render(str(p2Score),True,white)
    pygame.time.delay(4)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,white, [sizex/2-4,0,8,650])
    pygame.draw.ellipse(screen, white, [ball_pos_x, ball_pos_y, ball_size, ball_size])
    pygame.draw.rect(screen, white, (x,y,width,height), 0)
    pygame.draw.rect(screen, white, (x2,y2,width,height), 0)
    screen.blit(p1ScoreImg, (sizex/2-70,20))
    screen.blit(p2ScoreImg, (sizex/2+50,20))
    pygame.display.update()
