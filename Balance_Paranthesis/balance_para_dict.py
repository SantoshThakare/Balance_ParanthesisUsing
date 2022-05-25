class Stack:
    def __init__(self):
        self.element = []

    def empty(self):
        return self.element == []

    def push(self, item):
        self.element.append(item)

    def pop(self):
        return self.element.pop()

    def check(self, lst):

        d = {'(': ')', '{': '}', '[': ']'}
        for item in lst:
            if item == '(' or item == '{' or item == '[':
                Stk.push(item)
            elif item == ')' or item == '}' or item == ']':
                value = Stk.pop()
                if d[value] != item:
                    return 'Not Balanced'
            else:
                continue
        if Stk.empty():
            return 'Balanced'
        else:
            return 'Not Balanced'


if __name__ == '__main__':

    Stk = Stack()
    lst = list(input())
    print(Stk.check(lst))

