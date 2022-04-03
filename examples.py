from equiv import equiv


def p_(p):
    return p


def id1(p):
    return p and True


def id2(p):
    return p or False


def implies1(p, q):
    return (not p) or q


def implies2(p, q):
    return (p and q) or (not p)


def s1(p, q):
    return not (p or q)


def s2(p, q):
    return (not p) and (not q)


def s3(p, q):
    return not implies1(p, q)


def s4(p, q):
    return p and (not q)


def s5(p, q, r):
    return ((not p) and (not q) and (not r)) or ((not p) and (not q) and r) or (p and q and (not r)) or (p and q and r)


def s6(p, q):
    return ((not p) and (not q)) or (p and q)


def tautology1(p):
    return p or (not p)


def tautology2(p, q):
    return (p or (not p)) and (q or (not q))


def contradiction1(p):
    return (not p) and p


def contradiction2(p, q):
    return not ((not ((not p) and p)) or (not ((not q) and q)))


def t1():
    return True


def t2():
    return not False


def nt1():
    return False


def nt2():
    return not True


def main():
    # Examples
    print(equiv(p_, id1)) # True
    print(equiv(p_, id2)) # True
    print(equiv(implies1, implies2)) # True
    print(equiv(s1, s2)) # True
    print(equiv(s3, s4)) # True
    print(equiv(s5, s6)) # True
    print(equiv(tautology1, tautology2)) # True
    print(equiv(contradiction1, contradiction2)) # True
    print(equiv(tautology1, contradiction1)) # False
    print(equiv(t1, t2)) # True
    print(equiv(t1, t2, nt1)) # False
    print(equiv(nt1, nt2)) # True


if __name__ == '__main__':
    main()
