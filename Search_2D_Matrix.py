##TC=O(Log(M*N))
class Solution:
    def Search_2D_Matrix(self, matrix:list[list[int]],target:int)->bool:
        if not matrix: return False
        N = len(matrix[0])
        M = len(matrix)
        l,r = 0, len(N)-1
        mid = (l+r)//2
        while l<=r:
            if matrix[mid//M][mid%N]==target:
                return True
            elif matrix[mid//M][mid%N]<target:
                l=mid+1
            else:
                r=mid-1
            return False 
