mylist = [1,2,3]
duplist = mylist # Assigning reference of mylist to duplist
mylist = 'Koushik' # Changing reference

print(f'This is mylist {mylist}')
print(f'This is duplist {duplist}')
print('--------------------------')

mylist = [1,2,3]
mylist[0] = 69

print(f'This is mylist {mylist}')
print(f'This is duplist {duplist}')
print('--------------------------')

list1 = [1,2,3]
list2 = list1 # Assigning reference of list1 to list2

print(f'This is list 1 {list1}')
print(f'This is list 2 {list2}')
print('--------------------------')

list1[0] = 56

print(f'After changing 0th element of list 1 {list1}')
print(f'List 2 {list2} printing same value because list 2 have reference of list 1')
print('--------------------------')

l1 = [1,2,3]
l2 = l1[:] # Copying

print(f'This is L1 {l1}')
print(f'This is L2 {l2}')
print('----------------------')

l1[0] = 66

print(f'After changing L1 {l1}')
print(f'L2 value remains same as previous {l2}')
print('--------------------------')

ls1 = [1,2,3]
ls2 = ls1 # Assigning reference of ls1 to ls2

print(f'List 1 {ls1}')
print(f'List 2 {ls2}')
print(f'({ls1 is ls2}) this give us true because List 1 & List 2 have same reference') 
print('--------------------------')

ls1 = [1,2,3]
ls2 = [1,2,3]

print(f'List 1 {ls1}')
print(f'List 2 {ls2}')
print(f'({ls1 is ls2}) because List 1 & List 2 have diffrent reference') 
print('------------ END --------------')