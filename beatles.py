# Create empty list, and populate with original three Beatles
beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

# Prompt user to add Stu Sutcliffe and Pete Best
stu = input("Add 'Stu Sutcliffe': ")
pete = input("Add 'Pete Best': ")

for i in range(len(beatles)//2):
  beatles.append(stu)
  beatles.append(pete)

print(beatles)

del beatles[4]
del beatles[3]
print(beatles)

beatles.insert(0, "Ringo Starr")
print(beatles)

print("The Fab", len(beatles))