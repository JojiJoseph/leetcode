class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def get_all_seq(length):
            
            lis = []
            flag = False
            for start_digit in range(1,10):
                digit = start_digit
                seq = ""
                
                for j in range(length):
                    if digit >= 10:
                        flag = True
                        break
                    seq += str(digit)
                    digit += 1
                if not flag:
                    lis.append(seq)
                else:
                    break
            return lis
        low_len = len(str(low))
        high_len = len(str(high))
        out = []
        for i in range(low_len, high_len+1):
            out.extend(get_all_seq(i))
        out = map(int,out)
        out = [item for item in out if low <= item <= high]
        return out
