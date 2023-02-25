import time

points = 1500 #change for user input instead

# points per character --> 5 points = 1 character

num_of_char = points//5

#opening file with building1

with open("/Users/evahiso/Desktop/building txt/building1.txt") as file1:
    building1_lines = [line.rstrip() for line in file1] #removes end space
    building1_lines.reverse() #reverses order of lines
    file1contents = file1.read()#reads characters in file
    building1_char_total = len(file1contents) #gets number of characters in the file

#building 1 progress
char_printed1 = 0 #num of chars printed out of possible chars in a day
char_printed_total1 = 0 #num of chars printed out of chars possible in building

# opening file with building 2
with open("/Users/evahiso/Desktop/building txt/building2.txt") as file2:
    building2_lines = [line.rstrip() for line in file1]
    building2_lines.reverse()
    file2contents = file2.read()
    building2_char_total = len(file2contents)

#building 2 progress
char_printed2 = 0
char_printed_total2 = 0

#Opening file with building 3
with open("/Users/evahiso/Desktop/building txt/building3.txt") as file3:
    building3_lines = [line.rstrip() for line in file3]
    building3_lines.reverse()
    file3contents = file3.read()
    building3_char_total = len(file3contents)

#building 3 progress
char_printed3 = 0
char_printed_total3 = 0

if char_printed_total1 < building1_char_total: #while building 1 is unfinished, keep on working on building 1
    for line in building_lines1:
        for element in line:
            if char_printed1 < num_of_char: #if the number of chars printed is still not the same as the characters available for that day:
                print(element, end="")
                time.sleep(0.01)
                char_printed1 += 1
            else:
                break
        print()
elif char_printed_total1 >= building1_char_total: #move on to building 2
    if char_printed_total2 < building2_char_total:
        for line in building_lines2:
            for element in line:
                if char_printed2 < num_of_char:
                    print(element, end="")
                    time.sleep(0.01)
                    char_printed2 += 1
                else:
                    break
            print()
    elif char_printed_total2 > building2_char_total:



