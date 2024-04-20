from read import lands
def kitta_exist(kitta_no,for_rent):
    data =lands()
    for kitta in data:
        if int(kitta[0])==kitta_no:
            if for_rent:
                if kitta[5].strip()=="Not Available":
                    print("************** Land is not available ***************")
                    return False
            else:
                if kitta[5].strip()=="Available":
                    print("************** Land is already available if you want to return book first ***************")
                    return False
            return True
    return False
