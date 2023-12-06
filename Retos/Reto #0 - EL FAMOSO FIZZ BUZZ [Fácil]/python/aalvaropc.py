class Solution:
    def fizzbuzz(self):
        for i in range(1, 101):
            match i:
                case i if i % 15 == 0:
                    print('fizzbuzz')
                case i if i % 3 == 0:
                    print('fizz')
                case i if i % 5 == 0:
                    print('buzz')
                case _:
                    print(i)

res = Solution()
res.fizzbuzz()