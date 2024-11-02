# python3
import sys


def build_suffix_array(text):
    # Step 1: Generate all suffixes along with their starting indices
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Step 2: Sort the suffixes lexicographically by the suffix strings
    suffixes.sort()
    
    # Step 3: Extract the starting indices of sorted suffixes
    result = [suffix[1] for suffix in suffixes]
    
    return result



if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
