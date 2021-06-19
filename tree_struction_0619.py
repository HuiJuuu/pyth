class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

A = Node('A')
B = Node('B')
C = Node('C')

A.left = B
A.right = C

#이진탐색트리 클래스
class Binarysearchtree:
    def __init__(self):
        self.root = None

    #삽입 메소드 : key값을 트리에 삽입
    def insert(self, key):
        #1. 루트에서부터 key 값을 비교해보면서 부모가 될 노드를 찾는다.
        #2. 부모의 자식으로 key 값을 가지는 새로운 노드를 연결한다.

        #루트 노드가 없는 경우
        if self.root is None:
            self.root = Node(key)
            return
        p_node = None
        c_node = self.root

        #자식이 None이 될 때까지 탐색
        while c_node is not None:
            p_node = c_node
            if c_node.key > key:
                c_node = c_node.left
            else:
                c_node = c_node.right

        #부모의 왼쪽 자식이 될지 오른쪽 자식이 될지 결정
        if p_node.key>key:
            p_node.left = Node(key)
        else:
            p_node.right = Node(key)


    #탐색 메소드 : 트리에서 key 값을 검색 (일치하는 값이 있으면 True, 아니면 False)
    def search(self, key):
        c_node = self.root

        while c_node is not None:
            if c_node.key >key:
                c_node = c_node.left
            elif c_node.key < key:
                c_node = c_node.right
            else:
                return True
        return False


    #삭제 메소드 : 트리에서 key 값을 삭제
    def remove(self,key):
        p_node = None
        c_node = self.root

        #삭제할 키값을 갖는 노드를 찾는다.
        while(c_node is not None) and (key != c_node.key):
            p_node = c_node
            if c_node.key > key:
                c_node = c_node.left
            else:
                c_node = c_node.right

        #찾았는데 노드가 None인 경우 -> 해당 key 값이 없다는 뜻임
        if c_node is None:
            return
        # 1. 삭제할 노드가 단말 노드인 경우
        elif (c_node.left is None) and (c_node.right is None):
            if p_node is None:  #삭제라여는 노드가 루트 노드다.
                self.root = None
            else:   #삭제하려는 노드가 루트가 아닌 단말 노드다.
                if p_node.left == c_node:
                    p_node.left = None
                else:
                    p_node.right = None
        # 2. 삭제할 노드가 하나의 서브트리를 갖는 경우.
        elif (c_node.left is not None) or (c_node.right is not None):
            #삭제하려는 노드의 자식 노드를 찾는다.
            cc_node = None
            if c_node.left is not None:
                cc_node = c_node.left
            else:
                cc_node = c_node.right

            if p_node is None:  #삭제하려는 노드가 루트 노드인 경우
                self.root = cc_node
            else:
                if p_node.left == c_node:
                    p_node.left = cc_node
                else:
                    p_node.right = cc_node
        #3. 삭제할 노드가 두개의 서브트리를 갖는 경우
        else:
            # 3-1. 오른쪽 서브 트리에서 후속자를 찾는다.
            # 3-2. 오른쪽 서브 트리의 후속자는 제일 왼쪽 자식이다.

            sp_node = c_node        #후속자 노드의 부모노드
            s_node = c_node.right   #후속자 노드

            while s_node.left is not None:
                sp_node = s_node
                s_node = s_node.left

            # 3-3. 후속자의 부모와 오른쪽 자식을 연결한다. (후속자와 부모의 연결은 끊어짐.)

            if sp_node.left == s_node:
                sp_node.left = s_node.right
            else:
                sp_node.right = s_node.right

            # 3-4. 후속자의 키값을 삭제할 노드의 키값에 복사한다.

            c_node.key = s_node.key




bst = Binarysearchtree()
bst.insert(6)
bst.insert(4)
bst.insert(12)
bst.insert(5)

print(bst.search(6))    #True
print(bst.search(4))    #True
print(bst.search(12))   #True
print(bst.search(5))    #True
print(bst.search(1))    #False