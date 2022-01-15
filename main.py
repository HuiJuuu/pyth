import pygame

pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (20, 20, 20)

# 화면 크기 설정
size = (1280, 720)  # 1280 * 720
screen = pygame.display.set_mode(size)

# 게임 제목 설정
pygame.display.set_caption("Avoid the Bullets")

# 프레임을 정하기 위한 변수
clock = pygame.time.Clock()

#플레이어 위치변수
player_x = 200
player_y = 200
width = 20
height = 20
moveSpeed = 3
bullet_x = 400
bullet_y = 400
bullets = []

onGame = True
done = False

# 움직임 구현 함수 (방향키)
def move(li):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and li[0] > 0:
        li[0] -= moveSpeed

    if keys[pygame.K_RIGHT] and li[0] < 1280 - width:
        li[0] += moveSpeed

    if keys[pygame.K_UP] and li[1] > 0:
        li[1] -= moveSpeed

    if keys[pygame.K_DOWN] and li[1] < 720 - height:
        li[1] += moveSpeed

    return li[0], li[1]

# 게임 실행 루프
while not done:
    # 초당 10프레임
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT이벤트는 창에서 X버튼
            done = True
    currLocation = [player_x, player_y]
    player_x, player_y = move(currLocation)

    screen.fill(GRAY)
    player = pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 10, 10))
    bullet = pygame.draw.rect(screen, (0, 0, 255), (bullet_x, bullet_y, 5, 5))

    if player.colliderect(bullet) == True:

        done = True
    # 화면을 업데이트 해주는 함수
    pygame.display.flip()  # 없으면 화면이 그려지지 않음

pygame.quit()


# Rect = img.get_rect()
#
#for bullet in bullet:
#   if bullet.colliderect(player):
#      done = True
#     screen.blit(bullet_image, bullet[rect])
