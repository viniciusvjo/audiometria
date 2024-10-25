from django.urls import path
from . import views

app_name = "grau_perda"

urlpatterns = [
    # ex: /grau_perda/
    path("", views.GrauPerdaListView.as_view(), name="index"),

    # ex: /grau_perda/create/
    path("create", views.GrauPerdaCreateView.as_view(), name="create"),

    # ex: /grau_perda/3/
    path("<int:pk>/", views.GrauPerdaDetailView.as_view(), name="detail"),

    # ex: /grau_perda/update/3
    path("update/<int:pk>", views.GrauPerdaUpdateView.as_view(), name="update"),

    # ex: /grau_perda/delete/3
    path("delete/<int:pk>", views.GrauPerdaDeleteView.as_view(), name="delete"),
]
