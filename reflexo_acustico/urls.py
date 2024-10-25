from django.urls import path
from . import views

app_name = "reflexo_acustico"

urlpatterns = [
    # ex: /reflexo_acustico/
    path("", views.ReflexoAcusticoListView.as_view(), name="index"),

    # ex: /reflexo_acustico/create/
    path("create", views.ReflexoAcusticoCreateView.as_view(), name="create"),

    # ex: /reflexo_acustico/3/
    path("<int:pk>/", views.ReflexoAcusticoDetailView.as_view(), name="detail"),

    # ex: /reflexo_acustico/update/3
    path("update/<int:pk>", views.ReflexoAcusticoUpdateView.as_view(), name="update"),

    # ex: /reflexo_acustico/delete/3
    path("delete/<int:pk>", views.ReflexoAcusticoDeleteView.as_view(), name="delete"),
]
