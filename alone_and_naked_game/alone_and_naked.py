# This game is a WIP.
# TODO: Implement a prompt about the HINT, instead of explicity telling folks about hints.
print "You wake up in a forest alone and naked."
print "You have no recollection of how you got there, or even who you are."
print "You don't even know whether you're a male or a female. You better check."
print "Quick sidenote, you can type HINT during most of the prompts to receive a hint about what I'm looking for, because I'm probably going to be pretty finicky about the answers I expect you to give me and it's not like you can read my mind."
print "Let's check out what you are. I'll give you a free hint this time. Type 'Check Gender' into the prompt to see what you got down there."
gender_check = raw_input("> ")
if gender_check.lower() == "check gender":
    print "You check your gender, and seem rightly satisfied with the result."
else:
    print "Type 'check gender', like I told you to."
    gender_check = raw_input("> ")
    if gender_check.lower() == "check gender":
        print "You check your gender, and seem rightly satisfied with the result."
    else:
        print "Forget it. This game is going to be too hard for you."
        exit(1)
print "So what did you see down there? Was something hangin' around down there, or not? A simple 'Yes' or 'No' will suffice. If I receive anything different, I'm going to assume you're a man because you can't follow directions."
gender_confirm = raw_input("> ")
if gender_confirm.lower() == "no":
    print "You're a woman, congrats!"
else:
    print "Uh oh. You're a man."