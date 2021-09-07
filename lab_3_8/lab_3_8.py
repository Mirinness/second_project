#Write a script that creates a new output file called myfile.txt
mic = open('myfile.txt', 'w')

#writes the string "Hello file world!" into it
mic.write('Hello file world!')

#write another code that opens myfile.txt in w+ mode
mic2 = open('myfile.txt', 'w+')

#read and print its contents
mic2 = open('myfile.txt', 'r')
print(mic2.read())

#write into “Hello file” string new value “my” – “Hello my file”
mic = open('myfile.txt', 'w+')
mic.write('Hello my file world!')

#Save changes without file object close
mic = open('myfile.txt', 'r')