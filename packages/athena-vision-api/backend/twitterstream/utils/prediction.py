from django.apps import apps
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline


class Prediction:
    def __init__(self) -> None:
        self.model, self.word_vectors = apps.get_app_config(
            "twitterstream").scope.values()

        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words("english"))

        # Initial transformer here

# Public methods:

    # Method to predict hate speech
    def predict_hate(self, tweet_text):
        production_pipeline = self.__create_pipeline()
        full_pipeline = Pipeline([
            ("convert_to_series", FunctionTransformer(self.__convert_to_series)),
            ("preprocessing", production_pipeline),
            ("svm_model", self.model)
        ])
        return full_pipeline.predict(tweet_text)[0]

# Private methods:

    # Method to create hatespeech pipeline
    def __create_pipeline(self, production_mode=True, y=None):
        if not production_mode and type(y) == type(None):
            raise Exception(
                "Cannot run in train/test model with target values")

        return Pipeline([
            ("clean", FunctionTransformer(self.__clean)),
            ("preprocessing", FunctionTransformer(self.__text_preprocessing)),
            ("drop_empty", FunctionTransformer(self.__remove_empty_vectors,
             kw_args={"production_mode": production_mode, "y": y})),
            ("mean_pooling", FunctionTransformer(self.__mean_pooling,
             kw_args={"production_mode": production_mode})),
        ])

    # Methods for hate classification pipeline
    def __convert_to_series(self, tweet_texts):
        return pd.Series(tweet_texts)

    def __tokenizer(self, tweet):
        return word_tokenize(tweet)

    def __remove_url_mentions_hashtags(self, tweet_tokens):
        return [token for token in tweet_tokens
                if not token.startswith("http")
                and not token.startswith("@")
                and not token.startswith("#")]

    def __lowercaseing(self, tweet_tokens):
        return [token.lower() for token in tweet_tokens]

    def __remove_punctuation(self, tweet_tokens):
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        return [token for token in tweet_tokens if token not in punctuations]

    def __stemming(self, tweet_tokens):
        return [self.stemmer.stem(token) for token in tweet_tokens]

    def __remove_stopwords(self, tweet_tokens):
        return [token for token in tweet_tokens if token not in self.stop_words]

    def __clean(self, tweet):
        tweet = tweet.apply(lambda t: self.__tokenizer(t))
        tweet = tweet.apply(lambda t: self.__remove_url_mentions_hashtags(t))
        tweet = tweet.apply(lambda t: self.__lowercaseing(t))
        tweet = tweet.apply(lambda t: self.__remove_punctuation(t))
        tweet = tweet.apply(lambda t: self.__stemming(t))
        tweet = tweet.apply(lambda t: " ".join(self.__remove_stopwords(t)))
        return tweet

    def __text_preprocessing(self, tweets):
        tweets = tweets.apply(lambda tweet: [self.word_vectors[token]
                                             for token in tweet.split() if token in self.word_vectors])
        return tweets

    def __remove_empty_vectors(self, X, production_mode=True, y=None):
        mask = X.apply(lambda x: len(x) == 0)
        X = X[~mask]

        if production_mode:
            return X

        y = y[~mask]
        return X, y

    def __mean_pooling(self, vector, production_mode=True):
        if production_mode:
            mean_vectors = vector.apply(lambda vec: np.mean(vec, axis=0))
            return pd.DataFrame(mean_vectors.tolist())

        X = vector[0]
        y = vector[1]
        X = X.apply(lambda vec: np.mean(vec, axis=0))
        return X, y
