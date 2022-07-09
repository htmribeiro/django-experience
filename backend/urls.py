from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('', include('backend.todo.urls', namespace='todo')),
    path('admin/', admin.site.urls),
]
