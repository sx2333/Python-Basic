import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***":
        "From *** get the *** attribute and set is to '***'."    
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():  # 依次读取链接中的每一行
                                            # readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存。
    WORDS.append(str(word.strip(), encoding = "utf-8"))  # .strip()的功能就是将字符串中的头尾空格去掉


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.conut("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)  # random.randint(a,b) 用于生成指定范围内的随机数，包括a，b
        param_names.append(','.join(random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


#keep going util they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())  #list()表示将不可修改的元组修改为列表
        random.shuffle(snippets)

    for snippet in snippets:
        phrase = PHRASES[snippet]
        question, answer = convert(snippet, phrase)
        if PHRASES_FIRST:
            question, answer = answer, question

        print(question)

        input("> ")
        print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")

    
        
        
