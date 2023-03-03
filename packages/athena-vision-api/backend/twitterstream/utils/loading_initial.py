import joblib
from gensim.models import KeyedVectors
from django.conf import settings
from os import path


def loading_wordvec():
    print("\n\nLoading Word2vec....\n")
    BASE_DIR = settings.BASE_DIR

    path_to_vectors = path.join(
        BASE_DIR, "twitterstream", "static", "models", "word2vec.bin")

    wv = KeyedVectors.load_word2vec_format(
        path_to_vectors, binary=True)
    print("\nWord2vec Loaded\n")

    return wv


def loading_model():
    print("\n\nLoading model....\n")

    BASE_DIR = settings.BASE_DIR
    path_to_model = path.join(
        BASE_DIR, "twitterstream", "static", "models", "model.pkl")

    with open(path_to_model, 'rb') as f:
        svc_model = joblib.load(f)

    print(type(svc_model))
    print("\nModel Loaded\n")

    return svc_model


def loading_model_and_vector():
    model = loading_model()
    word2vec = loading_wordvec()

    scope = {}
    scope["model"] = model
    scope["word_vectors"] = word2vec

    return scope
