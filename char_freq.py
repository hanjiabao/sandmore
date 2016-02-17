string = "abbabcbdbabdbdbabababcbcbab"
def char_freq(string):
    if string is None:
        return None
    else:
        char = {}
        for s in string:
            i = 0
            for c in string:
                if s == c:
                    i = i + 1
                    char2 = {s:i}
                    char = dict(char, **char2)
        print char
if __name__=="__main__":
    char_freq(string)
