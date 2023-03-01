import json
from channels.generic.websocket import WebsocketConsumer
from .utils.sample_stream import TweetStream
from os import getenv


class TweetStreamConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.__getStream()

    def receive(self, text_data):
        data = json.loads(text_data)
        if data["signal"].lower() == "more":
            self.__getStream()

    def disconnet(self, close_code):
        pass

    def __getStream(self):
        self.tweet_data = []
        stream = TweetStream(
            self.tweet_data, bearer_token=getenv("T_BEARER_TOKEN")
        )

        stream.sample(expansions=["author_id"], tweet_fields=[
            "entities", "lang"])

        self.send(text_data=json.dumps({
            "type": "json",
            "data": self.tweet_data
        }))
