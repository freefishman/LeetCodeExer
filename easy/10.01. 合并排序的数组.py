class Solution:
    def merge(A, m, B, n) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        head = m+n-1
        while n > 0:
            if m == 0 and n > 0:
                A[head] = B[n-1]
                head -= 1
                n -= 1
            else:
                if B[n-1] >= A[m-1]:
                    A[head] = B[n-1]
                    head -= 1
                    n -= 1
                elif B[n-1] < A[m-1]:
                    A[head] = A[m-1]
                    A[m-1] = -1
                    head -= 1
                    m -= 1
        return A

print(Solution.merge([4,5,6,0,0,0],3,[1,2,3],3))