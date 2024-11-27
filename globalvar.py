phrase = "Let it be"


def global_printer():
    print(phrase)



global_printer()
print(phrase)



phrase = "Hey Jude"

global_printer()


def printer():
    local_phrase = "Yesterday"

    print(local_phrase) 

printer()


print(local_phrase)