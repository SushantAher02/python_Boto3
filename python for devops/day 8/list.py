# s1= "abhishek"
# s2 = "sushant"
# s3 = "tejas"
# print(s1)
# print(s2)
# print(s3)
# print(s4)

################################################################################
#list

studentlist =["abhishek", "sushant","tejas"]

print(studentlist)
print(studentlist[0])
listlen = len(studentlist)
print(listlen)

#appending
studentlist.append("aher")
print(studentlist)

#removing
studentlist.remove("abhishek")
print(studentlist)

#slicing
subset = studentlist[1:3]
print(subset)

#concatenation
#newlist = studentlist + [5,6]
#print(newlist)
print(studentlist.sort())

