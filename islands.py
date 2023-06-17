# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

Input = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


def x(p,q):

    if Input[p,q] == 1:
        Input[p,q] = 2
        x(p,q+1)
        x(p,q-1)
        x(p-1,q)
        x(p+1,q)
    if Input[p,q] == 0 :
        return 
    if Input[p,q] == 2:
        return 
    

island = 0
for i in range(len(Input)):
    for j,val in enumerate(Input[i]):
        if (val == "1"):
            island+= 1
            x(int(i),int(j))
            

print(Input)     

