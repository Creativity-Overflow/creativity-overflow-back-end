from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import CustomUser , Artist

# class SignUpView(CreateView):

#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"


@csrf_exempt
def signup(request):
    body = json.loads(request.body)
    user = CustomUser.objects.create(username = body['username'], email = body['email'])
    user.set_password(body['password'])
    user.save()
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def signup_artist(request):
    body = json.loads(request.body)
    user = Artist.objects.create(username = body['username'], email = body['email'])
    user.set_password(body['password'])
    user.save()
    return JsonResponse({'status': 'ok'})
