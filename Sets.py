age={1,1,1,2,3,4,3,2,3,4,0}
print(age)

names={'adarsh','srikar','adarsh'}
print(names)

names.add('adarsh')
print(names)

names.add(1234)
print(names)

#discard is used to remove object form the sets
#syntax is set_name.discard(object)
#it doesnot throw any error if object is not present in the set
#set prints the values in it in the unorderd fashion

names.discard('murthy')
print(names)

print(names.clear())
print();print()

#after using set-name.clear() if we try to print the set we get the output as None

Junior_datascientist = {'R','Python','Tableau'}
Datascientist = {'R','Python','Scala','Java','Tableau'}

print(Junior_datascientist)
print(Datascientist)

#union is the builtin function realted to sets available in python.
#it returns all the elements belonging to both set_A and set_B
#Syntax is set_A.union(set_B)

union = Junior_datascientist.union(Datascientist)
print(union)