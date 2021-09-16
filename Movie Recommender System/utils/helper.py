import ast
from nltk.stem.porter import PorterStemmer
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L 

def convert3text(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
    return L


def stem(text):
    ps=PorterStemmer()
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
 