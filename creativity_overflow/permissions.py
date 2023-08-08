from rest_framework import permissions
from accounts.models import CustomUser

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # hover over SAFE_METHODS to see which qualify
        if request.method in permissions.SAFE_METHODS:
            print("request",request)
            return True

        # if we're allowing the purchaser to be null in Model
        # then this will check for that case and allow access

        if obj.artist_id is None:
            return True

        return obj.artist == request.user
    
class IsArtistOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user is an artist (assuming is_artist is a field in CustomUser)
        user = request.user
        return user.is_authenticated and user.is_artist

class IsOwnerArtist(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.artist_id == request.user.id
    
class IsAdminUsers(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_staff