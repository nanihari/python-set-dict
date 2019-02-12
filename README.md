# python-set,dict,array
## An unordered list of unique elements is defined as sets and sets does not have an attribute "append". we have to work with add()
normal_set = set(["a", "b","c"]) 
# Adding an element to normal set is fine and for adding even update() works
normal_set.add("d") 
print(normal_set).
#a = set()
#a.update([1]) #works
#a.add(1) #works
#a.update([1,2])#works
#a.add([1,2])#fails 
## frozen set in python is a immutable version of python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation. Due to this, frozen sets can be used as a key in Dictionary or as element of another set. But like sets, it is not ordered(the elements can be set at any index).
we have many methods like union, intesection, difference and clear methods.
## creation of sets is same as lists and tuple. 
n=set([1,2,3,4,5])
print(n)
## dicard function will be used to delete an element in sets. (num.discard(element))
## to create an intersection of the sets. (num1& num2)
##union function can be defined by num|num1 (or) num.unoin(num1)
## difference can be defined as num-num1
The symmetric difference of two sets A and B is the set of elements which are in either of the sets A or B but not in both ca be defined as seta=setb^setc or seta=setb.symmetric_difference(B)
