list = input('Enter the numbers ')
list = list.split()

for i in range(len(list)):
    list[i]= int(list[i])

print('The sum of the numbers is '+str(sum(list)))