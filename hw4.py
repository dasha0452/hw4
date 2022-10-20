print('enter a number: ')
n = int(input())
print('enter a number system: ')
cc = int(input())

def perevod(n):
    res = ''
    while n > 0:
        res = str(n % cc) + res
        n = n // cc
    return res
print(n, '-->', perevod(n))