from read import lands
def update_availability_file(kitta_no,availability):
    updated_data = []
    data =lands()
    for line in data:
        if int(line[0])==kitta_no:
            line[-1] = availability
        updated_data.append(','.join(line))
    with open("land.txt","w") as file:
        file.write("\n".join(updated_data))
    
  