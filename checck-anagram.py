# Check if two strings are anagrams
a = input("Enter string1: ")
a1 = input("Enter string2: ")

f = {}

if len(a) == len(a1):
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    for i in a1:
        if i in f:
            f[i] -= 1
            if f[i] < 0:
                print(f"{a} and {a1} are not anagrams")
                break
        else:
            print(f"{a} and {a1} are not anagrams")
            break
    else:
        print(f"{a} and {a1} are anagrams")
else:
    print(f"{a} and {a1} are not anagrams")
    

'''
Enter string1: tea
Enter string2: eat
tea and eat are anagrams
'''
