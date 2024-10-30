# python3
import sys

NA = -1

class Node:
    def __init__(self):
        self.next = [NA] * 4  # A, C, G, T에 대한 자식 노드 초기화
        self.patternEnd = False  # 패턴의 끝 여부 표시

def letter_to_index(char):
    """문자(A, C, G, T)를 인덱스(0~3)로 변환합니다."""
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[char]

def build_trie(patterns):
    """패턴들을 트라이에 삽입합니다."""
    root = Node()
    for pattern in patterns:
        current_node = root
        for char in pattern:
            index = letter_to_index(char)
            if current_node.next[index] == NA:
                current_node.next[index] = Node()  # 새로운 노드 생성
            current_node = current_node.next[index]
        current_node.patternEnd = True  # 패턴의 끝 표시
    return root

def search_from_position(text, start, root):
    """텍스트의 특정 위치에서 트라이를 탐색합니다."""
    current_node = root
    for i in range(start, len(text)):
        index = letter_to_index(text[i])
        if current_node.next[index] == NA:
            return False  # 매칭 실패 시 종료
        current_node = current_node.next[index]
        if current_node.patternEnd:
            return True  # 패턴의 끝에 도달하면 매칭 성공
    return False

def solve(text, n, patterns):
    """텍스트에서 모든 패턴의 시작 위치를 찾는 함수입니다."""
    result = set()  # 중복된 위치를 방지하기 위해 집합 사용
    root = build_trie(patterns)  # 트라이 생성

    # 텍스트의 각 위치에서 패턴 매칭 시도
    for i in range(len(text)):
        if search_from_position(text, i, root):
            result.add(i)  # 매칭된 위치를 결과에 추가

    return sorted(result)  # 오름차순 정렬된 리스트 반환

# 입력 처리
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = [sys.stdin.readline().strip() for _ in range(n)]

# 정답 계산 및 출력
ans = solve(text, n, patterns)
sys.stdout.write(' '.join(map(str, ans)) + '\n')
