class Solution:
    def maxArea(self, height: List[int]) -> int:
        # store areas in array
        areas=[]
        # set pointers at first and last element
        l = 0
        r = len(height)-1
        while l < r:
            # add to area array
            areas.append((r-l)*(min(height[r], height[l])))
            # always move pointer that points to the lower line
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max(areas)



