import keras
import nltk
import string
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
import gensim
from scipy import spatial
import spacy
import pandas as pd
from nltk.stem import PorterStemmer

nlp = spacy.load('en_core_web_lg')  #loading pretrained vocabulary

def clean_text(text):  #this function clean the text like remove stopwords, make text into tokens lemmatize the text, lower case all letters
    doc1=""
    tokens=word_tokenize(text)  #tokenizing the text
    tokens=[w.lower() for w in tokens]
    table=str.maketrans('','',string.punctuation) #remove punctuation
    stripped=[w.translate(table) for w in tokens]
    words=[word for word in stripped if word.isalpha()] 
    stop_words=set(stopwords.words('english'))   #remove stop words
    words=[w for w in words if w not in stop_words]
    lmtzr = WordNetLemmatizer()  #lemmatizer
    stemmer = PorterStemmer() #stemming
    for i in words:  #making tokens to text
        doc1=doc1+i+' '    
    doc1=nlp(doc1)
    return doc1


data=pd.read_csv('doc2.csv') #data read
d=pd.DataFrame(data) #converting scv to dataframe
count=0
pointer=0
d['Suggetions']=' '

for i in d['Key words']:
    input_text=i  #Input what user want to search
    input_text=clean_text(input_text)
    max_val=-1
    index=0
    sim=[]
    mapping={}
    for i in d['Description']:   #this for loop check similarity betweeen input and all description and find the maximum out of it
        ti=clean_text(i)
        x=input_text.similarity(ti)  #this uses Glove and average the word embedding to make a document a vector
        sim.append(x)
        mapping[x]=d.iloc[index,0]
        if(x>max_val):
            max_val=x
            suggest=d.iloc[index,0] #getting the title of the desired description
        index=index+1    
    
    sim.sort(reverse=True)
    if d.iloc[pointer,0]==mapping[sim[0]] or d.iloc[pointer,0]==mapping[sim[1]] or d.iloc[pointer,0]==mapping[sim[2]]:
        count=count+1
    print(d.iloc[pointer,0])
    d.iloc[pointer,3]=mapping[sim[0]]+', '+mapping[sim[1]]+', '+mapping[sim[2]]
    print(mapping[sim[0]]+', '+mapping[sim[1]]+', '+mapping[sim[2]])
    print(' ')
    pointer=pointer+1
print(count/len(d['Key words']))
print(count)
print(len(d['Key words']))
