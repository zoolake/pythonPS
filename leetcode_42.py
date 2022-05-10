class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        left_max, right_max = height[left], height[right]

        # two-pointer
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                result += left_max - height[left]
                left += 1

            else:
                result += right_max - height[right]
                right -= 1

        return result