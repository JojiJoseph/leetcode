class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        ans = ""
        while i < n:
            if command[i] == "G":
                ans += "G"
                i += 1
            elif command[i:i+2] == "()":
                ans += "o"
                i += 2
            else:
                ans += "al"
                i += 4
        return ans
