def hello():
    print("Hello!")

def bye():
    print("Bye!")

commands = {"hello": hello, "bye": bye}

cmd = input("command (hello/bye): ")
commands[cmd]()