# 605. Can Place Flowers (Easy)
class Solution:
    def canPlaceFlowers(flowerbed, n) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0



        # if len(flowerbed) == 1 and flowerbed[0] == 0:
        #     return True
        # if len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0 and n <= 1:
        #     return True
        # if len(flowerbed) == 3 and flowerbed[0] == 0 and flowerbed[1] == 0 and flowerbed[2] == 0 and n <= 2:
        #     return True
        # for i in range(len(flowerbed) - 2):
        #     if (i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0):
        #         flowerbed[i] = 1
        #         n -= 1
        #     elif (flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i + 2] != 1):
        #         flowerbed[i + 1] = 1
        #         n -= 1
        #     elif (i == len(flowerbed) - 3 and flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0):
        #         flowerbed[i + 2] = 1
        #         n -= 1
        #
        # if n <= 0:
        #     return True
        # else:
        #     return False

print(Solution.canPlaceFlowers([0,0,0], 2))