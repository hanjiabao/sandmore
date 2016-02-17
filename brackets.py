brackets = "[[][][][][][]]"
def brackets_ok(brackets):
    if brackets == "":
        print "OK"
    else:
        i = 0
        for b in brackets:
            if i < 0:
                print "NOT OK"
                return 0
            print b
            if b == "[":
                i = i + 1
            else:
                i = i - 1
        if i == 0:
            print "OK"

if __name__=="__main__":
    brackets_ok(brackets)
