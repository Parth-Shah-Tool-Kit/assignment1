#You are given a large integer represented as an integer, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.


x = int(input("Enter the number: \n"))

def increment(number):
    arr = []
    while True:
        arr.append(number%10)
        number = number // 10
        if number == 0:
            break
    arr = arr[::-1]
    arr[-1] = arr[-1] + 1
    return arr


print("The incremented numebr is: ")
print(increment(x))
