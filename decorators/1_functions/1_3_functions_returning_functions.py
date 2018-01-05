"""
Now the fun part...

You’ve seen that functions are objects. Therefore, functions:

- can be assigned to a variable
- can be defined in another function

That means that a function can return another function.
"""


def get_talk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize() + "!"

    def whisper(word="yes"):
        return word.lower() + "..."

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = get_talk()

# You can see that "talk" is here a function object:
print(talk)
# outputs : <function get_talk.<locals>.shout at 0x102287268>

# The object is the one returned by the function:
print(talk())
# outputs : Yes!

# And you can even use it directly if you feel wild:
print(get_talk("whisper")())
# outputs : yes...

# If you can return a function, you can pass one as a parameter:


def scream(word="yes"):
    return word.capitalize() + "!"


def do_something_before(func):
    print("I do something before then I call the function you gave me")
    print(func())

do_something_before(scream)
# outputs:
# I do something before then I call the function you gave me
# Yes!
