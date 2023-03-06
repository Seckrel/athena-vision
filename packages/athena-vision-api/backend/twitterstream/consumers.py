import json
from channels.generic.websocket import WebsocketConsumer
from .utils.sample_stream import TweetStream
from .utils.prediction import Prediction
from os import getenv
import requests

from django.core.cache import cache


class TweetStreamConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        # Debugging and Developing
        self.__getStream()
        self.__makePrediction()

        # Unmute above doing lunch

        # self.send(text_data=json.dumps({
        #     "type": "json",
        #     "data": [{
        #         "text": "fadhfkdajfkjdafjdafjdka djadgjakngkldjgo ajklgjaklgjdaljg",
        #         "author_name": "hello1",
        #         "hate_flag": 1,
        #         "topic": "Something",
        #         "sentiment": "Pos",
        #     }, {
        #         "text": "lkgaiejoadgwjgsd gjsdkgjawgo dhgoia",
        #         "author_name": "hello2",
        #         "hate_flag": 1,
        #         "topic": "Something",
        #         "sentiment": "NEU",
        #     }, {
        #         "text": "fjal djfld a d ",
        #         "author_name": "hello3",
        #         "hate_flag": 0,
        #         "topic": "Something",
        #         "sentiment": "neg",
        #     }],
        #     "context": {
        #         "blur": blur,
        #         "topic": topic,
        #         "emotion_tone": emotion_tone
        #     }
        # }))

    def receive(self, text_data):
        data = json.loads(text_data)

        # muted during development

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

    def __zip_label(self, labels, key):
        for idx, tweets in enumerate(zip(self.tweet_data, labels)):
            self.tweet_data[idx][key] = tweets[1]

    def __topic_analysis(self, topic, tweet_texts):
        if topic == 0:
            self.__zip_label(
                ["" for i in range(len(self.tweet_data))], "topic")
            return

        API_URL = "https://api-inference.huggingface.co/models/classla/xlm-roberta-base-multilingual-text-genre-classifier"
        headers = {
            "Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        try:
            output = query({
                "inputs": tweet_texts
            })

            topics = list(map(lambda x: x[0]["label"], output))

            self.__zip_label(topics, "topic")
        except:
            self.__zip_label(
                ["" for i in range(len(self.tweet_data))], "topic")

    def __sentiment_analysis(self, emotion_tone, tweet_texts):
        if emotion_tone == 0:
            self.__zip_label(["" for i in range(
                len(self.tweet_data))], "sentiment")
            return

        API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-xlm-roberta-base-sentiment"
        headers = {
            "Authorization": f"Bearer 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"}

        def query(payload):
            response = requests.post(
                API_URL, headers=headers, json=payload)
            return response.json()

        try:
            output = query({
                "inputs": tweet_texts
            })
            labels = list(map(lambda x: x[0]["label"][:3], output))

            self.__zip_label(labels, "sentiment")
        except:
            self.__zip_label(["" for i in range(
                len(self.tweet_data))], "sentiment")

    def __hate_prediction(self, blur):
        model = Prediction()
        for idx, tweet in enumerate(self.tweet_data):
            try:
                hate_flag = 0

                if blur == 1:
                    hate_flag = model.predict_hate(tweet["text"])

                self.tweet_data[idx]["hate_flag"] = str(hate_flag)
            except:
                self.tweet_data[idx]["hate_flag"] = "0"

    def __makePrediction(self):
        print("="*4, ">Predicting<", "="*4)

        data = cache.get("session")

        blur = 0
        emotion_tone = 0
        topic = 0
        tweet_texts = []

        if cache.get("ext_power"):
            if data != None:
                print('Caching...........')
                blur = data.get("blur")
                emotion_tone = data.get("emotional tone")
                topic = data.get("topic label")

        if emotion_tone == 1 or topic == 1:
            tweet_texts = [d["text"] for d in self.tweet_data]

        self.__hate_prediction(blur)

        print("sentiment", emotion_tone)
        self.__sentiment_analysis(emotion_tone, tweet_texts)
        
        print("topics", topic)
        self.__topic_analysis(topic, tweet_texts)

        print("="*4, ">Predicting<", "="*4)

        self.send(text_data=json.dumps({
            "type": "json",
            "data": self.tweet_data
        }))
