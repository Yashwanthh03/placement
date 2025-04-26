value=[6,7,1,3,8,2,5]

def maxStolenValue(value):
    num= len(value)
    if num== 0:
        return 0
    if num== 1:
        return value[0]
    
    DP=[0]*num
    DP[0]=max(DP[0],DP[1])
    for index in range(1,num):
        DP[index]=max(DP[index-1],DP[index-2]+value[index])
        print(DP)
    return DP[-1]
print(maxStolenValue(value))