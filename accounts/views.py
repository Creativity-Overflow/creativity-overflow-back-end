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
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def signup_artist(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.is_artist=True
            user = form.save()
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

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