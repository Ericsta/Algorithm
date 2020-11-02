class Solution:
    def nextValue(self, chars, currentValue):
        m, n = len(chars), len(currentValue)
        dic = {}
        count = 0
        for char in chars:
            dic[char] = count
            count += 1
        curlist = [char for char in currentValue]
        if dic[curlist[-1]] < m - 1:
            curlist[-1] = chars[dic[curlist[-1]] + 1]
            return "".join(curlist)

        carry = 0
        for index, char in enumerate(curlist[::-1]):
            if index == 0:
                value = dic[char] + 1 + carry
            else:
                value = dic[char] + carry
            value, carry = value % m, value // m
            curlist[index] = chars[value]
        if carry != 0:
            curlist.append(chars[1])
        return "".join(curlist[::-1])



if __name__ == '__main__':
    matrix = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌"]
    b = "捌捌"
    solution = Solution()
    A = solution.nextValue(matrix, b)
    print(A)
