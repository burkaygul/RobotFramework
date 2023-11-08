myList = ["Burkay", 27, True, 3.0];

print(myList)

print(type(myList));
print(type(myList[0]));
print(type(myList[1]));
print(type(myList[2]));
print(type(myList[3]));

myList.append("wiseQuarter");
myList.append(2023);
myList.append(False);

print(myList)

if 27 in myList:
    print(f"yes")
else:
    print(f"no")


nums = [1,6,81,15];

print(sorted(nums))


del myList[2]
print(myList)

newList = list(range(10,20))
print(newList)

products = "zil", "pc", "keyboard";
print(sorted(products))


newProducts = []
print(type(newProducts))
newNewProducts = list()
print(type(newNewProducts))
