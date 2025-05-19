str=(input("enter any string:"))
vowels="aeiouAEIOU"
count=sum(1 for char in str if char in vowels)
print(f"number of vowels in {str} are {count}")