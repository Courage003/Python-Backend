country_file = open(r"C:\Users\Dhruv\Desktop\Pyhton Backend\Python-Backend\advanced\new.txt", "w")

country_file.write('This is the new text')
#everything initial will get changed to this
#if we create new filename a new file will be created


country_file = open(r"C:\Users\Dhruv\Desktop\Pyhton Backend\Python-Backend\advanced\new.txt", "a")
country_file.write('/n This is a new line')

#append add on
