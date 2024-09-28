#take input from user and convert into upper case, lower case and title format
'''
str=input("Enter a string:")
str1=str.upper()
str2=str.lower()
str3=str.title()
print("The string in Upper  Case is ",str1)
print("The string in Lower Case is ",str2)
print("The string in Title case is ",str3)
'''





#2. tke string as input and check if given string is palindrome or not

'''
str = input("Enter a string ")
filteredString = "".join(str.split()).lower()
reverseStr=str[::-1]
if str==reverseStr:
 print("The string {str} is a palindrome")
else:
    print("The string {str} is not a palindrome")
'''



# to search a substring in a givern string
'''
str = input("Enter a string ")
subString = input("Enter a substring")
if subString in str:
    print("The Substring " , subString ,"is found in string ",str)
else:
    print("The Substring " ,subString ,"is not found in string",str)
'''



# take input and count the word in given sentence 

'''
def count_words(sent):
    str=sent.split()
    count = 0
    for i in range(len(str)):
        count+=1
    print("No. of words in sentence =", count)

ence= input("Enter a sentence ")
count_words(ence)
 '''
 
#5 . take input sentence and check the occurence of the word "The"
 