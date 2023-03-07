from django.apps import AppConfig
from .utils.loading_initial import loading_model_and_vector


class TwitterstreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitterstream'

    called_already = False

    def ready(self) -> None:

        # muted during debugging
        if not self.called_already:
            self.scope = loading_model_and_vector()
            self.called_already = True

        print("-------->READY<--------")

        return super().ready()
