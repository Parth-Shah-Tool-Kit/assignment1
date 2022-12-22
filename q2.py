# Implementing pow(x, n), which calculates x raised to the power n

x = int(input("Enter the base number"))
n = int(input("Enter the power"))


def power(base, power):
    ans = 1
    for i in range(power):
        ans = ans * base
    return ans

print("The requied answer is:")
print(power(x,n))
