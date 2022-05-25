def check(exp):
    open_br = tuple('({[')
    close_br = tuple(')}]')
    map = dict(zip(open_br, close_br))
    queue = []

    for i in exp:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == '__main__':

    string = "{[]{()}}"
    print(string, "-", check(string))

    string = "((()"
    print(string, "-", check(string))
