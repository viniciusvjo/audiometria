from django.urls import path
from . import views

app_name = "timpanograma"

urlpatterns = [
    # ex: /timpanograma/
    path("", views.TimpanogramaListView.as_view(), name="index"),

    # ex: /timpanograma/create/
    path("create", views.TimpanogramaCreateView.as_view(), name="create"),

    # ex: /timpanograma/3/
    path("<int:pk>/", views.TimpanogramaDetailView.as_view(), name="detail"),

    # ex: /timpanograma/update/3
    path("update/<int:pk>", views.TimpanogramaUpdateView.as_view(), name="update"),

    # ex: /timpanograma/delete/3
    path("delete/<int:pk>", views.TimpanogramaDeleteView.as_view(), name="delete"),
]
