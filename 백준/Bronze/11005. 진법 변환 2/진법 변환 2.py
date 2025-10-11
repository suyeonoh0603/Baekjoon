N, B = map(int, input().split())
A = ''
digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N>0 :
    A = digit[N%B] + A
    N = N // B

print(A)