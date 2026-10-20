from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Set up the DRF router
router = DefaultRouter()
router.register(r'api/notes', views.NoteViewSet, basename='api-note')

urlpatterns = [
    # ... keep your existing paths ...
    
    # Include the generated API routes
    path('', include(router.urls)),
]