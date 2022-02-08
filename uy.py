# dict - словари

#new_dict = {
#    "x" = [100,
#           "y"] = 200
#}
#print(new_dict["x"])

#new_dict = {
#    "samat" : {
#        "algebra" : 80,
#        "biologia" : 90
#    },
#}
#print(new_dict['samat']['algebra'])

#a = dict()

#a = {}
#print(a)

#a = dict([(10, 17), ('a', 1)])
#print(a)

 #dicts = {'s' : 'Nazik'}


#dick = {
#    "a" : 4,
#    "b" : 5,
#    "c" : 7
#}
#print(len(dick))
#for i in dick.values():
 #    print(i)
#for i,y in dick.items():
#    print(i, y)


#subject = {
#    'algebra' : 88,
#    'inglish' : 81,
#    'biologi' : 90
#}
##print(subject.values())
#
#counter = 0
#for i in subject.values():
#    counter += i
#
#print(counter / len(subject))


#q = int(input('в ведите число: '))
#w = 1
#for i in range(2, q+1):
#    w = w * i
#print(w)


#lists = [1, 2, 3]
#lists.pop(2)


#subject = {
#    'algebra' : 88,
#    'inglish' : 81,
#    'biologi' : 90
#}
#a = subject.pop('algebra')
#print(a)
#print(subject)



#new_subj = {
#    'python' : 100,
#    'java' : 78
#}
#subject.update(new_subj)
#subject.update({'geograf': 56})
#print(subject)

#new = dict.fromkeys(['a', 'b'])
#rint(new)

#lists = ['samat', 'nazik', 'erlan', 'bael']
#s = dict.fromkeys(lists, 50000)
#s['samat'] = 60000
#print(s)

#s = {1: 3, 4: 5}
#print(s.get(1))
#print(s.get(8), 'no key')


#s = {1: 3, 4: 5}
#print(s.setdefault(5))
#print(s)


#n  = {
#    'user' : {
#        "name" : "loli",
#        "surname" : 'POli',
#        'age' : 19,
#    },
#    "user1" : {
#        "name" : 'poli',
#        'surname' : 'joli'
#    }
#}
#
#print(n.get('user1').get('name'))
#
#x = n.copy()
#x = n
#n['user3'] = {'name' :'lopu'}
#print(n)


compal = {
    1: {
        '1name' : 'Beka',
        '1surn' : ' Molli',
        'age' : 45,
        '1rabota' : 'mehanik',
        'zarik' : 550
    },
    2: {
        '2name': 'Beka',
        '2surn': ' Molli',
        'age': 12,
        '2rabota': 'mehanik',
        'zarik': 550
    },
    3: {
        '3name': 'Beka',
        '3surn': ' Molli',
        'age': 76,
        '3rabota': 'mehanik',
        'zarik': 550
    },
    4: {
        '4name': 'Beka',
        '4surn': ' Molli',
        'age': 16,
        '4rabota': 'mehanik',
        'zarik': 550
    },
    5: {
        '5name': 'Beka',
        '5surn': ' Molli',
        'age': 37,
        '5rabota': 'mehanik',
        'zarik': 550
    },
}

for i in compal:
    if compal[i]['age'] >= 20:
        print(compal[i])

