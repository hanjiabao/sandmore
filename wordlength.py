string = "i am a boy."
punctuation = [" ", ".", ".", "!", "?", ":", ";"]
#list punctuation could be added more punctuation if needed
def wordlength(string):
    if string is "":
        print 0
    else:
        i = 0
        j = 0
        char_length = []
        for s in string:
            if s in punctuation:
                char = string[j:i]
                print s, char, i, j
                char_length = char_length + [len(char)]
                j = i + 1
            i = i + 1
        print char_length

if __name__=="__main__":
    wordlength(string)
