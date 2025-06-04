while True:
    age=int(input("enter your age:"))
    print(age)
    try:
        if age<18:
            raise AgeValidationError(age)
            continue
        else:
            print("valid age")
            break
    except:
        print("age is not valid")