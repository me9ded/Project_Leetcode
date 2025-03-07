class Solution:
    def is_prime(self,limit):
        temp=[True]*(limit+1)
        temp[0]=temp[1]=False
        for number in range(2,int(limit**0.5+1)):
            if temp[number]:
                for multiple in range(number*number,limit+1,number):
                    temp[multiple]=False
        return temp
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr=self.is_prime(right)
        primes=[number for number in range(left,right+1) if arr[number]]
        if len(primes) < 2:
            return -1,-1
        difference=float("inf")
        pair=(-1,-1)
        for index in range(1,len(primes)):
            current=primes[index]-primes[index-1]
            if current < difference:
                difference=current
                pair=primes[index-1],primes[index]
        return pair
        