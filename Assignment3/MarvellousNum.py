def chkprime (num): 
    if num > 1:
        for i in range(2, num):
            if num % i == 0:   
                return 0
                break
        else:
            return 1
    else :
        return 0

    