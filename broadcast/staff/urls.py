from django.urls import path, include
from staff.views import dashboard, publishView

urlpatterns = [
    path('dashboard/',dashboard),
    path('publish/',publishView),
]