# get string from console
string = input('Enter the string: ')
# get the list of words from input string
words = string.split(' ')
# create the largest word variable that init with empty string
largest_word = ''
for word in words:
    # if legth of the word bigger that lenght of the largest word
    if len(word) > len(largest_word):
        # then largest word becomes equal current word
        largest_word = word
print(largest_word)