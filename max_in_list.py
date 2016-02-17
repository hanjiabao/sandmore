num = [123, 234, 65, 345, 53, 232, 766, 323]
def max_in_list(num):
    def max(x, y):
        if x >= y:
            return x
        return y
    print reduce(max,num)
if __name__=="__main__":
    max_in_list(num)
