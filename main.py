from read import display
from validator import kitta_exist
def main():
    print("\t ------------------------------------")
    print("\t |       Techno Property Land      |  ")
    print("\t ------------------------------------  ")
    keeprunning = True
    print("\t   WELCOME TO TECHNO PROPERTY LAND! ")

    name= input("    Enter you name: ")
    phonenumber = input("    Enter your cell number: ")
    while True:
        print("          Rent a Land   :     1")
        print("          Return a land  :    2")
        print("          Exit           :    3")
        number = int(input(" Enter your desired option: "))
        if number == 1:
            renting = True
            while renting == True:
                display()
                address= input("Enter your address:") 
                kn= int(input("Enter Kitta Number: "))
                while not kitta_exist(kn,True):
                    print("Your Kitta Number is not valid Please re-entered")
                    kn = int(input("Enter Kitta Number: "))

                months = int(input("Enter a the months for renting: "))
                p = input("Enter the purpose of the renting : ") 
                b= input("   Do you want to see more? ")
                if b == "no":
                    renting = False

                    
        elif number == 2:
            returning = True 
            while returning == True:
                display()
                kno= int(input(" Enter Kitta Number of the rented land : "))
                while not kitta_exist(kno,False):
                    print("Your Kitta Number is not valid Please re-entered")
                    kno = int(input("Enter Kitta Number: "))
                expected_month = int(input("Enter the expected rented month : "))
                actual_month = int(input("Enter  the actual month you have rented the land : "))
                a = input("   Do you want to continue ?")
                if a.strip() == "no":
                    returning = False

        elif number == 3:
            print("         -----------------------------------------")
            print ("         You are Exiting. Thank you for visiting!")
            print("         -----------------------------------------")
            break
        else :
            print(" Please enter a valid input ( 1 , 2 or 3) " )
main() 
                
                    
