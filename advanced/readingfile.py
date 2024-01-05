country_file = open(r"C:\Users\Dhruv\Desktop\Pyhton Backend\Python-Backend\advanced\countries.txt", "r")
#raw error added to stop backspace act as escape characters
#r refers for reading
#w for writing
#a for appenind
#r+ for both reading and writing
print(country_file.readable())
print(country_file.readline()) #reads first line
print(country_file.readlines())


for files in country_file.readlines():
    print(files)

country_file.close()

