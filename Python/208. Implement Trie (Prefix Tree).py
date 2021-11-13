class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False
    def __getitem__(self, idx):
        return self.children[idx]
    def __setitem__(self, idx, value):
        self.children[idx] = value

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node[ch]
            else:
                node[ch] = TrieNode()
                node = node[ch]
        node.end_node = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node[ch]
            else:
                return False
        return node.end_node
            
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node[ch]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
