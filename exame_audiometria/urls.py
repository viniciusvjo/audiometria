from django.urls import path
from . import views

app_name = "exame_audiometria"

urlpatterns = [
    # ex: /exame_audiometria/
    path("", views.ExameAudiometriaListView.as_view(), name="index"),

    # ex: /exame_audiometria/create/
    path("create", views.ExameAudiometriaCreateView.as_view(), name="create"),

    # ex: /exame_audiometria/3/
    path("<int:pk>/", views.ExameAudiometriaDetailView.as_view(), name="detail"),

    # ex: /exame_audiometria/update/3
    path("update/<int:pk>", views.exame_audiometria_update, name="update"),
    #path("update/<int:pk>", views.ExameAudiometriaUpdateView.as_view(), name="update"),

    # ex: /exame_audiometria/delete/3
    path("delete/<int:pk>", views.ExameAudiometriaDeleteView.as_view(), name="delete"),

    path("export-pdf", views.export_pdf, name="export-pdf"),

    path("search/", views.Search.as_view(), name="search"),
]
