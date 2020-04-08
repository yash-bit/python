'''
friend = 0
can_message = "Message allowed" if friend else "Message not allowed"
print(can_message)
'''
is_magician = 0
is_expert = 1

if is_magician and is_expert:
    print("You are an expert")

elif is_magician and not(is_expert):
    print(" Atleast you are trying")

elif not(is_magician) and is_expert:
    print("You need magic")   

