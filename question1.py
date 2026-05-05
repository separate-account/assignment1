def problem1(string):
    string = string.lower()
    string_1 = string + string
    l = [i for i in string_1]
    # print(l)
    for i in range(a := 0, n := len(string)):
        b = []
        c = 0
        for j in range(i, min(i + n, i + 26)):
            if ((s := l[j]) in b):
                break
            else:
                b.append(s)
                c += (ord(s) - ord("a") + 1)
                a = max(a, c)

    print(a)

string = input("Enter a string: ")
problem1(string)
