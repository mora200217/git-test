class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        arr = [0 for i in range(n+1)]
        arr[1], arr[2] = 1, 1
        for i in range(3, len(arr)):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        return arr[n]

s = Solution()
print(s.tribonacci(5))