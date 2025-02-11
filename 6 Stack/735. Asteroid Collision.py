asteroids = [5,10,-5,-10,-10]
s=[]

for a in asteroids:
    if a>0:
        s.append(a)
    else:
        while s and s[-1]>0 and s[-1] <-a:
            s.pop()
            
        if s and s[-1]==-a:
            s.pop()
            
        elif not s or s[-1] < 0:
            s.append(a)
            
# return s
print(s)


















# # a=asteroids
# # ioa = list(range(len(a)))
# # c=sorted(a)

# # print(c)

# ast =asteroids
# a=[]
# i=0
# while i<len(asteroids):
#     if ast.pop()<0:
        
        