import pygame
import random
import time

pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
GRAY = (20, 20, 20)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 화면 크기 설정
size = (1280, 720)  # 1280 * 720
screen = pygame.display.set_mode(size)

# 게임 제목 설정
pygame.display.set_caption("Avoid the Bullets")

# 프레임을 정하기 위한 변수
clock = pygame.time.Clock()

player_x = 640
player_y = 360
width = 20
height = 20
count = 0

moveSpeed = 10
#back_sound = pygame.mixer.Sound("MP_Hennessy Drum.mp3")
#back_sound.play(-1)

onGame = True
done = False
Ready = True

# 움직임 구현 함수 (방향키)
def move(li):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and li[0] > 0:
        li[0] -= moveSpeed

    if keys[pygame.K_RIGHT] and li[0] < 1280 - height :
        li[0] += moveSpeed

    if keys[pygame.K_UP] and li[1] > 0:
        li[1] -= moveSpeed

    if keys[pygame.K_DOWN] and li[1] < 720 - width:
        li[1] += moveSpeed
    return li[0], li[1]  # li[0]은 x좌표, li[1]은 y좌표


class Bullits:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.x_speed = random.uniform(1, 5)
        self.y_speed = random.uniform(1, 5)
        #self.x_speed += 0.5
        #self.y_speed += 0.5

        clock.tick(60)
        start_ticks = pygame.time.get_ticks()

        self.second = start_ticks // 1000
        self.second_list = [1, 5, 10, 15, 20, 25, 30]

        for s in self.second_list:
            if s == self.second:
                self.x_speed += 0.5
                self.y_speed += 0.5




    def draw(self):
        self.rect = pygame.draw.rect(screen, GREEN, (self.pos_x, self.pos_y, width, height))

    def move(self):
        self.pos_x += self.x_speed
        self.pos_y += self.y_speed

    def wall_check(self):
        if self.pos_x + self.x_speed > 1280 - width or self.pos_x + self.x_speed < height:
            self.x_speed = -self.x_speed
        if self.pos_y + self.y_speed > 720 - width or self.pos_y + self.y_speed < height:
            self.y_speed = -self.y_speed

    def collision_check(self):
        if self.rect.top < player.bottom and player.top < self.rect.bottom and player.left < self.rect.right and self.rect.left < player.right:
            return True
        else:
            return False

    def check_all(self):
        self.draw()
        self.move()
        self.wall_check()
        res = self.collision_check()
        if res == True:
            return True
        else:
            return False


enemy_1 = Bullits(random.randrange(10, 1270), random.randrange(10, 710))
enemy_2 = Bullits(random.randrange(10, 1270), random.randrange(10, 710))
enemy_3 = Bullits(random.randrange(10, 1270), random.randrange(10, 710))
enemy_4 = Bullits(random.randrange(10, 1270), random.randrange(10, 710))
enemy_5 = Bullits(random.randrange(10, 1270), random.randrange(10, 710))
enemy_6 = Bullits(random.randrange(10, 1270), random.randrange(10, 710))

start_level = 1

# 게임 실행 루프
while not done:
    # 초당 10프레임
    clock.tick(60)
    start_ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    currLocation = [player_x, player_y]
    player_x, player_y = move(currLocation)

    screen.fill(GRAY)

    player = pygame.draw.rect(screen, RED, (player_x, player_y, width, height))

    temp1 = enemy_1.check_all()
    temp2 = enemy_2.check_all()
    temp3 = enemy_3.check_all()
    temp4 = enemy_4.check_all()
    temp5 = enemy_5.check_all()
    temp6 = enemy_6.check_all()

    if temp1==True or temp2==True or temp3==True or temp4==True or temp5==True or temp6==True or \
            player_x == 0 or player_x == 1280 or player_y == 0 or player_y == 720:
        screen.fill(BLACK)
        myFont = pygame.font.SysFont("arial", 60, True, False)
        text_Title = myFont.render("GAME OVER", True, WHITE)
        text_Rect = text_Title.get_rect()
        text_Rect.centerx = round(1260 / 2)
        text_Rect.y = 300
        screen.blit(text_Title, text_Rect)

        done = True

    time_text = str(start_ticks // 1000)
    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Title = myFont.render("Time : " + time_text, True, WHITE)
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = round(1100)
    text_Rect.y = 10
    screen.blit(text_Title, text_Rect)


    score = start_ticks // 1000
    score_list = [5, 10, 15]
    level = str(start_level)


    for s in score_list:
        if s == score:
            start_level += 1
            level = str(start_level)

    myFont = pygame.font.SysFont("arial", 30, True, False)
    text_Tittle_2 = myFont.render("Score : " + level, True, WHITE)
    text_Rect = text_Title.get_rect()
    text_Rect.centerx = round(1100)
    text_Rect.y = 40
    screen.blit(text_Tittle_2, text_Rect)

    if done:
        pygame.display.flip()
        pygame.time.delay(2 * 1000)  # 1 second == 1000 milliseconds

    pygame.display.flip()

pygame.quit()

# import os
# os.system("pause")