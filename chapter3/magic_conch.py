import random
#Basically the eight ball exercise, but it's the magic counch from spongebob


# initiate program
# input question
# program will randomly return one of the
# following strings.
# Program can be exited
conchResponse = ["Maybe someday.","Nothing.","Neither.","I don't think so.","No.","Yes.","Try asking again.","[in a mocking tone] No!"]
amountOfResponse = len(conchResponse)
print("""You see a conch in the middle of the kelp forest. Being drawn to it, you pick it up.
      You notice a draw string, and on further inspection you notice the conch's opening is 
      covered in a dark metalic mesh. You pull the draw string, and from the conch's mesh a question emerges.
      
      
       /|
      <.->
     ;_.-'\   
    {    _.}_   
     \.-' /# `,
      \  |###/
       \ |##/
        \|_/
      """)

question = None
while(question != exit ):
    question = input("Magic Conch....")
    if(question == "exit"):
        print("""You proceed to put the magic conch back where you found, having had your questions more or less answered. You walk away""")
        break
    else:
        print(conchResponse[random.randint(0,amountOfResponse)])        
