school_records={
'personal_info':
{"kid": {"tom": {"class": "intermediate", "age": 10},
"sue": {"class": "elementary", "age": 8}
},
"teen": {"joseph": {"class": "college", "age": 19},
"marry": {"class": "high school", "age": 16}
},
},
'grades_info':
{"kid": {"tom": {"math": 88, "speech": 69},
"sue": {"math": 90, "speech": 81}
},
"teen": {"joseph": {"coding": 80, "math": 89},
"marry": {"coding": 70, "math": 96}
},
},
}
print(list(school_records["grades_info"]["teen"]["joseph"].items()))
print(school_records["grades_info"]["teen"]["joseph"])
 
school_records={
"personal_info":
{"kid": {"tom": {"class":"intermediate", "age":10},
"sue": {"class":"elementary", "age":8}
},
"teen" : {"joseph" : {"class":"college", "age" : 19},
"marry": {"class":"high school", "age":16}
},
},
}
print(school_records['personal_info']['teen']['marry']['age'])

friends = {
"friend1" : {"first" : "Sue", "last" : "Bold"}, 
"friend2" : {"first" : "Steve", "last" : "Smith"},
"friend3" : {"first" : "Sergio", "last" : "Tatoo"}
}
print(friends)

favourite = {
"friends" : {
"friend1" : {"first" : "Sue", "last" : "Bold"},
"friend2" : {"first" : "Steve", "last" : "Smith"},
"friend3" : {"first" : "Sergio", "last" : "Tatoo"}
},
"family" : {
"family1" : {"first" : "Mary", "last" : "Tisa"},
"family2" : {"first" : "Samuel", "last" : "Brown"},
"family3" : {"first" : "Tom", "last" : "Happy"}
}
}
print (favourite)

fruit = {'Apple', 'Orange', 'Banana' }

set_1 = {'red', 'blue', 'pink', 'red'}
colors = 'red', 'blue', 'pink', 'red'
set_2 = set(colors)
print(set_1)
print(set_2)

colors = 'red', 'blue' , 'pink', 'red'
type(colors)
set_2 = set(colors)
set_2

empty_set = set ()
print(type(empty_set))

bos_kume = {} # bos kume bu sekilde olusturulmaz !!! bu bir dictionary dir
type(bos_kume)

bos_kume = set()
type (bos_kume)

flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid' , 'rose' , 'orchid' ]
flowerset = set(flower_list)
flowerlist = list(flowerset)
print(flowerset)
print(flowerlist)

kumem = {1,2,2,3,3,3}
len(kumem)
kumem
len([1,2,2,3,3,3])
len({1,2,2,3,3,3})
a = {1,2,2,3,3,3}
a
set('claruswaaaaaayyyyyysssssss')

import string
alfabe = string.ascii_lowercase
alfabe

listem = list(alfabe)
print(listem)

print(set(listem))

import string
alfabe = string.ascii_lowercase
listem = list(alfabe)
print(listem)
print(set(listem))

kumem ={1,'1',1.0}
len(kumem)
{1,'1',1.0}

1 == '1'
1 == 1.0

id(1)
id(1.0)

id(1) == id(1.0)

a = 23
b = a

b

a == b
id(a)
id(b)
id(a) == id(b)
id(23) == id(a)

a = {'carnation' , 'orchid', 'rose' , 'violet' }
b = {'rose' , 'orchid' , 'rose' , 'violet' , 'carnation' }

a = {1,2,3,4}
a

hash(5)

hash('abc')
hash((1,2,3,4))

a = {(1,2,3),'ali','ahmet'}
a

a = {1,2,3}
a.add(4)
a
a.add(5)
a
a.add('alti')
a
a.discard(2)
a
a.discard(8)
a
a
a.remove(3)
a
a
a.pop()
a

a = set('philadelphia')
b = set('dolphin')

a = set('philadelphia')
print(a)

b = set('dolphin')
print(b)

print(a - b)
print(a.difference(b))

print(b - a)
print(b.difference(a))

A = {1,2,3,4,5}
B = {4,5,6,7}

print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

A.difference(B)
B.difference(A)

A-B
A.intersection(B)

A & B
A.union(B)

A|B

a = set('05/21/2022')
b = {'05/21/2022'}
print(a)
print(b)

tarih = '04/01/2023'

set1 = {tarih}
set2 = set(tarih)
print('Set 1 in ciktisi', set1)
print('Set2 nin ciktisi', set2)

