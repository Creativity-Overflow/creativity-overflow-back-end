from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import CustomUser
from decimal import Decimal

@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            email = data.get('email')
            password = data.get('password1')
            
            user = CustomUser.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            return JsonResponse({'message': 'User created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt
def signup_artist(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            email = data.get('email')
            password = data.get('password1')
            
            user = CustomUser.objects.create(username=username, email=email)
            user.is_artist = True
            user.set_password(password)
            user.save()

            return JsonResponse({'message': 'User created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt
def update_credits(request):
    if request.method == "PUT":
        body = json.loads(request.body)
        user = request.user
        try:
            instance = CustomUser.objects.get(id=user.id)
            credits_value = body.get('credits')  # Use dictionary.get() to safely get the value
            if credits_value is not None:
                instance.credits = Decimal(credits_value)
                instance.save()
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'error': 'Invalid credits value'}, status=400)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)