from django.http import JsonResponse

from telegram.tasks import send_message


def index(request):
    send_message.delay('It works!')
    return JsonResponse({"success": True})
