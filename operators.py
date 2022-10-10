# assignment operator
# = simple assignment operator
# shift value from right to left variable
var1 = 20 #20 assigned to var1
print(var1)

var1, var2 = 34, 45
print(var1, var2)

var1, var2 = var2, var1
print(var1, var2)
# multiple assignment
var1 = var2 = var3 = 100
print(var1, var2, var3)
print(id(var1))
print(id(var2))
print(id(var3))

#short-hand assignment operator
num1 = 20
print(id(num1))
# num1 = num1 + 5
num1+=5
print(id(num1))
print(num1) 

# arithmetic operators
# + addition
from array import array
n1 = array("i", [3,4,5])
n2 = array("i", [6,7,8])
n3 = n1+n2
print(n3)

# arithmetic operators
# +, -, =, /
import math
var1 = 28
var2 = 7
var3 = var1//var2
var4 = var1%var2
var5 = var1**var2
print(var3, var4, var5)
var6 = math.pow(2, 4)
print(var6)
var7 = math.sqrt(49)
print(var7)

#Relational Operator
#compare two values and return boolean result
# == equals to
#value1 is equals to value2 -> True
from array import array
var1 = {1, 2, 3}
var2 = {1, 2, 3}
result = (var1==var2)
print(result)

#greater than >
#left value is greater than right value i.e. v1>v2 then it is true
v1 = 3
v2 = 3
result=v1>v2
print(result)

# less than <
# left value is less than right value -> true
v1 = 12
v2 = 20
result= v1<v2
print(result)

# greater than or equals to
#left value is greater than or equals to right value->true
v1 = 10
v2 = 10
result = v1>=v2
print(result)

#less than or equals to 
#left value is less than or equals to right value -> true
v1 = 10
v2 = 10
result= v1<=v2
print(result)

#not equals to !=
#left value is equals to right value
v1 = 20
v2 = 20
result1 = v1==v2
result2 = v1 != v2
print(result1, result2)

#logical operator
#1. and
result = (10>5) and (10>6)
print(result)
result = (10>56) and (10>65)
print(result)

#2. or

result = (10>5) or (10>6)
print(result)
result = (10>56) or (10>65)
print(result)

#3.not
#true -> False
#false -> True
print(not True)
print(not False)
print(not True or True)
print(not False and False)
