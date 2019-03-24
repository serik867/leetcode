def reverse(x):
    flag = False

    if x<0:
        flag= True
        x = x*-1

    result = int(str(x)[::-1])*-1 if flag else int(str(x)[::-1])

    if result not in range(-2**31,2**31):
        return 0
    else:
        return result


s=1234
t=43456
p=234234523423423423423423424234234234234234234234234253644564676756

print(reverse(s))
print(reverse(t))
print(reverse(p))