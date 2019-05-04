def break_words(stuff):
    """This function will brerak up words for us."""
    words = stuff.split(' ')
    return words  #定义函数，将句子中的单词进行拆分

def sort_words(words):
    """Sort the words."""
    return sorted(words)  #按字母顺序对单词进行排序

def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0)  #默认为删除列表第一个值
    print(word)

def print_last_word(words):
    """Prints the last word after poping it off."""
    word = words.pop(-1)  #默认为删除列表的最后一个值
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)  #调用break_word和sort_words函数

def print_first_and_last(sentence):
    """Print the first and last words of the sentence. """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
