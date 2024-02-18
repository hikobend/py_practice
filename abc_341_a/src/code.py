# aに入力された回数分01を出力する
def show_number(a: int) -> str:
    result: str = ""
    for i in range(a):
        result += "01"
    result += "1"
    return result
