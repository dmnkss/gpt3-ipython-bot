def splited_print(text):
    """
    Print prompt in lines
    """
    text = text.replace('\r', '\n')
    for i in range(0, 2):
        print('------------')
    print(text)
    for i in range(0, 2):
        print('------------')
