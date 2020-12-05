class Solution:
    def addBinary(a: str, b: str) -> str:
        if len(a) < len(b):
            a,b = b,a
        i = len(a) - 1
        j = len(b) - 1
        a = list(a)
        b = list(b)

        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) > 1 and i >= 1:
                a[i - 1] = str(int(a[i - 1]) + 1)
                if int(a[i - 1]) > 2:
                    a[i] = "1"
                    a[i-1] = str(int(a[i-1]) - 1)
                else:
                    if int(a[i]) + int(b[j]) == 2:
                        a[i] = "0"
                    else:
                        a[i] = str(int(a[i]) - 1)
            elif int(a[i]) + int(b[j]) > 1 and i == 0:
                if int(a[i]) + int(b[j]) > 2:
                    a[i] = "1"
                    a.insert(i,str(int(a[i]) + int(b[j]) - 1))
                else:
                    a[i] = str(int(a[i]) - 1)
                    a.insert(i,1)
            elif int(a[i]) + int(b[j]) <= 1:
                a[i] = int(a[i]) + int(b[j])
            i -= 1
            j -= 1
        if j < 0:
            while(i > 0):
                if int(a[i]) > 2:
                    a[i - 1] = str(int(a[i - 1]) + 1)
                    if int(a[i - 1]) > 2:
                        a[i] = "1"
                        a[i - 1] = str(int(a[i - 1]) - 1)
                    else:
                        a[i] = str(int(a[i]) - 1)
                if int(a[i]) > 1:
                    a[i - 1] = str(int(a[i - 1]) + 1)
                    if int(a[i - 1]) > 2:
                        a[i] = "1"
                        a[i - 1] = str(int(a[i - 1]) - 1)
                    else:
                        a[i] = "0"
                i -= 1
            if i == 0 and int(a[i]) > 1:
                a[i] = "0"
                a.insert(i,1)
            return "".join('%s' %i for i in a)
        elif i < 0:
            a = b[:j] + a
            return "".join('%s' %i for i in a)

print(Solution.addBinary("110111","101"))

