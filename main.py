class AnybaseDecimal:
    def conversion(self, a, b):
        sum = 0
        i = 0
        while(a):
            sum += (a % 10) * b**i
            a = a//10
            i += 1
        return sum

a = int(input())
b = int(input())

object = AnybaseDecimal()
print(object.conversion(a, b))

"""You are given a number A. You are also given a base B. A is a number on base B.
You are required to convert the number A into its corresponding value in decimal number system.


Input
A = 1010
B = 2

Output
10
Input
A = 22 
B = 3

Output
8"""