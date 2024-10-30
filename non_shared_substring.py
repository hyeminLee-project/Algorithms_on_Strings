# python3
import sys

def solve(p, q):
    """p(Text1)와 q(Text2)에 대해 p에만 존재하는 가장 짧은 부분 문자열을 찾습니다."""
    
    # p에서 가능한 모든 부분 문자열을 길이별로 탐색
    for length in range(1, len(p) + 1):
        for i in range(len(p) - length + 1):
            substring = p[i:i + length]  # 부분 문자열 추출
            
            # 해당 부분 문자열이 q(Text2)에 존재하지 않으면 반환
            if substring not in q:
                return substring  # 첫 번째로 찾은 비공유 부분 문자열 반환

    return ""  # 비공유 문자열이 없는 경우 (이 문제에서는 항상 존재해야 함)

# 입력 처리
p = sys.stdin.readline().strip()  # Text1 입력
q = sys.stdin.readline().strip()  # Text2 입력

# 정답 계산 및 출력
ans = solve(p, q)
sys.stdout.write(ans + '\n')
