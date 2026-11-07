sentence=input("enter sentence : ")
vowels=0
consonent=0
for ch in sentence:
    if ch==" ":
        continue
    if ch=="!":
        break
    
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonent+=1
print(f"Total vowels are {vowels}") 
print(f"Total consonents are {consonent}") 
               