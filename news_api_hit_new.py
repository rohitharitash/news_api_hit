import datetime
import time
from newsapi import NewsApiClient
import pandas as pd





def test_fuc():

    key1 = "8f44b094b7bb4ceebc6ba53d21cee940" # this is the change in github server
    #key2 = "1200edfb432f488cab980978a64c252e"

    all_result = []



    params = {
        "param": [{"country": "in",
                   "category_entertainment": "entertainment",
                   "category_business": "business",
                   "category_general": "general",
                   "category_health": "health",
                   "category_science": "science",
                   "category_sports": "sports",
                   "category_technology": "technology",
                   "pagesize": 100,
                   "page": 1
                   }]
    }

    while True:
        newsapi = NewsApiClient(api_key=key1)

        top_headlines_entertainment = newsapi.get_top_headlines(category=params['param'][0]["category_entertainment"],
                                                                language='en',
                                                                country=params['param'][0]["country"],
                                                                page=params['param'][0]["page"],
                                                                page_size=params["param"][0]["pagesize"])
        time.sleep(1)

        top_headlines_business = newsapi.get_top_headlines(category=params['param'][0]["category_business"],
                                                           language='en',
                                                           country=params['param'][0]["country"],
                                                           page=params['param'][0]["page"],
                                                           page_size=params["param"][0]["pagesize"])
        time.sleep(1)

        top_headlines_general = newsapi.get_top_headlines(category=params['param'][0]["category_general"],
                                                          language='en',
                                                          country=params['param'][0]["country"],
                                                          page=params['param'][0]["page"],
                                                          page_size=params["param"][0]["pagesize"])

        time.sleep(1)

        top_headlines_health = newsapi.get_top_headlines(category=params['param'][0]["category_health"],
                                                         language='en',
                                                         country=params['param'][0]["country"],
                                                         page=params['param'][0]["page"],
                                                         page_size=params["param"][0]["pagesize"])

        time.sleep(2)

        top_headlines_science = newsapi.get_top_headlines(category=params['param'][0]["category_science"],
                                                          language='en',
                                                          country=params['param'][0]["country"],
                                                          page=params['param'][0]["page"],
                                                          page_size=params["param"][0]["pagesize"])

        time.sleep(2)

        top_headlines_sports = newsapi.get_top_headlines(category=params['param'][0]["category_sports"],
                                                         language='en',
                                                         country=params['param'][0]["country"],
                                                         page=params['param'][0]["page"],
                                                         page_size=params["param"][0]["pagesize"])
        time.sleep(1)

        top_headlines_technology = newsapi.get_top_headlines(category=params['param'][0]["category_technology"],
                                                             language='en',
                                                             country=params['param'][0]["country"],
                                                             page=params['param'][0]["page"],
                                                             page_size=params["param"][0]["pagesize"])

        entertainment_pd = pd.DataFrame(top_headlines_entertainment["articles"])
        entertainment_pd['category'] = "entertainment"
        business_pd = pd.DataFrame(top_headlines_business["articles"])
        business_pd['category'] = "business"
        general_pd = pd.DataFrame(top_headlines_general["articles"])
        general_pd['category'] = "general"
        health_pd = pd.DataFrame(top_headlines_health["articles"])
        health_pd['category'] = 'health'
        science_pd = pd.DataFrame(top_headlines_science["articles"])
        science_pd['category'] = 'science'
        sports_pd = pd.DataFrame(top_headlines_sports["articles"])
        sports_pd['category'] = 'sports'
        technology_pd = pd.DataFrame(top_headlines_technology["articles"])
        technology_pd['category'] = 'technology'

        final_result = pd.concat(
            [entertainment_pd, business_pd, general_pd, health_pd, science_pd, sports_pd, technology_pd],
            ignore_index=True)
        print(entertainment_pd.shape)
        print(business_pd.shape)
        print(final_result.shape)
        now = datetime.datetime.now()


test_fuc()

def __main__():
    test_fuc()

def other():
    return "test"