# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
# You are also given three integers sr , sc and color . You should perform
# a flood fill on the image starting from the pixel image[sr][sc] .
# Return the modified image after performing the flood fill.

image = [[1,1,1],[1,1,0],[1,0,1]]

# 1 1 1
# 1 1 0
# 1 0 1

sr = 1
sc = 1
color = 2
old_color = image[sr][sc]
m = len(image)-1
n = len(image[0])-1

def flood_fill(sr,sc):
    if image[sr][sc] != old_color:
        return
    else :
        image[sr][sc] = color
        if sc<n :
            flood_fill(sr,sc+1)
        if sc>0:
            flood_fill(sr,sc-1)
        if sr<m:
            flood_fill(sr+1,sc)
        if sr>0:
            flood_fill(sr-1,sc)


flood_fill(sr,sc)

print(image)


