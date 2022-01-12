print("Welcome to a COVIZ- A quiz game based on Covid-19 to increase awareness ")
print("Instructions: -Based on the statement appearing on the screen you will have to chose wheather that statement is a myth or fact about Covid-19 ")
print("Choose '1' for Myth")
print("Choose '2' for Fact")
score=0

statement_1="The ingredients in COVID-19 vaccines are dangerous."
print("statement 1---",statement_1)
a=int(input("Myth or Fact?"))
if a==1:
    print("HURRAY! You are Correct!!")
    score+=1
    print("Score= ", score)
else:
    if a==2:
        print("UHHOH! It is a Myth!! ")
    print("FACT: Nearly all the ingredients in COVID-19 vaccines are also ingredients in many foods – fats, sugars, and salts.")
    print("Score= ",score)


statement_2="COVID-19 vaccines can alter my DNA."
print("statement 2---", statement_2)
b=int(input("Myth or Fact?"))
if b==1:
    print("HURRAY! You are Correct!!")
    score += 1
    print("Score= ", score)
else:
    if b==2:
        print("UHHOH! It is a Myth!! ")
        print("FACT:COVID-19 vaccines do not change or interact with your DNA in any way.")
        print("Score= ", score)

statement_3="Drinking alcohol doesn’t cure or prevent COVID-19."
print("statement---3",statement_3)
c=int(input("Myth or Fact?"))
if c==1:
    print("UHHOH! It is a Fact!! ")
    score -= 1
    print("Score= ", score)
else:
    if c==2:
        print("HURRAY! You are Correct!!")
        score+=1
        print("Score= ",score)

if score==3:
    print("Congratulations!! You are well aware about Covid-19!!")
else:
    print("Hope we were able add to your awareness Covid-19!!")
    print("Thanks for playing!! ")












