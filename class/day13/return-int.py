string = input()
num1_str, op, num2_str = string.split()
num1, num2 = int(num1_str), int(num2_str)
if op == '+': result = num1 + num2
elif op == '-': result = num1 - num2
elif op == '*': result = num1 * num2
elif op == '/':
    q = num1 // num2
    remainder = num1%num2 
    result =[q,remainder]
else:
    result = "Invalid"
print(result)

