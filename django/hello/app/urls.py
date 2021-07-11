from django.urls import path, include

import app.views

urlpatterns = [
    path('hello/', app.views.hello_world),
    path('content/', app.views.content),
]






