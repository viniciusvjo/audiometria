from django.urls import path
from . import views

app_name = "configuracao_audiometrica"

urlpatterns = [
    # ex: /configuracao_audiometrica/
    path("", views.ConfiguracaoAudiometricaListView.as_view(), name="index"),

    # ex: /configuracao_audiometrica/create/
    path("create", views.ConfiguracaoAudiometricaCreateView.as_view(), name="create"),

    # ex: /configuracao_audiometrica/3/
    path("<int:pk>/", views.ConfiguracaoAudiometricaDetailView.as_view(), name="detail"),

    # ex: /configuracao_audiometrica/update/3
    path("update/<int:pk>", views.ConfiguracaoAudiometricaUpdateView.as_view(), name="update"),

    # ex: /configuracao_audiometrica/delete/3
    path("delete/<int:pk>", views.ConfiguracaoAudiometricaDeleteView.as_view(), name="delete"),
]
