class Solution:
    def rotate(self, nums, k):
        #paso1
        size = len(nums)
        aux = [0] * size

        #paso2
        for i in range(size):
            position = (i + k) % size

            #paso3
            aux[position] = nums[i]

        #paso4
        nums[:] = aux