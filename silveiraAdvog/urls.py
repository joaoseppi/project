from django.urls import path


from silveiraAdvog.views import home, cadastro, login


urlpatterns = [
    path('', home),
    path('cadastro/', cadastro),
    path('login/', login)
]
