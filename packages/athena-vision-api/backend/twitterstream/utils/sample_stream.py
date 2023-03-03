import tweepy
import time
import json
from queue import Queue
from django.apps import apps


class TweetStream(tweepy.StreamingClient):
    def __init__(self, tweet_data, bearer_token) -> None:
        super().__init__(bearer_token)
        self.tweet_data = tweet_data
        self.support_lang = ['en', 'ne']
        self.buffer_size = 5
        self.pumping = True
        self.delay = 0.2

    def on_connect(self):
        print("connected")
        self.buffer = Queue(self.buffer_size)

    def on_data(self, data):
        data_dict = self.__byte_to_json(data)

        if self.__check_lan(data_dict["data"]["lang"]):
            required_data = self.__extract_data(data_dict)

            if self.pumping:
                self.__pump(required_data)
            else:
                self.__sink()

        time.sleep(self.delay)

    def __pump(self, data):
        if self.buffer.qsize() >= self.buffer_size:
            self.pumping = False
            return

        self.buffer.put(data)

    def __sink(self):
        self.disconnect()

        for _ in range(self.buffer.qsize()):
            self.tweet_data.append(self.buffer.get())

        self.buffer.queue.clear()

    def __extract_data(self, data_dict):
        author_name = self.__get_author(
            data_dict["data"]["author_id"], data_dict["includes"]["users"])

        tweet = data_dict["data"]["text"]
        tweet_id = data_dict["data"]["id"]

        return {
            "id": tweet_id,
            "text": tweet,
            "author_name": author_name
        }

    def __check_lan(self, data_lang):
        return True if data_lang in self.support_lang else False

    def __byte_to_json(self, data):
        # convert byte string to regular string
        json_string = data.decode('utf-8')
        json_obj = json.loads(json_string)

        return json_obj

    def __get_author(self, author_id, users):
        author_name = list(filter(
            lambda user: user['id'] == author_id, users))[0]["username"]
        return author_name
