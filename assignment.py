largest =None
smallest = None
while True:
    val=input('enter a value')
    if val=='done':
        break
    try:
        val=int(val)
        if largest is None:
            largest=val
            smallest=val
            continue
        if val>largest:
            largest=val
        if val<smallest:
            smallest=val
    except:
        print('Invalid input')
        continue
print('Maximum is',largest)
print('Minimum is',smallest)
    
