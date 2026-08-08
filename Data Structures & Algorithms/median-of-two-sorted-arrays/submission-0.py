class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)

        # where would the median be in two joined lists?
        # or the left half of the median when they're joined
        target_idx = (total) // 2

        # construct the list as we go, popping off the lower of each of the two sides
        # until we can get at that index

        all_nums = []
        while len(all_nums) < target_idx + 1:
            if len(nums1) != 0 and len(nums2) != 0:
                if nums1[0] < nums2[0]:
                    all_nums.append(nums1.pop(0))
                else:
                    all_nums.append(nums2.pop(0))
            elif len(nums1) == 0:
                all_nums.extend(nums2)
            else:
                all_nums.extend(nums1)

        if total % 2 != 0:
            return all_nums[target_idx]
        
        return (all_nums[target_idx] + all_nums[target_idx - 1]) / 2