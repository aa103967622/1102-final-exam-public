def p00(n=0):
    even=None
    # ↓程式區域↓
    n = int(input("請輸入一個整數: "))

    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

    print("輸出結果:", is_prime)
    # ↑程式區域↑
    return even
