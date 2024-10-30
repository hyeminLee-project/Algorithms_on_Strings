# python3
import sys

NA = -1

# 각 노드에 최대 4개의 자식을 저장 (A, C, G, T에 해당)
class Node:
    def __init__(self):
        self.next = [NA] * 4  # A, C, G, T에 대한 연결 노드 초기화
        self.is_end_of_pattern = False  # 해당 노드가 패턴의 끝인지 여부

def letter_to_index(char):
    """문자(A, C, G, T)를 0 ~ 3의 인덱스로 변환"""
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[char]

def build_trie(patterns):
    """패턴들을 트라이에 삽입"""
    root = Node()  # 루트 노드 생성
    for pattern in patterns:
        current_node = root  # 루트에서 시작
        for char in pattern:
            index = letter_to_index(char)  # 문자에 해당하는 인덱스 계산
            if current_node.next[index] == NA:
                current_node.next[index] = Node()  # 새로운 노드 생성
            current_node = current_node.next[index]  # 다음 노드로 이동
        current_node.is_end_of_pattern = True  # 패턴의 끝 표시
    return root

def search_from_position(text, start, root):
    """텍스트의 특정 위치에서 시작해 패턴을 찾는 함수"""
    current_node = root  # 루트에서 시작
    for i in range(start, len(text)):
        char = text[i]
        index = letter_to_index(char)  # 문자에 해당하는 인덱스 계산
        if current_node.next[index] == NA:
            return False  # 매칭 실패 시 종료
        current_node = current_node.next[index]  # 다음 노드로 이동
        if current_node.is_end_of_pattern:
            return True  # 패턴의 끝에 도달한 경우 매칭 성공
    return False

def solve(text, n, patterns):
    """텍스트에서 모든 패턴의 시작 위치를 찾는 함수"""
    result = []
    root = build_trie(patterns)  # 트라이 생성

    # 텍스트의 각 위치에서 패턴 매칭 시도
    for i in range(len(text)):
        if search_from_position(text, i, root):
            result.append(i)  # 매칭된 위치 저장

    return result

# 입력 처리
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = [sys.stdin.readline().strip() for _ in range(n)]

# 정답 계산 및 출력
ans = solve(text, n, patterns)
sys.stdout.write(' '.join(map(str, ans)) + '\n')
