import pygame
from random import randint

# 기본 변수 정의
player_x = 200
player_y = 200
width = 20
height = 20
time_ = 0
moveSpeed = 5
score = 0
objects = []
onGame = True
done = False

# 화면 크기 설정
size = (1280, 720)  # 1280 * 720
screen = pygame.display.set_mode(size)

# 버블 이미지
bubbleImg = pygame.image.load("images/bubble.PNG").convert()
bubbleImg = pygame.transform.scale(bubbleImg, (30, 30))

# 플레이어
playerImg = pygame.image.load("images/niddle.PNG").convert()
playerImg = pygame.transform.scale(playerImg, (30, 30))
player = screen.blit(playerImg, (player_x, player_y))


# 메인 클래스
class Bullits:
    # 초기값 세팅
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        if diff(score)[1] == "Easy":
            speed = randint(-1, 1)
        elif diff(score)[1] == "Normal":
            speed = randint(-3, 3)
        elif diff(score)[1] == "Hard":
            speed = randint(-5, 5)
        if speed == 0:
            speed = 1
        self.x_speed = speed
        self.y_speed = speed
        self.crashed = 0

    # 객체(버블) 그리기
    def draw(self):
        self.bubble = screen.blit(bubbleImg, (self.pos_x, self.pos_y))

    # 속도만큼 객체 움직이기
    def move(self):
        self.pos_x += self.x_speed
        self.pos_y += self.y_speed

    # 객체가 벽과 부딛쳤는지 확인
    def wall_check(self):
        if self.pos_x + self.x_speed > 1280 - width or self.pos_x + self.x_speed < 0:
            self.x_speed = -self.x_speed
            self.crashed += 1
        if self.pos_y + self.y_speed > 720 - width or self.pos_y + self.y_speed < 0:
            self.y_speed = -self.y_speed
            self.crashed += 1

    # 객체가 플레이어와 부딛쳤는지 확인
    def collision_check(self):
        if self.bubble.top < player.bottom and player.top < self.bubble.bottom and player.left < self.bubble.right and self.bubble.left < player.right:
            return True
        else:
            return False

    # 객채의 상태 체그
    def check_all(self):
        self.draw()
        self.move()
        self.wall_check()

        # 플레이어와 부딛쳤다면.
        if self.collision_check():
            while True:
                pass
        # Easy 난이도라면 4번 튕기면 삭제
        if diff(score)[1] == "Easy":
            if self.crashed >= 4:
                return True
            elif self.crashed < 4:
                return False

        # Normal 난이도라면 5번 튕기면 삭제
        if diff(score)[1] == "Normal":
            if self.crashed >= 5:
                return True
            elif self.crashed < 5:
                return False

        # Hard 난이도라면 3번 튕기면 삭제
        if diff(score)[1] == "Hard":
            if self.crashed >= 3:
                return True
            elif self.crashed < 3:
                return False

# 난이도 리턴 함수
# diff(score) 시 (숫자, "Difficuly") 을 리턴
difficulty = {"easy": 100, "normal" : 50, "hard" : 20}
def diff(score):
    if score < 20:
        return difficulty["easy"], "Easy"
    elif 20 <= score < 50:
        return difficulty["normal"], "Normal"
    else:
        return difficulty["hard"], "Hard"

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

# 플레이어 함수
def print_player(x, y):
    global player
    currLocation = [x, y]
    player_x, player_y = move(currLocation)
    player = screen.blit(playerImg, (player_x, player_y))
    return player_x, player_y