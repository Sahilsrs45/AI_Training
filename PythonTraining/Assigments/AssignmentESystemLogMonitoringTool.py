logs =["INFO", "DEBUG", "WARNING", "ERROR", "INFO", "CRITICAL", "WARNING"]

for i in logs:
    if i=="INFO":
        continue
    if i=="WARNING" or i=="ERROR":
        print(i)
        
    if i=="CRITICAL":
        break    