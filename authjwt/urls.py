
from django.urls import path
from .views import CadasterView, LoginView, DeleteView, EditView, VerifyEmailView

urlpatterns = [
    path("cadaster/", CadasterView.as_view(), name="cadaster"),
    path("login/", LoginView.as_view(), name="login"),
    path("delete/", DeleteView.as_view(), name="delete"),
    path("edit/", EditView.as_view(), name="edit"),
    path("verify/", VerifyEmailView.as_view(), name="verify")
]