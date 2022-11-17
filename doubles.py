from collections import Counter

out = []

def doubles(text):
    outpute = Counter(text)
    for i in outpute:
        print(len(i))
        if outpute[i] > 1:
            i = str(i) + "s"
            out.append(i)
        else:
            out.append(i)
    print(out)

doubles(["cow", "chair", "horse", "cow", "door", "cow"])