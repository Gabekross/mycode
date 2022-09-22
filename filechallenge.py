#!/usr/bin/python3
count = 0
with open("/home/student/dracula.txt","r") as foo:
    with open("/home/student/vampytimex.txt","w") as foo2:
        for line in foo:
            if "vampire" in line.lower():
                count = count + 1
                print(line)
                foo2.write(line)
print("total vampire word count: ",count)
