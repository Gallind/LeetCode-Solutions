class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
        
        sol = []
        node = trie.root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                sol.append(node.suggestions)
            else:
                sol.append([])
                node = None
        return sol
                










