class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            if flowerbed[0]==0 and n==1 or n==0 :
                return True
            return False
        for i in range(0,len(flowerbed)):  
            if flowerbed[i]==0:
                if i==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                elif i==len(flowerbed)-1 and flowerbed[i-1]==0:
                    print('hi')
                    flowerbed[i]=1
                    n-=1
                elif flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
            if n<=0:
                return True
        return False
                



        
