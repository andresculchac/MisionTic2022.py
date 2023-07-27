def main():
    num = int(input())
    result_list = []
    for i in range(num):
        m = int(input())
        n = int(input())
        result_list.append(ackerman(m,n))

    for j in result_list:
        print(j)

def ackerman(m,n):
    if (m == 0):
        return n+1
    elif m>0 and n==0:
        return ackerman(m-1,1)
    elif m>0  and n > 0:
        return ackerman(m - 1,ackerman(m,n-1))
    
main()

