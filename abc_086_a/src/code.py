def culc(a: int, b: int) -> str:
    if (a * b) % 2 == 0:
        return "偶数"
    elif (a * b) % 2 == 1:
        return "奇数"
    else:
        return "error"
