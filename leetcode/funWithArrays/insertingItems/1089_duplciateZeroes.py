class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i=0
        while(i<length):
            #checks whether the element is 0
            if not arr[i]:
                arr.insert(i, 0)
                arr.pop(length)
                i += 1
            i += 1