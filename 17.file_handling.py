#the key function for working with files is open(filename(path), modes)

#MODES : there are 4 modes(method) mainly
#1. "r" : Read only : gives errors if file does not exist
#2. "a" : Append : creates files if file does not exist
#3. "w" : write : opens file for writing, creates file if file does not  exist
#4. "x" : create : creates file , give error if file alredy exists
#5. "t" : Text mode
#6. "b" : Binary Mode


# f = open("demo.txt","x")
# f = open("demo.txt","a")
# f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!")
# f = open("demo.txt", "r")
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# f.close(5)

#another task

# import os
# if os.path.exists("ajay.txt"):
#     os.remove("ajay.txt")
    
# f = open("ajay.txt","x")

# f.write("Hi there\n I AM India\n")

# f = open("ajay.txt","r")
# print(f.read())
# # print(f.readline())
# f.close()



#My Practice
import os
# if os.path.exists("new.txt"):
#     os.remove("new.txt")

# f = open("new.txt","x")

# f.write("HI there my name is file handling\n in python")
# f.close()

r = open("new.txt","r")
print(r.read())
print(r.readline())

r.close()

a = open("new.txt","a")
a.write("this text is due to apeend ")
a = open("new.txt","r")
print(a.read())
a.close()



