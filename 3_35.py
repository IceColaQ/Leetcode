class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        while(left<=right):
            middle = (right + left) // 2
            if ( nums[middle] < target ):
                left = middle + 1
            elif ( nums[middle] > target ):
                right = middle - 1
            elif ( nums[middle] == target ):
                return middle
        return right + 1

# 还是一个二分法查找或者插入的的问题 
# 一定要注意 最后为什么返回 right + 1
# 这里的加一是因为 left 和 right都是数组中的下标 返回数组的序次的时候应该+1 (List从0 开始)
# (考虑 递归的条件！)