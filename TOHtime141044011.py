def TOHtime(A,B,C,D,n):
    if n==1:
        i=A.pop()
        C.append(i)
        print("disk",i,": Move from", A[0] ,"to", C[0])
        D[i-1]+=abs((C[1]-A[1]))*i
        
    else:
        
        TOHtime(A,C,B,D,n-1)
        i=A.pop()
        C.append(i)
        print("disk",i,": Move from", A[0]," to", C[0])
        D[i-1]+=abs((C[1]-A[1]))*i
        
        TOHtime(B,A,C,D,n-1)
        

def callTOH(n):
    A=["SRC",1]
    B=["AUX",2]
    C=["DST",3]
    D=[]
    i=n
    while(i>=1):
        A.append(i)
        D.append(0)
        i-=1
    TOHtime(A,B,C,D,n)
    i=1
    while(i<=len(D)):
        print("Elapsed time for disk ",i,": ",D[i-1])
        i+=1
        


callTOH(4)
