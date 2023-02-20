entrada1, input2 = int(input()), int(input())
quality =[]
bingo   =[]
simp    =[]
for _ in range(input2):
  quality += [int(input())] 
for suerte in range(entrada1): 
  if quality.count(suerte) > 1: 
    bingo += [quality.count(suerte)] 
    simp += [suerte] 
X = max(bingo) 
for suerte in range(len(simp)):
  if bingo[suerte] == X:
    print(simp[suerte])