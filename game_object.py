
from drawing import Drawer, get_color_text

#테트리스의 한칸 블록입니다.
class Block:
    def __init__(self, coordinate, pivot, text):
        self.coord = coordinate     # 블록의 좌표
        self.pivot = pivot          # 블록의 회전 중심점
        self.text = text            # 블록의 모양(색 포함)

    # 블록을 회전 중심점(pivot)을 기준으로 시계방향(clockwise)으로 회전한다.
    # (X1, Y1) -> 시계방향 회전 -> (-Y1, X1)
    def turn_cw(self):
        #원점으로 좌표계를 이동시킨다.
        origin_x = self.coord[0] - self.pivot[0]
        origin_y = self.coord[1] - self.pivot[1]

        #원점 기준으로 시계방향 90도 회전
        turn_x = -origin_y
        turn_y = origin_x

        final_x = turn_x + self.pivot[0]
        final_y = turn_y + self.pivot[1]

        self.coord = [final_x, final_y]


    #블록을 회전 중심점(pivot)을 기준으로 반시계방향(count-clockwise)으로 회전한다.
    # (X1, Y1) -> 반시계방향 회전 -> (Y1, -X1)
    def turn_ccw(self):
        # 원점으로 좌표계를 이동시킨다.
        origin_x = self.coord[0] - self.pivot[0]
        origin_y = self.coord[1] - self.pivot[1]

        # 원점 기준으로 반시계방향 90도 회전
        turn_x = origin_y
        turn_y = -origin_x

        final_x = turn_x + self.pivot[0]
        final_y = turn_y + self.pivot[1]

        self.coord = [final_x, final_y]
        pass

    #블록을 지정된 위치에 그린다.
    def draw(self, drawer):
        drawer.print_at(self.coord[0], int(self.coord[1]), self.text)


#테트리스의 여러 개의 블록 세트를 나타냅니다.
class BlockSet:
    def __init__(self, coord_list, pivot, text):
        self.pivot = pivot  # 회전의 중심점(블록 세트의 위치)
        self.text = text    # 블록들의 모양
        self.blocks = []    # 블록 인스턴스들

        #입력받은 상대 좌표의 리스트로부터 블록 인스턴스 생성
        for coord in coord_list:
            self.blocks.append(
                Block(
                    [coord[0] + self.pivot[0], coord[1] + self.pivot[1]],
                    self.pivot,
                    self.text
                )
            )

    # 모든 블록을 그립니다.
    def draw(self, drawer):
        for block in self.blocks:
            block.draw(drawer)

    # 모든 블록을 시계방향 회전합니다.
    def turn_cw(self):
        for block in self.blocks:
            block.turn_cw()

    # 모든 블록을 반시계방향 회전합니다.
    def turn_ccw(self):
        for block in self.blocks:
            block.turn_ccw()

    # 모든 블록들을 offset 만큼 이동시키는 기능입니다. (상대좌표)
    def move_offset(self, offset):
        self.pivot[0] += offset[0]
        self.pivot[1] += offset[1]
        for block in self.blocks:
            block.coord[0] += offset[0]
            block.coord[1] += offset[1]
            block.pivot =self.pivot

    # 모든 블록들의 회전 중심점을 변경하는 기능입니다.
    # 지정된 좌표로 모든 블록들을 이동합니다. (절대좌표)
    def set_pivot(self, pivot):
        self.pivot = pivot
        for block in self.blocks:
            block.coord[0] = block.coord[0] + pivot[0]
            block.coord[1] = block.coord[1] - block.pivot[1] + pivot[1]

class TBlock(BlockSet):
    def __init__(self, pivot):
        super().__init__(
            [
                [-1, 0], [0, 0], [1, 0],
                         [0, 1]
            ],
            pivot,
            get_color_text('violet', '■')
        )

class JBlock(BlockSet):
    def __init__(self, pivot):
        super().__init__(
            [
                [-1, -1],
                [-1, 0], [0, 0], [1, 0]
            ],
            pivot,
            get_color_text('blue', '■')
        )

class LBlock(BlockSet):
    def __init__(self, pivot):
        super().__init__(
            [
                                 [1, -1],
                [-1, 0], [0, 0], [1, 0]
            ],
            pivot,
            get_color_text('orange', '■')
        )

class SBlock(BlockSet):
    def __init__(self, pivot):
        super().__init__(
            [
                          [0, 0], [1, 0],
                 [-1, 1], [0, 1]
            ],
            pivot,
            get_color_text('green', '■')
        )

class ZBlock(BlockSet):
    def __init__(self, pivot):
        super().__init__(
            [
                [-1, 0], [0, 0],
                         [0, 1], [1, 1]
            ],
            pivot,
            get_color_text('red', '■')
        )

class OBlock(BlockSet):
    def __init__(self, pivot):
        super().__init__(
            [
                [0, 0], [1, 0],
                [0, 1], [1, 1]

            ],
            pivot,
            get_color_text('yellow', '■')
        )

    def turn_cw(self):
        pass

    def turn_ccw(self):
        pass

class IBlock(BlockSet):
    def __init__(self, pivot):
        self.turn_state = 0
        self.turn_base = [
            [[-2, 0], [-1, 0], [0, 0], [1, 0]],
            [[0, 1], [0, 0], [0, -1], [0, -2]],
            [[-2, 1], [-1, 1], [0, 1], [1, 1]],
            [[-1, 1],[-1,0], [-1,-1], [-1,-2]]
        ]
        super().__init__(
            [
                [-2, 0], [-1, 0], [0, 0], [1, 0]
            ],
            pivot,
            get_color_text('cyan', '■')
        )

    def turn_cw(self):
        self.turn_state = (self.turn_state + 1) % 4
        for block, base in zip(self.blocks, self.turn_base[self.turn_state]):
            block.coord[0] = block.pivot[0] + base[0]
            block.coord[1] = block.pivot[1] + base[1]

    def turn_ccw(self):
        self.turn_state = 3 if self.turn_state -1 < 0 else self.turn_state -1
        for block, base in zip(self.blocks, self.turn_base[self.turn_state]):
            block.coord[0] = block.pivot[0] + base[0]
            block.coord[1] = block.pivot[1] + base[1]

if __name__ == '__main__':
    from time import sleep

    d = Drawer(50, 20)
    blocks = [
        OBlock([5, 5]),
        IBlock([10, 5]),
        JBlock([15, 5]),
        LBlock([20, 5]),
        TBlock([25, 5]),
        SBlock([30, 5]),
        ZBlock([35, 5])
    ]
    while True:
        d.clear()
        for block in blocks:
            block.draw(d)
            block.turn_ccw()

        d.flush()
        sleep(1)