given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]
unique = set(given_list)
print(unique)

listem = [1,2,2,3,3,3,3,4,4,4,5,5]
uniqe_elemanlar = list(set(listem))
print(uniqe_elemanlar)

mytuple = tuple(listem)
mytuple
{mytuple}

A = set("Wellingthon")
B = set ("Washinghton")
print(A&B)
print(A|B)
print(A-B)

a = set("washington")
b = set("wellington")
print(a-b)
print(b-a)
print(a & b)
print(a|b)

usa_capt = set('Washington' )
nz_capt = set('Wellington')
print(usa_capt)
print(nz_capt)
print(usa_capt - nz_capt)
print(usa_capt.difference(nz_capt))
print(nz_capt - usa_capt)
print(nz_capt.difference(usa_capt))
print(nz_capt & usa_capt)
print(nz_capt.intersection(usa_capt))

if True:
    print('it is true')

if True:
    print('If blogu calisti')

if True:
    print('If blogu calisti')

if True:
    print('If blogu calisti')

if 5:
    print('If blogu calisti')

bool(5)

if 'False':
    print('If blogu calisti')

bool('False')

if [[]] :
    print('If blogu calisti')

bool ( [[]])

a = 5
b = 7

5<7

if a<b:
    print('If blogu calisti')
print('Bu her halukarda calisir')

if '0':
    print('If blogu calisti')
print('Bu her halukarda calisir')

bool('0')

if 0 or "False" and None :
    print("hello universe")

if -1 :
    print("hello")

minced = True
h_bread = True
lettuce = True
pepper = True
g_store = True

hamburger = minced and h_bread and g_store and(pepper or lettuce)

if hamburger:
    print( 'Bon Appetid')

x = (4,6,8)
print(type(x))

x = ([4,6,8] )
print(type(x))

a = ('abc')
type(a)

a = ([1,2,3])
type(a)

a = ([1,2,3], )
type(a)

x = (5+3j)
print(type(x))

type(3+4j)

x = ([4,6,8], )
print(type(x))

x = (5+3j, )
print(type(x))

t = ('foo', 'bar', 'baz' )

a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9) [1 :: 3]

set1 = set ("TWELVE PLUS ONE")
set2 = set ("ELEVEN PLUS TWO")

if set1 == set2:
    print("We are the same!")

x = 6
y = 9

print("is x equal to y?:" , x == y)
print("is x not equal to y?:", x != y)
print("is x less than y?:",x < y)
print("is x greater than y?:", x > y)
print("is x less than or equal to y?:", x <= y)
print("is x greater than or equal to y?:", x >= y)

2 == 2 
2 == 3 
2 != 2 
2 != 3
3 > 2 
2 > 3
2 < 3
3 < 2
3 >= 2
3 >= 3
2 >= 3
3 <= 2
3 <= 3
2 <= 3

print(1 == 1)
print("henry" == "Henry")
print(12 < 12.1)
print("hard" != "easy")

empty_seat = 14
if empty_seat > 3: # in this case, 14>3=True, so the body will execute
    print('there is still seat to sit')

minced = True
bread = True
lettuce = False
pepper = True
grocer = True
hamburger = (minced and grocer and bread) and (lettuce or pepper)

if hamburger :
    print("Bon Appetit")

set1 = set('twelve plus one')
set2 = set('eleven plus two')

if set1 == set2 :
    print('We are the same')

set1 = set('twelve plus one' ) 
set1

set2 = set('eleven plus two')
set2

# input()

# input('Yes veya No diye bir girdi yaziniz : ')

# girdi = input('Yes veya No diye bir girdi yaziniz : ')

# girdi

# a = input(' Bir sayi giriniz : ')
# b = input('Ikinci sayiyi giriniz : ')

# a + b

# type(a)
# type(b)

# a = int(input('Bir sayi giriniz : '))
# b = int(input('Ikinci sayiyi giriniz : '))

# cevap = input('Yes veya No degeri girin')

# input('Yes veya No degeri girin : ') == 'Yes'
# input('Yes veya No degeri girin') == 'Yes'
# input('Yes veya No degeri girin : ').title() == 'Yes'
# input('Yes veya No degeri girin : ').lower() == 'yes'
# input('Yes veya No degeri girin : ').lower() == 'yes'
input('Yes veya No degeri girin : ').lower().strip() == 'yes' 