import pickle
import pandas as pd
import numpy as np
import nltk
# nltk.download('popular')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re,string


def clean_text(message):
    text = message.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

ps = PorterStemmer()
def text_transform(text):
  text = word_tokenize(clean_text(text))
  words = [ps.stem(w) for w in text if w not in set(stopwords.words('english'))]
  return " ".join(words)

def predictSpam(text):
    with open("model.pkl","rb") as files:
      saved_model = pickle.load(files)
      with open("vec","rb") as files:
        v = pickle.load(files)
        clean_text = text_transform(text)
        tv = v.transform([clean_text]).toarray()
        result = saved_model.predict(tv)
        return result
        
    
    
if __name__ == "__main__":
    text = "Dear Aman saxena, Bank of America is closing your bank account. Please confirm your PIN at http://www.google.com to keep your account activated."
    text2 = "A [redacted] loan for $950 is approved for you if you receive this SMS. 1 min verification & cash in 1 hr at www.[redacted].co.uk to opt out reply stop"
    text3 = "Buy 1 card get 1 free! Please kindly reply this email if you are interested. Thank you..."
    text4 = "You could be entitled up to $3,160 in compensation from mis-sold PPT on a credit card or Loan. Please reply PPI for info or STOP to opt out."
    
    
    print(predictSpam(text2))