for i in range(1,501):
    if i%41==0:
            break
    if i%6==0:
        continue
    
    if i%2!=0:
        print(i)