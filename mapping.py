# phone = input('Input a phone number');

# files = {
#     '1':'One',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four'
# }
# output = ""
# for ch in phone:
#  output +=  files.get(ch, "!") + " "

# print(output)

message = input('> ')
words = message.split (' ')

files = {
    ':)': '😀',
    ':(': '😞'
}
output = ""
for word in words:
    output += files.get(word, words).append(" ")
print(output)