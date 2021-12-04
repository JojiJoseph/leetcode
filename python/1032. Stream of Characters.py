from collections import deque
from typing import List


class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None]*26

    def add_word(self, word, i=0):
        n = len(word)
        if i == n:
            self.end = True
            return
        ch = ord(word[i]) - ord('a')
        if not self.children[ch]:
            self.children[ch] = TrieNode()
        self.children[ch].add_word(word, i+1)

    def find(self, word_stream, i=0):
        n = len(word_stream)

        if self.end == True:
            return True
        if i == n:
            return False
        ch = ord(word_stream[i])-ord('a')
        if self.children[ch]:
            return self.children[ch].find(word_stream, i+1)
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = deque(maxlen=2001)
        self.trie = TrieNode()
        for word in words:
            self.trie.add_word(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.find(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
