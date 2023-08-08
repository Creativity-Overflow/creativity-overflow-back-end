from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import CustomUser

@csrf_exempt
def signup(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user = CustomUser.objects.create(username=body['username'], email=body['email'])
        user.set_password(body['password'])
        user.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def signup_artist(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user = CustomUser.objects.create(username=body['username'], email=body['email'], is_artist=True)
        user.set_password(body['password'])
        user.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Method not allowed'}, status=405)
