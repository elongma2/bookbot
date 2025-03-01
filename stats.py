
def word_counter(text):
    count = 0
    word_list = text.split()
    for x in word_list:
        count +=1
    return count

def letter_counter(text):
    letter_dict = {}
    word_list = text.split()
    for x in word_list:
        for y in x.lower():
            if y in letter_dict:
                letter_dict[y] += 1
            else:
                letter_dict[y] = 1
    return letter_dict


def sort_dict(letter_dict):
    letter_dict = sorted(letter_dict.items(),key = lambda x: x[1] ,reverse=True)
    return letter_dict