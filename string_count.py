n ="aaaaabbbbccccccaaaaaaa"
def dstring(n):
    letter = n[0]
    letter_count = 0
    whole_string = []
    answer_set = []

    for x in n:

        if x == letter:
            letter_count = letter_count + 1
            whole_string.append(str(letter_count) + letter) 
        else:
            #print whole_string
            answer_set.append(whole_string.pop())
            letter_count = 0
            letter_count = letter_count + 1
            letter = x
            whole_string = []
            whole_string.append(str(letter_count) + letter)

    #print whole_string
    answer_set.append(whole_string.pop())

    return ''.join(answer_set)

print dstring(n)
