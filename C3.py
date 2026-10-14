def decimal_to_binary(num):
    left=""
    while num>0:
        
        left=str(num%2)+left
        num=num//2
    return left
