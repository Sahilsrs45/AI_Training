sumEven=0;
countEven=0;
sumOdd=0;
countOdd=0;

for i in range(1,50):
    if i%2==0 :
        sumEven+=i
        countEven+=1
        
        print("even no -",i)
    else :
        sumOdd+=i
        countOdd+=1  
        print("odd no -",i)  
        
print("sum of even numbers :",sumEven)
print("count of even no - ",countEven)
print("sum of odd numbers : ",sumOdd)
print("count of odd no - ",countOdd)    
            