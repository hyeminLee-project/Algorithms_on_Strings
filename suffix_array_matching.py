# python3
import sys
from collections import deque, defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.output = []
        self.fail = None

class AhoCorasick:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, pattern, index):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append(index)
    
    def build_failure_links(self):
        queue = deque()
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)
        
        while queue:
            current_node = queue.popleft()
            for char, child in current_node.children.items():
                queue.append(child)
                fail_node = current_node.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                child.fail = fail_node.children[char] if fail_node else self.root
                child.output += child.fail.output if child.fail else []
    
    def search(self, text):
        node = self.root
        occurrences = set()
        for i in range(len(text)):
            while node and text[i] not in node.children:
                node = node.fail
            node = node.children[text[i]] if node else self.root
            if node:
                for pattern_index in node.output:
                    occurrences.add(i - pattern_lengths[pattern_index] + 1)
        return occurrences

def find_occurrences(text, patterns):
    ac = AhoCorasick()
    global pattern_lengths
    pattern_lengths = [len(pattern) for pattern in patterns]
    
    # Insert all patterns into the Aho-Corasick Trie
    for i, pattern in enumerate(patterns):
        ac.insert(pattern, i)
    
    # Build failure links for Aho-Corasick automation
    ac.build_failure_links()
    
    # Search for patterns in the text
    return ac.search(text)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, sorted(occs))))