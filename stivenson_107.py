def find_gcf(x, y):
    if y == 0:
        return x
    else:
        return find_gcf(y, x % y)


first_num = int(input('write first numerator '))
second_num = int(input('write first denominator '))
nod = find_gcf(first_num, second_num)
# print('НОД РАВЕН =', find_gcf(first_num, second_num))
while True:
    if first_num % nod == 0 and second_num % nod == 0:
        first_num, second_num = int(first_num / nod), int(
            second_num / nod)
    else:
        print('new numerator =', first_num)
        print('new denominator =', second_num)
        break



