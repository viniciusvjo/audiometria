from django.urls import path
from . import views

app_name = "classificacao_iprf"

urlpatterns = [
    # ex: /classificacao_iprf/
    path("", views.ClassificacaoIPRFListView.as_view(), name="index"),

    # ex: /classificacao_iprf/create/
    path("create", views.ClassificacaoIPRFCreateView.as_view(), name="create"),

    # ex: /classificacao_iprf/3/
    path("<int:pk>/", views.ClassificacaoIPRFDetailView.as_view(), name="detail"),

    # ex: /classificacao_iprf/update/3
    path("update/<int:pk>", views.ClassificacaoIPRFUpdateView.as_view(), name="update"),

    # ex: /classificacao_iprf/delete/3
    path("delete/<int:pk>", views.ClassificacaoIPRFDeleteView.as_view(), name="delete"),
]
