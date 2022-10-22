A = [5,8,15,2,21,16,20]
B = [5,1,19,2,4]

# union = A.append(B)
# print(union)
C = []

N = len(A)

for i in range(N):
    elemento = A[i]
    if elemento not in B:
        C.append(elemento)
print(C)




