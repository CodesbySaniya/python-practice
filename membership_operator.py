#membership operator

# use to check whether valiue is in or not in collection(list,set,dict,tuple)

name = "saniya"
guess = input("enter your guessed letter for a correct word: ")

if guess in name:
 print(f"letter found {guess}")
else:
  print("letter not found")

my_dict = {"A" : 1 ,"B" : 2 , "C" : 3}

grade = input("enter the grade:").upper()

if grade in my_dict:
  print(f"{grade} will get {my_dict[grade]} rank")
else:
  print("you failed the exam")


# Write a program that asks the user to enter a word and prints only the vowels present in that word.

word = input("enter the word: ")
count =0
for letter in word:
  if letter in "aeiou":
    print(letter)
    count+=1
print(f" Total number of vowel in word  {count}")

