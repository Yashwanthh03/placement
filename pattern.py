index=1
num=5
while(index<6):
    if index%2==0:
        print(f"{index+1}",end="")
        print(f"{index}"*(num-1))
    else:
        print(f"{index}"*(num-1),end="")
        print(f"{index+1}")
    index+=1