# Api libraries
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from big_picture.classifier import Classifier
import pandas as pd
import requests
import pickle

# Internal libraries
#from big_picture.classifier import get_model

'''
    Em relação à arquitectura do API:
    Vou criar a função predict, que usa a instancia de 
    Classifier para fazer o predict da nova noticia:
    o que são os inputs e o que devem ser os outputs?
    porque a class instance de Classifier só da return 
    da tag da label, e da tag do cluster certo?

    acho que o input devia ser um news_api json ou algo do genero
    o output podia ser um cluster instance
    isso podia ser logo o output do classifier.predict
    '''

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {'welcome': 'This is the Big_Picture API'}

@app.get("/search")
def search(query, title=None, source=None, label=None, date_from=None):
    """
    Endpoint that searches for the news and retrieves 10 examples of news.

    Parameters
    ----------
    
    query: string
        String containing the query to be made to the API - the news to be searched.
    
    title: string
        Search for news containing that title. Default value is None.

    source: string or list
        Search for a precise source or a list of sources. Default value is None.
    
    label: string
        Search for a precise label. Default value is None.

    date: string
        Search for a precise date. Default value is None.

    date_from: string
        Search for news since a precise date. Default value is None.
    """

    # dar replace pela função do martins mais tarde
    opt_args = {'q': query,
                'qInTitle': title,
                'sources': source,
                'domain': label, 
                'from': date_from}

    params = {}

    for key, value in opt_args.items():
        if value != None:
            params[key] = value

    #TODO Define SECRET
    params['apiKey'] = 'a97dc775dfc04e44867f79e0b512590b'
    
    url = 'https://newsapi.org/v2/'
    everything = 'everything'
    top_headlines = 'top-headlines'


    response = requests.get(url + everything, params=params).json()

    # Select ten news and retrieve useful information
    news_dict = {}
    for idx, article in enumerate(response['articles'][0:10]):
        news_dict[idx] = {
            'title': article['title'],
            'author': article['author'],
            'source': article['source']['name'],
            'url': article['url'],
            'date': article['publishedAt'][0:10],
            'content': article['content']
        }

    return news_dict

@app.get("/predict")
def predict(df):
    """
    Class that creates an object with a model and the topics associated to the model,
    and the prediction for label and clusters.

    Parameters
    ----------
    
    df: DataFrame
        DataFrame that contains the content to be predict the label from.
    """

    filename = '../big_picture/models/classifier_baseline.sav'

    loaded_model = pickle.load(open(filename, 'rb'))

    prediction = loaded_model.predict(df.news_all_data)




    # get Classifier instance
    # predict new data
    # Sent_analysis new data
    # Normalize new SA clusters
    # return title, label, clusters and SA.

    return Classifier
