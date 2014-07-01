# Author:  Dorothy H. Sanchez
#
# This function will reverse a string

def reverse_string(text):
    hold = ''
    for character in text:
        hold = character + hold
    return hold

if __name__ == '__main__':
    print reverse_string('I am Happy')
