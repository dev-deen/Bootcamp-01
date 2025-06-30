#Q4)Generate a Random PAssword:

def simple_random(seed):
    seed = (seed * 7 + 3) % 100
    return seed
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    seed = 1
    pwd = ""
    for i in range(length):
        seed = simple_random(seed + i)
        index = seed % len(chars)
        pwd += chars[index]
    return pwd
print("Password:", generate_password(8))
