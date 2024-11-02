# python3
import sys

def BWT(text):
    # Step 1: Generate all cyclic rotations of the input text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Step 2: Sort the rotations lexicographically
    rotations.sort()
    
    # Step 3: Extract the last column of the sorted rotations
    last_column = [rotation[-1] for rotation in rotations]
    
    # Step 4: Join the last column characters to get the BWT result
    return ''.join(last_column)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))