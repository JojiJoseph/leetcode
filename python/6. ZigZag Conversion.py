class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        forward = True
        idx = 0
        for ch in s:
            idx %= numRows
            rows[idx] += ch
            if forward:
                idx += 1
            else:
                idx -= 1
            if idx == 0:
                forward = True
            if idx == numRows:
                forward = False
                idx -= 2
                if idx < 0:
                    idx = 0
        return "".join(rows)


if __name__ == "__main__":
    soln = Solution()
    assert soln.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert soln.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert soln.convert("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    assert soln.convert("A", 1) == "A"
    print("All test cases are passed successfully!")
