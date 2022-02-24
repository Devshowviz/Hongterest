from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
   path('create/',ProfileCreateView.as_view(), name='create'),
   path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]