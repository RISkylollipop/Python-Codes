condition = "";
start = False;
while True:
    condition = input("> ").lower()
    if condition == "start":
        if start:
            print('Car already Started')
        else:
            start = True;
            print('The car Started...')
    elif condition == "stop":
        if not start:
            print('Car is Stopped Already')
        else:
            start = False
            print('The car stopped')
    elif condition == "help":
        print("""
Start - To Start the Car.
Stop - To stop the Car.
Quit - To Quit Car Operation.
""")
    elif condition == "quit":
        break;
    else:
        print("I don't Understand Your Request");
    