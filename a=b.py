a=3
b=5
#print(a+b)


#list
a_list =[10,20,30,40]
#print(type(a_list))
#print(id(a_list))


#interpolation
name="chandu"
age = 20
#print(f"my name is {name} and im {age} years old" )


#operators
n1=3
n2=2
#print(f"sum of n1 and n2 is {n1+n2}")
#print(f"exponentiation of n1 and n2 is {n1**n2}")

#compound assignment operator
x=5
x += 5  # Equivalent to x = x + 5
#print(f" {x}")

#comparision operator
n1=5
n2=3
n3=6
n4=5
#print(n1==n2)
#print(n1==n4)
#print(n1!=n4)
#print(n1<n3)

#logical operator
x=5
y=6
a=10
b=8
resultand=x<y and a>b
#print(resultand)

#membership operator
a_list =[10,20,30,40]
is_present=40  in a_list
#print(is_present)
is_present=50 in a_list
#print(is_present)
is_present=50 not in a_list
#print(is_present)

#identity operator
n1=5
n2=5
#print(n1==n2)
#print(n1 is n2)
print(id(n1))
print(id(n2))
n1=[1,2,3,4,5,6,7,8,9]
n2=[1,2,3,4,5,6,7,8,9]
#print(n1 is n2)
#print (n1 is not n2)
#print (n1==n2)
print(id(n1))
print(id(n2))


