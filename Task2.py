try :
    text = input("Enter text to write to file  : ")
    my_file = open('output.txt','w')
    my_file.write(text)
    my_file.close()
    print("Data successfully written to output.txt\n")

    another_text = input("Enter another text to append : ")
    my_file = open('output.txt','a')
    my_file.write("\n" + another_text)
    my_file.close()
    print("Data successfully appended\n")

    print("Final content of output.txt : ")
    my_file = open('output.txt','r')
    content = my_file.readlines()
    for line in content:
        print(line.strip())

except :
    print("Error : The file 'output.txt' was not found")
