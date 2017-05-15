#! python3
# https://medium.com/towards-data-science/how-to-use-twitters-api-c3e25c2ad8fe

"""
ctkmyU61ZsBgOsxhZP7k0XfJw
UAPyjoAzI0vfvmbt1esn2OVm82CuTLM4pG1T5sQdpT4WAZ16OZ
861952602765795329-sSmDQoYwxZfsW0bX6hvRIDXPkTVYgbV
M2hUjXP65HHq9AHI506VW7hmRxzIWnGAJMGlm7GEMWjJS
"""
import twitter, re, datetime, pandas as pd

class twitterminer():
    request_limit = 20
    api = False
    data = []

    twitter_keys = {
        'consumer_key': "ctkmyU61ZsBgOsxhZP7k0XfJw",
        'consumer_secret': "UAPyjoAzI0vfvmbt1esn2OVm82CuTLM4pG1T5sQdpT4WAZ16OZ",
        'access_token_key': "861952602765795329-sSmDQoYwxZfsW0bX6hvRIDXPkTVYgbV",
        'access_token_secret': "M2hUjXP65HHq9AHI506VW7hmRxzIWnGAJMGlm7GEMWjJS",
    }

    def __init__(self, request_limit = 20):
        self.request_limit = request_limit
        # This sets the twitter API object for use internally within the calss
        self.set_api()

    def set_api(self):
        self.api = twitter.Api(
            consumer_key = self.twitter_keys['consumer_key'],
            consumer_secret = self.twitter_keys['consumer_secret'],
            access_token_key = self.twitter_keys['access_token_key'],
            access_token_secret = self.twitter_keys['access_token_secret']
        )

    def mine_user_tweets(self, user="tylerhardy42", mine_retweets=False):
        statuses = self.api.GetUserTimeline(screen_name=user, count=self.request_limit)
        data = []
        for item in statuses:
            mined={
                'tweet_id': item.id,
                'handle': item.user.name,
                'retweet_count': item.retweet_count,
                'text': item.text,
                'mined_at': datetime.datetime.now(),
                'created_at': item.created_at,
            }
            data.append(mined)
        return data

miner = twitterminer()
# insert handle we like
trump_tweets = miner.mine_user_tweets("realDonaldTrump")
trump_df = pd.DataFrame(trump_tweets)
print(dir(trump_df))

trump_text_file = open('trump_text_file.txt', 'w')
trump_text_file.write(str(trump_tweets))
trump_text_file.close()