if __name__ == '__main__':
    N = int(input())
    a = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        print(cmd)
        args = s[1:]
        print(args)
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("a."+cmd)
        else:
            print(a)