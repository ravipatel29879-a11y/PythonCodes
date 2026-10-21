stationery = []


def add():
    sid = int(input("Enter SID: "))
    sname = input("Enter Stationery name: ")
    price = int(input("Enter Stationery Price: "))

    d1 = {
        "SID": sid,
        "SName": sname,
        "Price": price
    }

    stationery.append(d1)
    print("Stationery added successfully!")


def display():
    print("==============================================")
    print("SID\tStationery Name\t\tPrice")
    print("==============================================")

    if not stationery:
        print("No stationery available.")
        return

    for s1 in stationery:
        print(s1["SID"], "\t", s1["SName"], "\t\t", s1["Price"])


def search():
    sid = int(input("Enter SID: "))
    found = 0

    for s1 in stationery:
        if s1["SID"] == sid:
            found = 1
            break

    if found == 1:
        print("Stationery is found")
        print("==============================================")
        print("SID\tStationery Name\t\tPrice")
        print("==============================================")
        print(s1["SID"], "\t", s1["SName"], "\t\t", s1["Price"])
    else:
        print("Not found")


def updateName():
    sid = int(input("Enter SID which name you want to change: "))
    found = 0

    for s1 in stationery:
        if s1["SID"] == sid:
            found = 1
            break

    if found == 1:
        print("Stationery is found")

        sname = input("Enter New Stationery name: ")
        s1["SName"] = sname

        print("Stationery name updated successfully!")
        print("==============================================")
        print("SID\tStationery Name\t\tPrice")
        print("==============================================")
        print(s1["SID"], "\t", s1["SName"], "\t\t", s1["Price"])

    else:
        print("Not found")


def deletebySID():
    sid = int(input("Enter SID which you want to delete: "))
    found = 0

    for s1 in stationery:
        if s1["SID"] == sid:
            stationery.remove(s1)
            found = 1
            print("Stationery deleted successfully!")
            break

    if found == 0:
        print("Not found")


def sortByPrice():
    if not stationery:
        print("No stationery available to sort.")
        return

    stationery.sort(key=lambda x: x["Price"])

    print("Stationery sorted by price successfully!")
    display()