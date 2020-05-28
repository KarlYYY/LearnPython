numbers = list(range(1,11,2))
print(numbers)

squares = []
for value in numbers:
    square = value**2
    squares.append(square)

print(squares)

digits = [1,2,3,4,5,6,10,200,333]
print(str(min(digits)) + ' ' +  str(max(digits)) + ' ' + str(sum(digits)))

squares = [value**3 for value in range(1,7)]
print(squares)

for value in list(range(1,10,1)):
    print(str(value) + '\n')

name = ['Kidd','Belle','Harry','A','B']
print(name[0:2])
print(name[:3])
print(name[1:])
print(name[-2:])
print(name[-1])
# slice copy
name_backup = name[:]
name_backup.append('C')
print(name_backup)
# 直接赋值会关联两个list
name_backup = name
name_backup.append('D')
name_backup.append('E')
print(name)
