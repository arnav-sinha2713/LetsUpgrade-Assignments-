# Assignment 1

# List
li=["Arnav","Mahi",2713,2756.36]
print(li)
print(type(li))

li.append(4547) # 1
print(li)
a=li.index("Mahi") # 2
print(a)
b=li.pop() # 3
print(b)
li.reverse() # 4
print(li)
li.clear() # 5
print(li)

# Dictionary
di={
    "name" : "Arnav" ,
    "age" : "17",
    "phone" : 9172840726,
    "email" : "arnavjdsg@gmail.com"
}
print(di)
print(type(di))

c=di.get('name') # 1
print(c)
d=di.items() # 2
print(d)
e=di.keys() # 3
print(e)
f=di.values() # 4
print(f)
di.clear() # 5
print(di)

# Sets
st={"Arnav",256,256,618.334,"Mahi"}
print(st)
print(type(st))

g=st.pop() # 1
print(g)
h=st.copy() # 2
print(h)
i={"Arnav"}
print(i.issubset(st)) # 3
j={"Arnav",256,618.334,"Mahi",342,"king"}
print(j.issuperset(st)) # 4
st.clear() # 5
print(st)

# Tuple
tu=("Arnav","Arnav",2,2,3,3,4,5,6,"Mahi")
print(tu)
print(type(tu))

k=tu.index("Arnav") # 1
print(k)
l=tu.count(2) # 2
print(l)
print(len(tu)) # 3

# Strings
s="I am a good boy and I love to program using python"
print(s)
print(type(s))

print(len(s)) # 1
m=s.count("a") # 2
print(m)
n=s.upper() # 3
print(n)
o=s.lower() # 4
print(o)
print(o.islower()) # 5

# Thank You