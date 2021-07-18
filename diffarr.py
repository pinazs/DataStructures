#Given an array nums of n integers where nums[i] is in the range [1, n],
#return an array of all the integers in the range [1, n]
#that do not appear in nums.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        #return nums
        i=1
        new_arr=[]
        count=0
        while i<= len(nums):
            #print (i)
            count=0
            for val in nums:
                if i == val:
                   # print(val)
                    i=i+1
                    count=1
                    break
            if(count == 0):
                new_arr.append(i)
                #print(i)
                i=i+1
           
        return new_arr        

s1=Solution()
nums=[4,3,2,7,8,2,3,1]
x=s1.findDisappearedNumbers(nums)
print(x)
                
