# import pandas as pd
# import numpy as np
# import nltk
import re
# import pickle
# import itertools
# from nltk.stem.wordnet import WordNetLemmatizer 
# from django.conf import settings
# import os
# import pandas as pd
# import pickle
# import os
##
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer 
import itertools
import numpy as np
import nltk
##
# import settings  # assuming settings module is available

# tweet = 'Layin n bed with a headache  ughhhh...waitin on your call...'

class emotion_analysis_code():

    lem = WordNetLemmatizer()

    def cleaning(self, text): 
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            index = 0
            for j in range(len(txt)):
                if txt[j][0] == '@':
                    index = j
            txt = np.delete(txt, index)
            if len(txt) == 0:
                return 'no text'
            else:
                words = txt[0]
                for k in range(len(txt)-1):
                    words+= " " + txt[k+1]
                txt = words
                txt = re.sub(r'[^\w]', ' ', txt)
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    #data.content[i] = [w for w in data.content[i] if not w in stopset]
                    for j in range(len(txt)):
                        txt[j] = self.lem.lemmatize(txt[j], "v")
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        return txt

    def predict_emotion(self,tweet):
        # return "" 
        ##
        # tweet = ' '.join(self.cleaning(tweet))
        # analysis = TextBlob(tweet)
        # if analysis.sentiment.polarity > 0:
        #         return 'Positive'
        # elif analysis.sentiment.polarity == 0:
        #         return 'Neutral'
        # else:
        #         return 'Negative'
        # def get_tweets(self, sentence):
        # sentence="I am very sad"
        # blob = TextBlob(tweet)
        # sentiment = blob.sentiment.polarity

        # if sentiment > 0.3:
        #     return "Love"
        # elif sentiment > 0:
        #     return "Happiness"
        # elif sentiment < -0.3:
        #     return "Sadness"
        # elif sentiment < 0:
        #     return "Worry"
        # else:
        #     return "Happiness" or "neutral"
        ##
        blob = TextBlob(tweet)
        sentiment = blob.sentiment.polarity

        if sentiment > 0.3:
         return "Love"
        elif sentiment > 0:
         return "Happiness"
        elif sentiment < -0.3:
         return "Sadness"
        elif sentiment < 0:
         return "Worry"
        else:
        # Check for the presence of angry-related words
          angry_keywords1 = ["happy","Congratulations", "joyful", "excited", "delighted", "ecstatic", "blissful", "content", "thrilled", "euphoric", "upbeat"]
          tweet_lower1 = tweet.lower()
          if any(keyword in tweet_lower1 for keyword in angry_keywords1):
            return "Happiness"
          angry_keywords = ["angry","not" ,"rage", "outrage", "furious", "irritated"]
          tweet_lower = tweet.lower()
           
          if any(keyword in tweet_lower for keyword in angry_keywords):
            return "Angry"
        #   if any(keyword in tweet_lower1 for keyword in angry_keywords1):
        #     return "Happiness"
          else:
            return "Neutral"

        # tweet = ["i am good","i ma sad"]
        # tweet_in_pandas = pd.Series(' '.join(self.cleaning(text)))
        

        # path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
        # path_model = os.path.join(settings.MODELS, 'finalized_model.sav')

        # # load vectorizer
        # # vec_file = 'vectorizer.pickle'
        # vectorizer = pickle.load(open(path_vec, 'rb'))
        # # load trained model
        # # filename = 'finalized_model.sav'
        # model = pickle.load(open(path_model, 'rb'))




        # test = vectorizer.transform(tweet_in_pandas)
        # # return model
        # predicted_sentiment = model.predict(test)
        # # return predicted_sentiment
        # final_sentiment = (predicted_sentiment[0])
        # if final_sentiment == 'worry':
        #     return 'Worry'
        # elif final_sentiment == 'sadness':
        #     return 'Sadness'
        # elif final_sentiment == 'happiness':
        #     return 'Happiness'
        # elif final_sentiment == 'love':
        #     return 'Love'
        # elif final_sentiment == 'hate':
        #     return 'Hate'  
    # def predict_emotion(self, text):
    #  tweet_in_pandas = pd.Series(' '.join(self.cleaning(text)))

    #  path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
    #  path_model = os.path.join(settings.MODELS, 'finalized_model.sav')

    #  vectorizer = pickle.load(open(path_vec, 'rb'))
    #  model = pickle.load(open(path_model, 'rb'))

    #  test = vectorizer.transform(tweet_in_pandas)
    #  predicted_sentiment = model.predict(test)

    #  final_sentiment = predicted_sentiment[0]
    #  return test
    #  if final_sentiment == 'worry':
    #     return 'Worry'
    #  elif final_sentiment == 'sadness':
    #     return 'Sadness'
    #  elif final_sentiment == 'happiness':
    #     return 'Happiness'
    #  elif final_sentiment == 'love':
    #     return 'Love'
    #  elif final_sentiment == 'hate':
    #     return 'Hate'
    #  else:
    #     return 'Unknown'
 

