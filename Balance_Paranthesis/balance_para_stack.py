def bracket_balance(exp):
    stack = []
    for ch in exp:
        if ch in ["(", "{", "["]:
            stack.append(ch)
        else:
            if not stack:
                return False
            current_item = stack.pop()
            if current_item == "(":
                if ch != ")":
                    return False
            if current_item == "{":
                if ch != "}":
                    return False
            if current_item == "[":
                if ch != "]":
                    return False

        if stack:
            return False
        return True


if __name__ == '__main__':

    exp = ["[{{}]"]

    if bracket_balance(exp):
        print("Balance")
    else:
        print("Unbalance")
