# python3
import sys

def kmp_prefix_function(pattern):
    # Preprocess the pattern to create the prefix array
    prefix = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            prefix[i] = j
    return prefix

def find_pattern(pattern, text):
    # Using the KMP algorithm to find all occurrences of pattern in text
    result = []
    prefix = kmp_prefix_function(pattern)
    j = 0  # index for pattern

    for i in range(len(text)):  # index for text
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):  # found a match
            result.append(i - j + 1)
            j = prefix[j - 1]
    
    return result

if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))