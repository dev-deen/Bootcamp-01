def multiples(n,limit):
    result=set()
    for i in range(1,limit+1):
        result.add(n*i)
    return result

def lcm(x,y):
    limit=x*y
    multiples_x=multiples(x,limit)
    multiples_y=multiples(y,limit)
    common=multiples_x.intersection(multiples_y)
    return min(common)
print(lcm(6,8))