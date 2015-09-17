def standardPick():
    num = int(input("Which standard do you want to check? 1 = UPC, 2 = ISBN-10, 3 = ISBN-13 "))
    if num == 1:
        UPC()
        
def UPC():
    upcCode = int(input("Type your barcode here: "))
    for upcCode in range (6):
        print(str(upcCode))

standardPick()
UPC()
        
    
    
    
        
    
        
    
