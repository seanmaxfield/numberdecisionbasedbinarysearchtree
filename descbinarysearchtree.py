n2=100
n3=101
n4=50
n5=51
n6=150
n7=151
n8=25
n9=26
n10=75
n11=76
n12=125
n13=126
n14=175
n15=176
n=int(input("search between 0 and 200: "))
amount=8
ind=[n,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15]
def binaryTree(ind):
    count=1
    retvalue=0
    side=""
    for i in range(3):
        if abs(ind[0]-ind[count]) < abs(ind[0]-ind[count+1]):
            retvalue=ind[count]
            count=2+(count*2)-1
            side="less than "
        else:
            retvalue=ind[count+1]
            count=2+(count*2)+1
            side="more than "
    print(side+str(retvalue))
    print("node "+str(round(count/2)))
binaryTree(ind)

