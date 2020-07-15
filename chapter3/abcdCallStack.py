# Call Stack Notes

# based on a meandering conversation
#   Conversation flow as follows 
# Talk about your friend Alice
#   -But it reminds you of your buddy Bob
#     - Which requires a prior explanation of your couin carol
#   -Once done with you go back to the bob story 
# Return to alice story  
#    -Then remember it being linked to David, so you tell that story
# Once done, you finish the Alice story
# 
# Call Stack/example above visualised
# ------------------------------------------------------
#                                 |David|
#                      | Bob |    | Bob |   | Bob |               |David| 
#|____| ->  |Alice| -> |Alice|-> |Alice| -> |Alice|-> |Alice| -> |Alice| -> |Alice| -> |____|  

# Call Stack example but with functions
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
    
def b():
    print('b() starts')
    c()
    print('b() return')
    
def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() starts')
    print('d() returns')
    
a()

# Print statements as follow, pre-call
#  function a is called
#  function b is called
#  function c is called
#  function c is returned
#  function b is returned
#  function d is called
#  function d is returned
#  function a is returned

# Once call stack, but the statements have been printed
# a() starts
# b() starts
# c() starts
# c() returns
# b() return
# c() starts
# c() returns
# a() returns

# Got the function called I guess with AREPL, while just running it in Python 
# terminal gave me the above 


# Above example above visualised, as I understand it
# ------------------------------------------------------
#                            |c()|
#                     |b()|  |b()|  |b()|          |d()|            
#|____| ->  |a()|-> |a()|-> |a()|-> |a()|-> |a()|-> |a()|-> |a()|-> |____|  

# Above example above visualised, as the book lays it out
# ------------------------------------------------------
#                             |c()|
#                    |b()|   |b()|   |b()|             |d()|            
#|____| ->  |a()|-> |a()|-> |a()|-> |a()|-> |a()|-> |a()|-> |a()|-> |____|  