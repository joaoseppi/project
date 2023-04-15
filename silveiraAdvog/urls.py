from django.urls import path


from silveiraAdvog.views import home


urlpatterns = [
    path('', home),
]
