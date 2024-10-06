
s = str(input("Nhập 1 chuỗi:"))

def NegativeNumberInStrings(s):
    negativeNumber = []
    for i in range(len(s)):
        if s[i] == "-":
            number = ""
            for j in range(i+1, len(s)):
                if s[j].isdigit():
                    number += s[j]
                else:
                    break
            if number != "":
                negativeNumber.append(int(number)*-1)
    return negativeNumber

print(NegativeNumberInStrings(s))