##############################check vowel#############################################
l = input("enter letter: ")
vowels = ('a', 'e', 'i', 'o', 'u')

if l.lower() in vowels:
    print("this letter "+l+" is vowel")
else:
    print("this letter "+l+" is not vowel")