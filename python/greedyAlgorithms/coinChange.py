def coinChange(number,coins):
  N=number
  coins.sort()
  index=len(coins)-1
  while True:
    if N>=coins[index]:
      print(coins[index])
      N=N-coins[index]
    if N<coins[index]:
      index-=1 
    if N==0:
      break

array=[1,2,5,10,25,50,100]
print(coinChange(201,array))
