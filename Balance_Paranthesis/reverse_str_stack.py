def create_stack():
    stack = []
    return stack


def size(stack):
    return len(stack)


def is_empty(stack):
    if size(stack)==0:
        return true


def push(stack,item):
    stack.append(item)


def pop(stack):
    if is_empty(stack):return
    return stack.pop()


def reverse(string):
    n= len(string)

    for i in range(0, n, 1):
        push(stack, string[i])

    string=""

    for i in range(0,n,1):
        string += pop(stack)
    return string


if __name__ == '__main__':
    stack = create_stack()
    string = "python"
    string = reverse(string)
    print("Reversed string is " + string)