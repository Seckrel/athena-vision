import json
from channels.generic.websocket import WebsocketConsumer
from .utils.sample_stream import TweetStream
from .utils.prediction import Prediction
from os import getenv


class TweetStreamConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.__getStream()
        self.__makePrediction()

    def receive(self, text_data):
        data = json.loads(text_data)
        if data["signal"].lower() == "more":
            self.__getStream()
            self.__makePrediction()

    def disconnet(self, close_code):
        pass

    def __getStream(self):
        self.tweet_data = []
        stream = TweetStream(
            self.tweet_data, bearer_token=getenv("T_BEARER_TOKEN")
        )

        print("--------->Samping")
        stream.sample(expansions=["author_id"], tweet_fields=[
            "entities", "lang"])
        print("-------->Sampled")

    def __makePrediction(self):
        model = Prediction()
        print("="*4, ">Predicting<", "="*4)

        for idx, tweet in enumerate(self.tweet_data):
            hate_flag = model.predict_hate(tweet["text"])
            self.tweet_data[idx]["hate_flag"] = str(hate_flag[0])

        print("="*4, ">Predicting<", "="*4)

        self.send(text_data=json.dumps({
            "type": "json",
            "data": self.tweet_data
        }))
