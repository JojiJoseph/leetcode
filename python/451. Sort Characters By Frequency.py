class Solution:
    def frequencySort(self, s: str) -> str:
        arr = [[i,0] for i in range(256)]
        for ch in s:
            arr[ord(ch)][1] += 1
        arr.sort(key=lambda x: x[1], reverse=True)
        out = ""
        for ch, count in arr:
            out += chr(ch)*count
        return out
