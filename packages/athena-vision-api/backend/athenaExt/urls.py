from django.urls import path
from .views import UpdateSetting, ExtPowerSetting

app_name = "athenaExt"

urlpatterns = [
    path("setting/", UpdateSetting.as_view(), name="setting"),
    path("extPower/", ExtPowerSetting.as_view(), name="extpower")
]
