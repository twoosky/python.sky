decimal = 13

result = ""

while True:
    a = decimal%2 # 1 or 0 : 맨 앞에 추가될 숫자
    result = str(a)+result
    decimal = decimal//2
    if decimal == 0: break

print(result)
