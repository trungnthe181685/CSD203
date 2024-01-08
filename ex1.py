def nearest():
    n= int(input(" Input the elemental of the array:"))
    a= []

    for i in range(n):
        a= a+ [float(input(" Enter a[%d]: " %i))]
    
    s=0
    for i in range(n):
        s+= a[i]

    averages = s/n
    print(f"The average value of the array is {averages}")

    result=[]
    for i in range(n):
        result.append(abs(a[i] - averages))
    
    positions=[]
    for i in range(n):
        if result[i]== min(result):
            positions.append(str(i))
            
    position_str = ", ".join(positions)
    print("The positions of the elements which have values nearest to the average are", position_str)    
position= nearest()


    
    