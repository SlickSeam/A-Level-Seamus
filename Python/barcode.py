def standardPick():
    num = int(input("Which standard do you want to check? 1 = UPC, 2 = ISBN-10, 3 = ISBN-13 "))
    print("")
    if num == 1:
        UPC()
    elif num == 2:
        ISBN10()
    elif num == 3:
        ISBN13()
        
def UPC():
    upcCode = input("Type your 12 digit barcode here: ")
    if len(str(upcCode)) != 12:
        print("")
        print("This is not a UPC Code, it does not have 12 digits")
        print("")
        UPC()        
    ans = 0
    num = 0
    for x in str(upcCode):
        num += 1
        if num %2 == 0:
            ans += int(x)*3
        else:
            ans += int(x)
    print("")
    if ans %10 == 0:
        print("This is a UPC Barcode")
    else:
        print("This is not a UPC Barcode")

def ISBN10():
    isbn10Code = input("Type your 10 digit barcode here: ")
    print(isbn10Code)
    if len(str(isbn10Code)) != 10:
        print("")
        print("This is not a ISBN-10 Code, it does not have 10 digits")
        print("")
        ISBN10()        
    ans = 0
    num = 10
    for x in str(isbn10Code):
        ans += int(x)*num
        num -= 1
    print("")
    if ans %11 == 0:
        print("This is an ISBN-10 Barcode")
    else:
        print("This is not an ISBN-10 Barcode")

def ISBN13():
    isbn13Code = input("Type your 13 digit barcode here: ")
    if len(str(isbn13Code)) != 13:
        print("")
        print("This is not a ISBN-13 Code, it does not have 13 digits")
        print("")
        ISBN13()        
    ans = 0
    num = 0
    for x in str(isbn13Code):
        num += 1
        if num %2 == 0:
            ans += int(x)*3
        else:
            ans += int(x)
    print("")
    if ans %10 == 0:
        print("This is an ISBN-13 Barcode")
    else:
        print("This is not an ISBN-13 Barcode")


    

standardPick()

        
    
    
    
        
    
        
    
