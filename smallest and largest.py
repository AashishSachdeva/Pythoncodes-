lar =None
small = None
while True:
    val=input('enter a number\n')
    if val =='done':
        break
    try :
        val=int(val)
        if small is None :
            lar=val
            small =val
        else:
            if val<=small:
                small=val
            if val>=lar:
                lar =val
    except:
        print ("please enter anumeric value\n")
print("smallest number is:",small,"largest number is:",lar)
