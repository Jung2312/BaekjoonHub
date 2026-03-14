def solution(code):
    mode = 0
    ret = []

    for idx, c in enumerate(code):
        if c == "1":
            mode = 1 - mode
        else:
            if mode == 0 and idx % 2 == 0:
                ret.append(c)
            elif mode == 1 and idx % 2 == 1:
                ret.append(c)

    result = "".join(ret)
    return result if result else "EMPTY"