from django.apps import AppConfig
from .utils.loading_initial import loading_model_and_vector


class TwitterstreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitterstream'

    def ready(self) -> None:

        # muted during debugging
        self.scope = loading_model_and_vector()
        print("-------->ready<--------")
        
        return super().ready()
