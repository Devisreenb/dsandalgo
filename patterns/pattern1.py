"""
techniques :
Run the outer for loop for no. of times you need the lines 
to be printed 

"""

"""
___________________columns
|* 
|* *
|* * *
|* * * *
rows 

no.of lines = no. of rows = no.of times outerloop runs 

identify how many columns are there for every row and types of elements 
here no. of columns in each row = row no.

symbol is *
"""
rows = 4

for i in range(rows+1):
    for j in range(i):
        print("*",end=" ")
    print("\n") 
