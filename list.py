#listing elements
#adding value in list
var1 = ["book","copy","pen"]
var1.insert(1,"pencil")
print(var1)

var1 = ["book","copy","pen"]
print(var1[0])

#extending var1
var1 = ["book","copy"]
var2 = ["pen","pencil"]
var1.extend(var2)
print(var1)

#adding (extending)tuple
var1 = ["book","copy"]
var2 = ("pen","pencil")
var1.extend(var2)
print(var1)

#removing value from list
var1 = ["book","copy","pen"]
var1.remove("pen")
print(var1)

#removing individual value from list 
var1 = ["book","copy","pen"]
var1.pop(1)
print(var1)

#removing second value
var1 = ["book","copy","pen"]
var1.remove("copy")
print(var1)

#removing last value
var1 = ["book","copy","pen"]
var1.pop()
print(var1)

var6="pra"
print(var6)
