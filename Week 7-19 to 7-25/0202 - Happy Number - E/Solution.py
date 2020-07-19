class Solution:
    def isHappy(self, n):
        memory = set()
        while n not in memory:
            print(n)
            memory.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        print(True)
        return True in memory


solve = Solution()

solve.isHappy(19)
