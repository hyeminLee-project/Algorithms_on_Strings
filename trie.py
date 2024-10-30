#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = {} # 트라이를 저장할 딕셔너리
    node_id = 0 # 현재 노드 ID
    tree[0] = {} #루트 노드 초기화
    for pattern in patterns:
        current_node = 0 # 루트 노드에서 시작
        for char in pattern:
            #현재 노드에 해당 문자가 없으면 새 노드 생성
            if char not in tree[current_node]:
                node_id += 1 #새로운 노드 ID 증가
                tree[current_node][char] = node_id
                tree[node_id] = {} #새 노드 초기화
            current_node = tree[current_node][char]
    # write your code here
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
