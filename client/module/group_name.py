import  random

def random_letters():
    letters = ['东','楠', '坤' ,'乐', '锟', '鉷']
    random.shuffle(letters)
    return ''.join(letters)
#print(random_letters())