#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(x, y, z):
    triangle = [x, y, z]
    triangle.sort()
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    if a+b<c:
        r = 0
    elif c == (((a**2)+(b**2))**0.5):
        r = 2
    elif (c**2) > ((a**2)+(b**2)):
        r = 3
    elif (c**2) < ((a**2)+(b**2)):
        r = 1
    return(r)

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
