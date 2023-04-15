from django.urls import path


from recipes.views import home, contato, sobre


urlpatterns = [
    path('recipes/', home),
    path('recipes/sobre/', sobre),
    path('recipes/contato/', contato),
]
