from read import display,get_price_location_area
from billing import billing
from validator import kitta_exist
from write import update_availability_file
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
                location,area,price = get_price_location_area(kn)
                total_price = int(price)*int(months)
                billing(name,kn,location,total_price,months,area,phonenumber)  
                update_availability_file(kn,"Not Available")
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
                location,area,price = get_price_location_area(kno)
                actual_price =  int(price)*int(actual_month)+(10/100)*(int(price)*int(actual_month))
                billing(name,kno,location,actual_price,actual_month,area,phonenumber)
                update_availability_file(kno,"Available")
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
                
                    
