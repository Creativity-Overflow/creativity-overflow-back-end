from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import jwt
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
            image=data.get('image')
            credits = Decimal(data.get('credits', "10000.00"))
            
            user = CustomUser.objects.create(username=username, email=email)
            user.set_password(password)
            user.image=image
            user.credits=credits
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
            credits = Decimal(data.get('credits', "10000.00"))

            user = CustomUser.objects.create(username=username, email=email)
            user.is_artist = True
            user.set_password(password)
            user.credits=credits
            user.save()

            return JsonResponse({'message': 'User created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt
def update_credits(request, pk):
    if request.method == "PUT":
        body = json.loads(request.body)
        
        try:
            instance = CustomUser.objects.get(id=pk)
            
            credits_value = Decimal(body.get('credits', "10000.00"))
            instance.credits = credits_value
            instance.save()            
            return JsonResponse({'status': 'ok'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)