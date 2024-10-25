from django.urls import path
from . import views

app_name = "tipo_perda_auditiva"

urlpatterns = [
    # ex: /tipo_perda_auditiva/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /tipo_perda_auditiva/3/
    path("<int:pk>/", views.TipoDetailView.as_view(), name="detail"),
    # ex: /tipo_perda_auditiva/create/
    path("create", views.createView, name="create"),
    path("delete/<int:pk>", views.TipoDeleteView.as_view(), name="delete"),
    path("update/<int:pk>", views.TipoUpdateView.as_view(), name="update"),
]
