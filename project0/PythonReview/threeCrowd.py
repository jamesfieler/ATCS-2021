def crowd_test(nameList):
    if len(nameList) > 3:
        nameList.pop(0)
        nameList.pop(0)
    
names = ["Aaron", "Ben", "Carl", "David"]
crowd_test(names)
print(names)