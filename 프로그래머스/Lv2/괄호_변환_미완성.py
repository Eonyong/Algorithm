def solution(p):
    w, u = "", ""
    # 1
    if p:
        s, e = [], []
        for g in p:
            if g == '(':
                s.append(g)
            else:
                try:
                    e.append(s.pop())
                    e.append(g)
                except:
                    e.append(g)
        else:
            if not s:
                return p
    else:
        return w
    print(s, e)



solution(")(")
solution("()))((()")