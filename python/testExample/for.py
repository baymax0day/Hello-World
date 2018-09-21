
def test(x):
    #print(x)
    if int(x) % 3 == 0:
        exit()
        return False
    else:
        return True

if __name__ == "__main__":
    a = ["1","2","3","4","0","5","6","7","0","8","9"]
    for i in a:
        try:
            print(10/int(i))
            #test(i)
        except Exception as msg:
            print(msg)
            continue
            #break
    exit()
#    with open("dnf") as f:
#        line = f.readlines()
#        index = 0
#        proxy = 0
#        while index < len(line):
#            for i in line[index:]:
#                index = index + 1
#                if not test(i):
#                    #index = index - 1
#                    proxy = proxy+1
#                    break
#        print proxy
