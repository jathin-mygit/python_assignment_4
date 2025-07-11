try :
    my_file = open('sample.txt','r')
    file_content = my_file.readlines()
    count = 0
    print("Reading file content : ")
    for line in file_content:
        count += 1
        print(f"Line {count} : {line.strip()}")
    my_file.close()

except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found")