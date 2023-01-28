dict={
    "name":"John Smith",
    "age":30,
    "is_verified":True,
    50:False
}
print(dict["name"])
print(dict.get("name"))
print(dict.get("name","Ishaan")) # default
print(dict[50])
dict.update({"age":50})
dict["age"]=40
print(dict)