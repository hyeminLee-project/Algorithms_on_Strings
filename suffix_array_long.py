# python3
import sys
# def build_suffix_array(text):
#   """
#   Build suffix array of the string text and
#   return a list result of the same length as the text
#   such that the value result[i] is the index (0-based)
#   in text where the i-th lexicographically smallest
#   suffix of text starts.
#   """
#   result = []
#   # Implement this function yourself
#   return result
def build_suffix_array(text):
    n = len(text)
    suffix_array = list(range(n))
    rank = [ord(c) for c in text]  # Initial ranks based on character ASCII values
    k = 1
    
    while k < n:
        # Sorting by the tuple (current rank, next rank)
        combined_rank = [(rank[i], rank[i + k] if i + k < n else -1, i) for i in range(n)]
        
        # Sort by the tuples (current rank, next rank)
        combined_rank.sort()
        
        # Update suffix array based on sorted combined ranks
        suffix_array = [suffix[2] for suffix in combined_rank]
        
        # Update ranks after sorting
        new_rank = [0] * n
        for i in range(1, n):
            new_rank[suffix_array[i]] = new_rank[suffix_array[i - 1]]
            if combined_rank[i][0:2] != combined_rank[i - 1][0:2]:
                new_rank[suffix_array[i]] += 1
        
        rank = new_rank
        k *= 2
    
    return suffix_array

if __name__ == '__main__':
    import sys
    text = sys.stdin.readline().strip()
    result = build_suffix_array(text)
    print(" ".join(map(str, result)))