match x := int(input()):
    case x if x < 425: print("Violet")
    case x if x < 450: print("Indigo")
    case x if x < 495: print("Blue")
    case x if x < 570: print("Green")
    case x if x < 590: print("Yellow")
    case x if x < 620: print("Orange")
    case x if x <= 780: print("Red")