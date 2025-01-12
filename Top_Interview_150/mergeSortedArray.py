class Solution:
    def merge(self, nums1, m, nums2, n):
        # Pointers for nums1, nums2, and the final position in nums1
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge nums2 into nums1 starting from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If any elements are left in nums2, copy them over
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        return nums1  # Return the merged result directly


# Example usage for driver
param_1 = [1, 2, 3, 0, 0, 0]
param_2 = 3
param_3 = [2, 5, 6]
param_4 = 3

solution = Solution()
result = solution.merge(param_1, param_2, param_3, param_4)
print(result)  # Output: [1, 2, 2, 3, 5, 6]
