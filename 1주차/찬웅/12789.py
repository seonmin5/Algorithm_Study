n = int(input())
numbers = list(map(int, input().split()))

stack = []
order = 1
for number in numbers:
    while stack and stack[-1] == order:
        stack.pop()
        order += 1
        print("stackpop", stack)
        print("order", order)
    
    if number == order:
        order += 1
        print("order", order)
    else:
        stack.append(number)
        print("stack", stack)

while stack and stack[-1] == order:
    stack.pop()
    order += 1

if order == n + 1:
    print("Nice")
else:
    print("Sad")