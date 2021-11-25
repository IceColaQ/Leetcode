class Solution(object):
    def search(self, nums, target):
        index = -1
        for number in nums:
            if number == target:
                index = nums.index(number)
                return index
        return index
    

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while (left<=right):
            
            middle = left + (right - left) // 2
            print ( middle )

            if ( nums[middle] < target):
                left = middle + 1
            elif ( nums[middle] > target ):
                right = middle - 1
            else:
                return middle
        return -1

a = Solution()
b = a.search([-1,0,1,2],1)
print(b)

# ###
# 这是一个典型的数组的二分查找的题目。
# 看到题目中出现 “有序上升”，‘无重复元素’ 等词汇的时候就可以考虑用
# binary-search的方法了。 

# 我第一种方法直接暴力索引。

# 第二种方法是采用二分法，注意在这里划分左右界限的时候
# 考虑到可能会出现偶数个元素的情况，middle = left + (right - middle)//2
# 在 python里 // 表示整数除法。
# 同时，第二种方法也是一个递归函数完成的。
# ###