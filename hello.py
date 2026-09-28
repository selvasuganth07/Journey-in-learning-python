# first python code for saying hello to name
name = input("what is your name? ").strip().title()
first,second = name.split(" ")
# print hello
print(f"hello,{first}",sep= " ")
