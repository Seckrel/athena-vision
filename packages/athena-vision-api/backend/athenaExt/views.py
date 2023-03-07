from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# method_decorator(csrf_exempt, name="updateSetting")
class UpdateSetting(APIView):
    def get(self, request):
        data = {
            'emotional tone': 0,
            'topic label': 0,
            "blur": 0,
            "strength": '1',
        }

        self.__set_session_setting(request, data)
        cache.set("ext_power", 0)

        return Response(data)

    def post(self, request):
        data = request.data
        self.__set_session_setting(request, data)

        for key in ["blur", "emotional tone", "topic label", "strength"]:
            val = request.session.get(key)
            print(f"{key}->{val}")

        return Response(status=200)

    def __set_session_setting(self, request, data):
        request.session["blur"] = data["blur"]
        request.session["emotional tone"] = data["emotional tone"]
        request.session["topic label"] = data["topic label"]
        request.session["strength"] = data["strength"]
        cache.set('session', request.session)


# method_decorator(csrf_exempt, name="extPowerSetting")
class ExtPowerSetting(APIView):
    def post(self, request):
        extFlag = request.data
        request.session["ext_power"] = extFlag
        cache.set("ext_power", extFlag)

        if not extFlag:
            return redirect("athenaExt:setting")
        else:
            request.session["blur"] = 1
            request.session["emotional tone"] = 0
            request.session["topic label"] = 0
            request.session["strength"] = "1"

        cache.set("session", request.session)
        for key in ["blur", "emotional tone", "topic label", "strength"]:
            val = request.session.get(key)
            print(f"{key}->{val}")

        return Response({"blur": 1, "extOn": True, "strength": "1"}, status=200)
