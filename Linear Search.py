items = ["Mohamed", "Ahmed", "Ali","Gaber","Fathy","Omar","Sayed","Hassan","Raouf"]
print ("List items are: " , items )
print ("please type the name you want to search for: ")
ele=input ()

# You can switch between 2 methods of linear search, change the switch value to select method 1 or 2
switch =2
if switch ==1:
    loc = -1
    for i in range (len(items)-1):
        if (ele == items[i]):
            loc=i
    if (loc>=0):
        print(ele,"found in location [",loc,"]")
    else:
        print(ele,"not found")

  
if switch==2:
    if ele in items:
        loc = items.index(ele)
        print(ele,"is found in location [",loc,"]")
    else:
        print("Sorry,",ele,"is not found!")

input("Program has completed")
