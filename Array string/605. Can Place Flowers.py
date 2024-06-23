fb=[0,0,1,0,1]
fb=[0]
n=1
os=0
for i in range(len(fb)):
    if fb[i]==0:
        if i>0 and i<len(fb)-1:
            if fb[i-1]!=1 and fb[i+1]!=1:
                fb[i]=1
                os+=1
        elif i==0:
            if len(fb)!=1:
                if fb[i+1]!=1:
                    fb[i]=1
                    os+=1
            else: 
                fb[i]=1
                os+=1
                
        elif i==len(fb)-1:
            if fb[i-1]!=1:
                fb[i]=1
                os+=1            
        
if n<=os:
    print(True)
else: print(False)                



#  old working
# fb=[0,0,1,0,1]
# n=1
# c=0
# os=0
# for i in range(len(fb)):
#     if fb[i]==0:
#         if i>0 and i<len(fb)-1:
#             if fb[i-1]==1 or fb[i+1]==1:
#                 c+=1
#             else: 
#                 fb[i]=1
#                 os+=1
#         elif i==0:
#             if len(fb)!=1:
#                 if fb[i+1]==1:
#                     c+=1
#                 else: 
#                     fb[i]=1
#                     os+=1
#             else: 
#                 fb[i]=1
#                 os+=1
                
#         elif i==len(fb)-1:
#             if fb[i-1]==1:
#                 c+=1
#             else: 
#                 fb[i]=1
#                 os+=1
            
        
# if n<=os:
#     print(True)
# else: print(False)                