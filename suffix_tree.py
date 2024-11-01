#python 3
# import sys

# def build_suffix_array(text):
#     suffixes = sorted((text[i:], i) for i in range(len(text)))
#     return [s[1] for s in suffixes]

# def build_lcp(text, suffix_array):
#     n = len(text)
#     rank = [0] * n
#     lcp = [0] * (n - 1)
    
#     for i, suffix in enumerate(suffix_array):
#         rank[suffix] = i
    
#     h = 0
#     for i in range(n):
#         if rank[i] > 0:
#             j = suffix_array[rank[i] - 1]
#             while i + h < n and j + h < n and text[i + h] == text[j + h]:
#                 h += 1
#             lcp[rank[i] - 1] = h
#             if h > 0:
#                 h -= 1
#     return lcp

# def build_suffix_tree(text):
#     suffix_array = build_suffix_array(text)
#     lcp = build_lcp(text, suffix_array)
#     result = []

#     stack = []
#     for i in range(len(suffix_array)):
#         suffix_start = suffix_array[i]
#         current_suffix = text[suffix_start:]
        
#         while stack and stack[-1][1] >= (lcp[i - 1] if i > 0 else 0):
#             last_suffix, length = stack.pop()
#             if length > 0:
#                 result.append(text[last_suffix:last_suffix + length])
        
#         if stack:
#             result.append(text[suffix_start:suffix_start + (lcp[i - 1] if i > 0 else len(current_suffix))])
        
#         stack.append((suffix_start, len(current_suffix)))
    
#     while stack:
#         suffix_start, length = stack.pop()
#         if length > 0:
#             result.append(text[suffix_start:suffix_start + length])
    
#     return result

# if __name__ == '__main__':
#     text = sys.stdin.readline().strip()
#     result = build_suffix_tree(text)
#     print("\n".join(result))

import sys
import threading

# 재귀 한도 및 스택 크기 설정
sys.setrecursionlimit(10**7)  # 재귀 깊이 한도 증가
threading.stack_size(2**27)   # 스택 크기를 128MB로 설정

class Node:
    def __init__(self, start=-1, length=0):
        self.children = {}
        self.start = start
        self.length = length

def build_suffix_tree(text):
    """
    문자열 text의 접미사 트리를 생성하고 트리의 간선 레이블을 모두 반환합니다.
    """
    root = Node()
    n = len(text)

    # 접미사 트리 생성
    for i in range(n):
        current_node = root
        j = i
        while j < n:
            if text[j] not in current_node.children:
                new_node = Node(j, n - j)
                current_node.children[text[j]] = new_node
                break
            else:
                child = current_node.children[text[j]]
                edge_length = child.length
                k = 0
                while k < edge_length and j + k < n and text[child.start + k] == text[j + k]:
                    k += 1
                if k < edge_length:
                    split_node = Node(child.start, k)
                    split_node.children[text[child.start + k]] = child
                    child.start += k
                    child.length -= k
                    current_node.children[text[j]] = split_node
                    split_node.children[text[j + k]] = Node(j + k, n - (j + k))
                    break
                j += edge_length
                current_node = child

    # 트리의 간선 레이블 수집
    result = []
    def collect_edges(node):
        if node.start != -1:
            result.append(text[node.start:node.start + node.length])
        for child in node.children.values():
            collect_edges(child)

    collect_edges(root)
    return result

def run_with_expanded_stack():
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))

if __name__ == '__main__':
    # 확장된 스택 크기 내에서 메인 함수를 별도의 스레드로 실행
    thread = threading.Thread(target=run_with_expanded_stack)
    thread.start()
    thread.join()

