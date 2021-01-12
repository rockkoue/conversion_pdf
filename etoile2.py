h=10
Net=1
Nbr_espac=h-1
for i in range(h):
    Net+=2
    Nbr_espac-=1
    print(Nbr_espac*" "+Net*"*")
    
