def solution(A):
    A=sorted(A)
    max1=A[-1]*A[-2]*A[-3]
    if A[0]<0 and A[1]<0:
        max2 = A[0]*A[1]*A[-1]
        if max2>max1:
            return max2
        else:
            return max1
    else:
        return max1