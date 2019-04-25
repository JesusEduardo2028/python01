def centre_text(*args):
    """OLD WAY
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)
    """
    """Comprenhension list way"""
    text = " ".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text("first", "second", "spam", 1, 2, 3 , 40000.0)
