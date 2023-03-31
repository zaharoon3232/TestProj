import array as a

vals = a.array('i', [10,20,23,245,123])

newArray = a.array(vals.typecode, (a for a in vals))
print(newArray)

print(vals)
#print(vals.buffer_info())

vals.reverse()
print(vals)

for  i in range(len(vals)):
    print(vals[i])

vale = a.array('u', ['a','e','i'])
for e in vale:
    print(e)


#vals = a.array('i', [10,20.23,-23,245,123])
#print(vals)


#vals = a.array('I', [10,20.23,-23,245,123])
#print(vals)


