# Python – Replace multiple words with K
str1 = input('Enter the string=')
char = input('Enter the word or words you want to replace with K=')
str2 = ''
for i in str1:
    str2 = str1.replace(char, 'k')
print(str2)
