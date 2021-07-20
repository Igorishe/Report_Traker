from django.http import JsonResponse

from telegram.tasks import send_notify


def index(request):
    send_notify.delay('It works!')
    return JsonResponse({"success": True})
