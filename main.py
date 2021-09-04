#파일 -> CMD -> .\venv\Scripts\python.exe main.py

from drawing import Drawer
from game_object import Snake, Food, Wall
import keyboard     # 모듈 설치를 위해 Alt + Enter 를 누르고 설치를 누름
import time
import random
import os

#CMD의 모든 텍스트를 지운다.
os.system('cls')

#화면을 다루기 위해 DRAWER 클래스의 인스턴스 생성
drawer = Drawer()

#화면의 커서를 지운다.
drawer.set_cusor_visible(False)

class GameManager:
    # GameManager 의 생성자
    #size는 30이 들어오면 30X30을 의미
    def __init__(self, size):
        self.size = size

        # 입력받은 size만큼 wall 오브젝트를 생성합니다.
        self.walls = []
        for x in range (size):
            for y in range(size):
                if 1 <= x <= size-2 and 1 <= y <= size-2:
                    continue
                self.walls.append(Wall(x, y,'■'))

        # 뱀을 성성하고 맵의 중앙에 배치합니다.
        self.snake = Snake(size//2, size//2)

        #
        self.food = self.summon_food()

        #
        self.is_run = False

    # 오브젝트가 없는 렌덤힌 위피에 음서을 생성하는 메서드
    def summon_food(self):
        new_food = None
        while True:
            # 1. 랜덤값을 생성 (x, y)범위는 테두리를 제외한 내부 사각형
            x = random.randint(1, self.size-2)
            y = random.randint(1, self.size-2)
            # 2. 랜덤 좌표로 음식을 생성
            new_food = Food(x, y, '●')

            collide = False
            # 3. 생성된 음식이 현재 있는 오브젝트 들과 충돌하는지 검사 (GameObject는 collision 메소드를 가지고 있음)
            # 3-1. 음식이 뱀 머리와 부딪히는지 검사 -> collide = True
            collide = new_food.collision(self.snake)
            # 3-2. 음식이 뱀 몸과 부딪히는지 검사 -> collide =  True
            for b in self.snake.body:
                collide = self.snake.collision(b)
                if collide:
                    break

            # 4. 충돌하면 다시 1로 돌아가서 반복, 충돌 안 하면 메서드 종료
            if collide is not True:
                break
        return new_food

    # 모든 오브젝트를 화면에 그리는 메서드
    def draw_all(self):
        drawer.clear(self.size)     # 맵의 모든 영역을 공백으로 지운다.
        self.snake.draw(drawer)     # 벰을 그린다.
        self.food.draw(drawer)      # 음식을 그린다.
        for w in self.walls:        # 모든 벽을 그린다.
            w.draw(drawer)

    # 게임의 상황을 검사하는 메서드
    def check(self):
        # 0. 뱀을 움직인다.
        self.snake.move()

        # 1. 뱀의 머리가 뱍에 부딪혔는가?
        for w in self.walls:
            if w.collision(self.snake):
                self.is_run = False

        # 2. 뱀의 머리가 뱀의 몸에 부딪혔는가?
        for b in self.snake.body:
            if b.collision(self.snake):
                self.is_run = False

        # 3. 뱀의 머리가 음식에 부딪혔는가?
        if self.snake.collision(self.food):
            self.food = self.summon_food()
            self.snake.grow()

    #키보드 입력을 처리하는 메서드
    def control(self):
        if keyboard.is_pressed('right'):
            self.snake.command(Snake.D_RIGHT)
        if keyboard.is_pressed('left'):
            self.snake.command(Snake.D_LEFT)
        if keyboard.is_pressed('up'):
            self.snake.command(Snake.D_UP)
        if keyboard.is_pressed('down'):
            self.snake.command(Snake.D_DOWN)

    #게임을 진행하는 메서드 입니다.
    def run(self):
        p_clock = 0     # 이전 시간
        c_clock = 0     # 현재 시간
        interval = 0    # 누적 시간

        self.is_run = True

        while self.is_run:
            p_clock = c_clock               # 반복문이 한 바퀴 돌기 전에 시간 저장
            c_clock = time.time()           # 반복문이 한 바퀴 돈 후 시간 저장
            interval += c_clock - p_clock   # 반복문이 한 바퀴 도는 동안 지난 시간 누적

            # 누적된 시간이 0.25초 이상이 되면 게임을 한 프레임 진행시킵니다.
            if interval >= 0.25:
                interval = 0
                self.draw_all()
                self.check()

            # 키보드 입력은 항상 확인해야 합니다.
            self.control()


g = GameManager(21)
g.run()


