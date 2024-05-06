table_title = {
    "kitta":"kitta Number",
    "address": "Address",
    "direction": "Land Direction",
    "anna": "Anna",
    "status": "Status",
    "price":"Price"
}
def lands():
    file = open("land.txt" , "r")
    data =[]
    for line in file.readlines():
        rows = (line.replace("\n" , "") .split(","))
        data.append(rows)
    file.close()
    return data


def display():
    data =lands()
    print(table_title["kitta"]+" "*(13 - len(table_title["kitta"]))+table_title["address"]+" "*(15 - len(table_title["address"])) +table_title["direction"]+ " "*(15- len(table_title["direction"]))+table_title["anna"]+ " "*(8 - len(table_title["anna"]))+table_title["price"]+ " "*(10 - len(table_title["price"]))+table_title["status"]+""*(15 - len(table_title["status"])))
    print("-"*80)
    for row in data :
       print(row[0]+" "*(12-len(row[0])) + row[1] +" "*(15 - len(row[1])) + row[2] + " "*(15- len(row[2]))+row[3] + " "*(8 - len(row[3]))+row[4] + " "*(10 - len(row[4]))+row[5])


def update_file(k_no):
    data =lands()
    # for kitta in data:
    #     if int(kitta[0])==k_no:
            
    # return False

def get_price_location_area(kitta_no):
    data =lands()
    for kitta in data:
        if int(kitta[0])==kitta_no:
            return kitta[1],kitta[3],kitta[4]
    return None,None,None