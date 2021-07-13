        s=input()
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} #first we store values of roman into hashmaps
        res, tmp = 0, 0
        for i in reversed(s):
            if dic[i]>=tmp:
                res=res+dic[i]
            else:
                res=res-dic[i]
            tmp=dic[i]
        return res
