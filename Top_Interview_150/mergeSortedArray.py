class Solution:
    def __init__(self, nums1, m, nums2, n):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n

    def merge(self):
        p1, p2, p = self.m - 1, self.n - 1, self.m + self.n - 1

        while p1 >= 0 and p2 >= 0:
            if self.nums1[p1] > self.nums2[p2]:
                self.nums1[p] = self.nums1[p1]
                p1 -= 1
            else:
                self.nums1[p] = self.nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            self.nums1[p] = self.nums2[p2]
            p2 -= 1
            p -= 1

    def get_result(self):
        return self.nums1


# Example usage for driver
param_1 = [1, 2, 3, 0, 0, 0]
param_2 = 3
param_3 = [2, 5, 6]
param_4 = 3

solution = Solution(param_1, param_2, param_3, param_4)
solution.merge()
print(solution.get_result())  # Output: [1, 2, 2, 3, 5, 6]
