def lotteryNumbers():
  def CheckNums(n):
    for i in range(1, len(n)):
      for j in range(i):
        if n[j] == n[i]:
          n[i] += 1
          CheckNums(n)
  from random import randint
  global lottoNums
  lottoNums = []
  for i in range(7):
    lottoNums.append(randint(1,49)) 
  CheckNums(lottoNums)
  for i in range(len(lottoNums)):
    if lottoNums[i] > 49:
      lottoNums[i] = 1
  CheckNums(lottoNums)
  print("Your lottery numbers are:")
  for i in range(len(lottoNums)-1):
    print(lottoNums[i], end="   ")
  print()
  print("And the bonus ball is: ", lottoNums[6])

UserNums = list(input("Type your 6 lotto numbers, seperated by a space...  ").split())
print()

lotteryNumbers()
lottoNums = [1,2,3,4,5,6,7]
print()
CorrectNums = 0
for i in range(6):
  for j in range(7):
    if int(lottoNums[j]) == int(UserNums[i]):
      CorrectNums += 1
      
print("You got ", CorrectNums, " right, your probability of winning the lottery (based off of the numbers you got correct) was: ", ((1/49)**(6-CorrectNums))*100, "%", sep="")