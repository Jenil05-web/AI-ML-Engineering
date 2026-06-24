questions = ("Give name of 5th planet from sun ",
             "who is known as father of india ?",
             "how many UT are there ?",
             "what is the name of national bird of india ?",
             "hottest planet of solar system ") 

options = (("A.earth " , "B.mercury" , "C.venus " ,"D.saturn") ,
            ("A.abc" , "B.jha" , "C.kdjf " ,"D.adfa") , ("A.pp" , "B.xx" , "C.dd " ,"D.gg") ,
              ("A.aaaaaaaaa" , "B.dddddddd" , "C.ffffffff " ,"D.kjdfdjaf"))

answers = ("C" , "D" , "A" , "B")
guessed = []
score = 0
question_num = 0

for question in questions :
    print("--------")
    print(question)


for option in options:
 print(option)

 guess = input("Enter (A,B,C,D):").upper()
guess.append(guess)

if guess == answers[question]:
   score +=1
   print("CORRECT !")
else:
   print("INCORRECT !")
   print(f"{answers}")
questions +=1

print("______-----")
print("RESULTS")
print("-----------")

print("answers :" , end="")
for answer in answers:
   print(answer,end="")

   print()
 