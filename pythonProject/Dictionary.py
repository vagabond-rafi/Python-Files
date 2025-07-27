
thisdict = { "brand" : "Ford", #brand,model,year these are key
             "Model" : "Mustang", # ford,Mustang,1964 these are values
             "Year"  : "1964"
             }

print(thisdict)
print(thisdict["brand"])
print(len(thisdict)) #how many item a dictionary has
print(type(thisdict))

dictt = dict (name = "Abc" , Age = 99, country = "Norway") # dictionary constructor
print("---------")
print(dictt)

diction = {
    "Griffindor" : "Hermione Granger",
    "Slytherin" : "Draco Malfoy",
    "Hufflepuff" : ["Cedric ",90]
}
print(diction)
print(diction.get("Slytherin"))
print(diction.keys())
print(diction.values())
diction.update({"Griffindor":"Harry potter"})
diction.pop("Hufflepuff")

print("Joy Bangla")