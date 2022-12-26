is_magican = False
is_expert = False

# check if magican AND expert:
# Print "You are a master magic"

# check if magician but not expert:
# Print "at least you are getting there"

# check if not magicain:
# Print: You need magic powers

if is_magican and is_expert:
    print("You are a master magician")
elif is_magican and not is_expert:
    print("at least you are getting there")
elif not is_magican:
    print("You need magic powers")
