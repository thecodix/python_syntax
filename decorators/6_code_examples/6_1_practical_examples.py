"""Now the big question: What can I use decorators for?

Seem cool and powerful, but a practical example would be great.
Well, there are 1000 possibilities.

Classic uses are extending a function behavior from an external lib (you can't modify it),
or for debugging (you don't want to modify it because it’s temporary).

You can use them to extend several functions in a DRY’s way, like so:
"""

import time
from urllib.request import urlopen


def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.clock()-t))
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("{0} {1} {2}".format(func.__name__, args, kwargs))
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print(reverse_string("Able was I ere I saw Elba"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, "
                     "snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, "
                     "a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo,"
                     " cash, a jar, sore hats, a peon, a canal: Panama!"))

# outputs:

# reverse_string ('Able was I ere I saw Elba',) {}
# wrapper 0.0
# wrapper has been used: 1x
# ablE was I ere I saw elbA

# reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura,
# maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana
# bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar,
# sore hats, a peon, a canal: Panama!',) {}
# wrapper 0.0
# wrapper has been used: 2x
# !amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,
# eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,
# inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,
# nalp a ,nam A


"""
Of course the good thing with decorators is that
you can use them right away on almost anything without rewriting.

DRY, I said:
"""


@counter
@benchmark
@logging
def get_random_futurama_quote():
    result = urlopen("http://subfusion.net/cgi-bin/quote.pl?quote=futurama").read()
    try:
        value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"


print(get_random_futurama_quote())
print(get_random_futurama_quote())

# outputs:
# get_random_futurama_quote () {}
# wrapper 0.02
# wrapper has been used: 1x
# The laws of science be a harsh mistress.
# get_random_futurama_quote () {}
# wrapper 0.01
# wrapper has been used: 2x
# Curse you, merciful Poseidon!
