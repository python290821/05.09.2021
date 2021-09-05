#name = input('please enter your name: ')
#print('hello', name)

#a,b,c = input('enter three numbers').split()

pizza = int(input('how manny pizza?'))
print('you ordered', pizza, 'slices')
kids = int(input('how manny kids?'))
full_slice_each_kid = pizza // kids
left_over = pizza % kids
print('each kid got', full_slice_each_kid, 'slices')
print('leftovers = ', left_over)

number = int(input('please enter a number 2 digits'))
asarot = number // 10
ahadot = number % 10
sum_digits = asarot + ahadot
print('the sum of digits=', sum_digits)

#print(a / b)
#print(9 // 4)

