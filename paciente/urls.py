from django.urls import path
from . import views

app_name = "paciente"

urlpatterns = [
    # ex: /paciente/
    path("", views.PacienteListView.as_view(), name="index"),

    # ex: /paciente/create/
    path("create", views.PacienteCreateView.as_view(), name="create"),

    # ex: /paciente/3/
    path("<int:pk>/", views.PacienteDetailView.as_view(), name="detail"),

    # ex: /paciente/update/3
    path("update/<int:pk>", views.PacienteUpdateView.as_view(), name="update"),

    # ex: /paciente/delete/3
    path("delete/<int:pk>", views.PacienteDeleteView.as_view(), name="delete"),
]
