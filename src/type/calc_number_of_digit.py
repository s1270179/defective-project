def calc_number_of_digit(num):

    cnt=0

    #整数判定関数
    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    for i in range)
    for s in reversed(str(num)):
        if is_int(s):
            cnt+=1
    
    return cnt
