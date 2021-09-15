from django.http import JsonResponse


def index(request):
    return JsonResponse({'success': 'your are on the main'})
