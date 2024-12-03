# python3
import sys

def InverseBWT(bwt):
    # Initialize variables
    n = len(bwt)
    first_col = sorted(bwt)  # The first column is the sorted BWT
    last_to_first = [0] * n  # Mapping from last column to first column
    
    # Build the last-to-first mapping
    count = {}
    first_count = {}
    for i, char in enumerate(first_col):
        if char not in first_count:
            first_count[char] = 0
        first_count[char] += 1
        count[(char, first_count[char])] = i

    bwt_count = {}
    for i, char in enumerate(bwt):
        if char not in bwt_count:
            bwt_count[char] = 0
        bwt_count[char] += 1
        last_to_first[i] = count[(char, bwt_count[char])]

    # Reconstruct the original string
    result = []
    index = bwt.index('$')  # Start from the position of '$'
    for _ in range(n):
        result.append(bwt[index])
        index = last_to_first[index]

    return ''.join(result[::-1])  # Reverse the result to get the original string


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()  # Read the input
    print(InverseBWT(bwt))  # Print the reconstructed string
