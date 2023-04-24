total = 0
for num in range(101):
    total = total + num
print('Total : ' + str(total))

evenNumbers = 0
for num in range(0, 100, 2):
    evenNumbers = evenNumbers + num
print('Total Even Numbers : ' + str(evenNumbers))

oddNumbers = 0
for num in range(1, 100, 2):
    oddNumbers = oddNumbers + num
print('Total Odd Numbers : ' + str(oddNumbers))
