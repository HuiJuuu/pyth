"""
이 스크립트에 윈도우의 CMD 창에 이쁘게 출력하기 위한 클래스 정의.

윈도우CMD를 제어하기 위해서는 윈도우에서 제공하는 API를
파이썬
"""
import ctypes
import sys

#CMD 창의 좌표를 나티내는 구조체를 선언합니다.
class COORD(ctypes.Structure):
    # 구조체의 필드 멤버로 int형 x와 y를 선언한다.
    _fields_ = [("x", ctypes.c_short), ("y", ctypes.c_short)]

# 커서의 정보를 나타내는 구조체를 선언합니다.
class CURSORINFO(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

#화면의 원하는 위치에 텍스트를 그릴 수 있는 클래스입니다.
class Drawer:
    # Drawer 클래스의 생성자 선언
    def __init__(self):
        #윈도우  API에서는 HANDLE 이라는 구조체를 변수를 통해
        #윈도우의 시스템 어플리케이션 등을 제어할 수 있습니다.
        #여기서는 윈도우의 API 함수를 호출하여 표준 출력 스트림의 HANDLE을 가져옵니다.
        self.o_handle = ctypes.windll.kernel32.GetStdHandle(-11)

    #CMD에서 깜박이는 커서를 보여줄지 숨길지 설정하는 메서드 입니다.
    def set_cusor_visible(self, visible):
        # 커서 구조체 변수 생성.
        cursor_info = CURSORINFO()
        # 현재 표준 출력 스트림의 커서 정보를 가져옴.
        ctypes.windll.kernel32.GetConsoleCursorInfo(self.o_handle, ctypes.byref(cursor_info))
        # 가져온 커서 정보의  visible에 파라미터로 받은 visible 값을 대입함.
        cursor_info.visible = visible
        # 수정된 커서 정보를 표준 출력 스트림에 적용함.
        ctypes.windll.kernel32.SetConsoleCursorInfo(self.o_handle, ctypes.byref(cursor_info))

    #CMD의 원하는 위치에 문자열을 출력하는 방식입니다.
    def print_at(self, x, y, string):
        # 좌표 구조체를 생성합니다.
        cursor_pos = COORD(x*2, y)
        # 표준 출력 스트림의 커서 위치를 해당 좌표로 갱신합니다.
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.o_handle,cursor_pos)
        # 파라미터로 받은 문자열을 출력합니다.
        sys.stdout.write(string)
        # 출력 버퍼에 쌓인 데이터를 모두 스트림으로 보내 출력합니다.
        sys.stdout.flush()

    # 화면의 (0,0)부터 size * size 만큼의 모든 텍스트를 지우는 메서드입니다.
    def clear(self, size):
         cursor_pos = COORD(0,0)
         ctypes.windll.kernel32.SetConsoleCursorPosition(self.o_handle,cursor_pos)
         sys.stdout.write((('  ' * size) + '\n') * size)
         sys.stdout.flush()

#테스트 코드
if __name__ == '__main__':
    drawer = Drawer()
    drawer.set_cusor_visible(False)
    drawer.clear(100)
    drawer.print_at(3, 0, 'A')
    drawer.print_at(3, 5, 'B')



