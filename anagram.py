w1 = input(" Enter first word :")
w2 = input(" Enter Second word :")
if sorted(w1.lower()) == sorted(w2.lower()):
    print("Anagram ")
else :
    print("Not Anagram ")
