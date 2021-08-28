"""
게임을 구성하는 게임 오브젝트들의 클래스를 정의합니다.

뱀 게임 구성 오브젝트
1. 뱀
2. 먹이
3. 벽

공통적인 특성
1. 구성요소간의 충돌감지
2. 구성요소는 좌표를 가짐
"""

# 구성요소간의 충돌감지 및 좌표, 문자를 가지는 클래스
class GameObject:
    #GameObject 생성자
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    # 충돌검사 메서드
    def collision(self, other):
        return other.x == self.x and other.y == self.y

    #화면에 그리는 메소드
    def draw(self, drawer):
        drawer.print_at(self.x, self.y, self.char)



# 벽 클래스
class Wall(GameObject):
    pass


# 먹이 클래스
class Food(GameObject):
    pass


# 뱀 클래스
class Snake(GameObject):
    D_RIGHT = (1, 0)
    D_LEFT = (-1, 0)
    D_UP = (0, -1)
    D_DOWN = (0, 1)

    # Snake의 생성자
    def __init__(self, x, y):
        super().__init__(x, y, '■')
        self.body = [GameObject(x, y + 1, '□'),
                     GameObject(x, y + 2, '□'),
                     GameObject(x, y + 3, '□')]

        self.next_d = Snake.D_UP      # 다음 방향
        self.curr_d = Snake.D_UP      # 현재 방향


    # 뱀이 먹이를 먹으면 호출하는 메소드
    def grow(self):
        self.body.append(GameObject(self.body[-1].x, self.body[-1].y, '□'))

    # 뱀이 좌표를 다음 방향으로 이동 시키는 메소드
    def move(self):
        #몸통 좌표 이동
        for i in range(len(self.body) -1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x = self.x
        self.body[0].y = self.y
        # 머리 좌표 이동
        self.x += self.next_d[0]
        self.y += self.next_d[1]

        # 현재 이동할 방향 갱신
        self.curr_d = self.next_d

    # 뱀이 다음에 이동할 방향을 지정하는 메소드
    def command(self, direction):
        # next_d를 curr_d의 반대 방향으로는 설정할 수 없음
        if self.next_d == Snake.D_RIGHT and direction == Snake.D_LEFT:
            return
        elif self.curr_d == Snake.D_LEFT and direction == Snake.D_RIGHT:
            return
        elif self.next_d == Snake.D_UP and direction == Snake.D_DOWN:
            return
        elif self.curr_d == Snake.D_DOWN and direction == Snake.D_UP:
            return
        else:
            self.next_d = direction

    #draw 메소드 오버라이딩
    def draw(self, drawer):
        #머리를 그린다
        super().draw(drawer)

        # 몸통을 그린다
        for b in self.body:
            b.draw(drawer)

if __name__ == '__main__':
    import time
    import drawing
    snake = Snake(30, 30)
    drawer = drawing.Drawer()

    while True:

        drawer.clear(100)
        snake.move()
        snake.draw(drawer)
        time.sleep(0.5)