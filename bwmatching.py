# python3
import sys
from collections import defaultdict

def PreprocessBWT(bwt):
    # Initialize dictionaries for starts and occ_counts_before
    starts = {}
    occ_counts_before = {char: [0] * (len(bwt) + 1) for char in set(bwt)}

    # Step 1: Compute starts
    sorted_bwt = sorted(bwt)
    for i, char in enumerate(sorted_bwt):
        if char not in starts:
            starts[char] = i

    # Step 2: Compute occ_counts_before
    for i in range(len(bwt)):
        char = bwt[i]
        for c in occ_counts_before:
            occ_counts_before[c][i + 1] = occ_counts_before[c][i] + (1 if c == char else 0)

    return starts, occ_counts_before

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    top = 0
    bottom = len(bwt) - 1

    while top <= bottom and pattern:
        symbol = pattern[-1]  # Take the last character of the pattern
        pattern = pattern[:-1]  # Remove the last character from the pattern

        # Check if the symbol is in the BWT range [top, bottom]
        if symbol in occ_counts_before:
            # Update top and bottom based on occ_counts_before and starts
            top = starts[symbol] + occ_counts_before[symbol][top]
            bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
        else:
            return 0

    return bottom - top + 1


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))
