#PATTERN 1
""" ****
    ****
    ****          for n=4
    ****
"""
def pattern1(n):
    for row in range(1,n+1):
        for column in range(1,n+1):
            print("*",end="")
        print()
n=int(input())
pattern1(n)


#PATTERN 2
"""   *
      **
      ***
      ****
      *****
"""
def pattern2(n):
    for row in range(1,n+1):
        for column in range(1,row+1):
            print("*",end="")
        print()
n=int(input())
pattern2(n)

#PATTERN 3
"""
    *****
    ****
    ***
    **
    *
"""
def pattern3(n):
    for row in range(0,n):
        for column in range(1,n+1-row):           #can also use n-row
            print("*",end="")
            row-=1
        print()
n=int(input())
pattern3(n)

#PATTERN 4
"""
    1
    23
    456
    78910
"""
def pattern4(n):
    i=1
    for row in range(1,n+1):
        for column in range(1,row+1):
            print(i,end="")
            i+=1
        print()
n=int(input())
pattern4(n)

#PATTERN 5
"""
    1
    12
    123
    1234
"""
def pattern5(n):
    i=1
    for row in range(1,n+1):
        for column in range(1,row+1):
            i+=1
            print(column,end="")
        print()
n=int(input())
pattern5(n)

#PATTERN 6
"""
    *
    **
    ***
    ****
    ***
    **
    *
"""

def pattern6(n):
    for row in range(1,n*2):
        if(row<=n):
            print("*"*row)
        else:
            print("*"*(n*2-row))
n=int(input())
pattern6(n)


        
      
