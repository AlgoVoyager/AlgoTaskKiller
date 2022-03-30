import os
filename = "kill_list.txt"
kill_list  = open(filename,"a+")
kill_list.close()

list_txt = open("kill_list.txt","r")
kill_list = list_txt.readlines()
list_txt.close()

print("\nsn. ProcessName List: ")
counter = 0
the_list = ""

for char in kill_list:
    if char != "\n" and char != "\r":
        counter += 1
        the_list += str(str(counter)+ ".  "+ char  )
print(the_list)

inp = input("""enter sn. of ProcessName 
or enter "c" custom ProcessName
or just click "enter" for all
>>>  """)

if inp =="":
    for i in kill_list:
        os.system(f"taskkill /IM \"{i}\" /F")       
elif inp =="c":
    inp2 = input("Enter process name: ")
    os.system(f"taskkill /IM \"{inp2}\" /F")
else:
    counter = 0
    the_li = ""
    for char in kill_list:
        if char != "\n" and char != "\r":
            counter += 1
            the_li = char
            if str(counter) == inp:
                os.system(f"taskkill /IM \"{char}\" /F")
