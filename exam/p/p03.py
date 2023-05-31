def p03(x=123):
    reverse=None
    # ↓程式區域↓
 reverse=None
    # ↓程式區域↓
    x = int(input("請輸入整數 x: "))
    reverse = 0
    is_negative = False

    if x < 0:
        is_negative = True
        x = abs(x)

    while x > 0:
        digit = x % 10
        reverse = (reverse * 10) + digit
        x = x // 10

    if is_negative:
        reverse = -reverse
    print("輸出結果:", reverse)
    # ↑程式區域↑
    return reverse
