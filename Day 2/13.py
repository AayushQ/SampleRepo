result =""
for r in range(0,7):
   
    for c in range(0,5):
       
        if((r==0 and c==0 or c==4) or (r==1 and (c==0 or c==4)) or (r==2 and(c==0 or c==1 or c==3 or c==4)) or (r==3 and (c==0 or c==2 or c==4)) or (r==4 and (c==0 or c==4)) or (r==5 and (c==0 or c==4)) or (r==6 and (c==0 or c==4))):
            result=result+"* "
        else:
            result=result+" "
    result=result+"\n"

print(result)
