words = {
'0': '',
'00': '',
'1': 'one',
'2': 'two',
'3': 'three',
'4': 'four',
'5': 'five',
'6': 'six',
'7': 'seven',
'8': 'eight',
'9': 'nine',
'10': 'ten',
'11': 'eleven',
'12': 'twelve',
'13': 'thirteen',
'14': 'fourteen',
'15': 'fifteen',
'16': 'sixteen',
'17': 'seventeen',
'18': 'eighteen',
'19': 'nineteen',
'20': 'twenty',
'30': 'thirty',
'40': 'forty',
'50': 'fifty',
'60': 'sixty',
'70': 'seventy',
'80': 'eighty',
'90': 'ninety',
}

def num_to_word(x):
    # split x into digits
    x = str(x)[::-1]
    while len(x)<3:
        x+="0"
    word = ""
    if not x[2] == "0":
        word += words[x[2]]+"hundred"
    if not x[1] == '0' or not x[0] == '0':
        if not x[2] == '0':
            word += 'and'
        if x[1] == '1':
            word += words[x[1]+x[0]]
        else:
            word += words[x[1]+'0']
            word += words[x[0]]
    return word

print num_to_word(650)

total = 0
for i in range(1,1000):
    total += len(num_to_word(i))
total += 11
print total