import pygame 

import random

import time 

pygame.init()


class Apple :
    def __init__(self) :
        self.r = 8
        self.x = random.randint(30,w-30)
        self.y = random.randint(30,h-30)
        self.img=pygame.image.load('apple.png')
        self.rect=self.img.get_rect()

    def show(self) :
        screen.blit(self.img,(self.x,self.y))
        # pygame.draw.circle(screen , self.color , [self.x , self.y] , self.r ,)
        # khat bala = avali safhe dovomi rang sevomi tul arz akhari shoaa


class Bomb :
    def __init__(self) :
        self.r = 10
        self.x = random.randint(30,w-30)
        self.y = random.randint(30,h-30)
        self.img=pygame.image.load('bomb.png')
        self.rect=self.img.get_rect()

    def show(self) :
        screen.blit(self.img,(self.x,self.y))
        # pygame.draw.circle(screen , self.color , [self.x , self.y] , self.r)


class Pear :
    def __init__(self) :
        self.r = 8
        self.x = random.randint (30,w-30)
        self.y = random.randint (30,h-30)
        self.img=pygame.image.load('pear.png')
        self.rect=self.img.get_rect()

    def show(self) :
        screen.blit(self.img,(self.x,self.y))
        # pygame.draw.circle(screen , self.color , [self.x , self.y] , self.r)


class Snake :
    def __init__(self) :
        self.color = (100,0,150)
        self.color2 = (50,100,200)
        self.color3 = (50,0,200)
        self.w=self.h=20
        self.x = w//2
        self.y = h//2
        self.score = 0
        self.speed = 2
        self.x_change = 0 
        self.y_change = 0
        self.body = []

    def eat_apple(self):
        if apple.x-apple.r-2 <= self.x <= apple.x+apple.r+2 and apple.y-apple.r-2<= self.y <= apple.y+apple.r+2 :
            return True
        else :
            return False
    
    def eat_bomb(self) :
        if bomb.x-bomb.r-2 <= self.x <= bomb.x+bomb.r+2 and bomb.y-bomb.r-2 <= self.y <= bomb.y+bomb.r+2 :
            # self.body.pop(0)
            # pop andis migire
            return True
        else :
            return False
    
    def eat_pear(self) :
        if pear.x-pear.r-2 <= self.x <= pear.x+pear.r+2 and pear.y-pear.r-2 <= self.y <= pear.y+pear.r+2 :
            return True 
        else :
            return False

    def show(self) :
        pygame.draw.rect(screen , self.color , [self.x , self.y , self.w , self.h])
        # rect=mostatil
        for i,x in enumerate(self.body):
            if i%2==0 :
                pygame.draw.rect(screen , self.color2 , [x['x'] , x['y'] , self.w , self.h])
            else :
                pygame.draw.rect(screen , self.color3 , [x['x'] , x['y'] , self.w , self.h])

    def move(self) : 
        self.body.append({'x' : self.x , 'y' : self.y})
        if len(self.body) > self.score :
            self.body.remove(self.body[0])
        # if self.score < len(self.body) :
        #     self.body.remove(self.body[0])

        if self.x_change == 1 :
            self.x+=self.speed
        if self.x_change == -1 :
            self.x-=self.speed
        if self.y_change == 1 :
            self.y+=self.speed
        if self.y_change == -1 :
            self.y-=self.speed

    def lose(self) :
        if self.score < 0 :
            return True
        if self.x <= 0 or self.x >= w or self.y <= 0 or self.y >= h :
            return True 
        else :
            return False 

w=h=666
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption(' Snake Game ')
clock=pygame.time.Clock()
fps=30
apple=Apple()
snake=Snake()
bomb=Bomb()
pear=Pear()
font=pygame.font.SysFont('comicsansms' , 35)

while True :  
    if snake.lose() :
        screen.fill((0,0,0))
        if snake.lose()== True :
            img_lose=pygame.image.load('GameOver.png')
            screen.blit(img_lose,(180,200))
        pygame.display.update()
        time.sleep(2)
        exit()

    for event in pygame.event.get() :
        # balaii baraye daryaft kilid kibord 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :
                snake.y_change = 1
                snake.x_change = 0
            if event.key == pygame.K_UP :
                snake.y_change = -1
                snake.x_change = 0
            if event.key == pygame.K_RIGHT :
                snake.x_change = 1
                snake.y_change = 0
            if event.key == pygame.K_LEFT :
                snake.x_change = -1
                snake.y_change = 0

    screen.fill((100,200,100))
    # screen.blit(txt,(100,100))
    # screen.fiil = rangaye_rgb avali red dovomi sabz sevomi abi

    apple.show()
    bomb.show()
    pear.show()
    snake.move()
    snake.show()
    
    if snake.eat_apple() :
        snake.score+=1
        snake.speed+=0.25
        apple=Apple()

    if snake.eat_bomb() :
        snake.score-=1
        snake.speed-=0.5
        if len(snake.body) <= 0 :
            if snake.lose() :
                screen.fill((0,0,0))
                pygame.display.update()
                time.sleep(2)
                exit()
        else :
            snake.body.pop(0)

        bomb=Bomb()

    if snake.eat_pear() :
        snake.score+=2
        snake.speed+=0.75
        pear=Pear()


    txt=font.render('SCORE : '+ str(snake.score),True,(10,150,220))
    screen.blit(txt,(225,15))
    pygame.display.update()
    clock.tick(fps)
