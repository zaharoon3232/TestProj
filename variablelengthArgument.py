def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


person('zaid', age=31, city='Canton', mob=1234235)