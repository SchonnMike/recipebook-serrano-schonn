from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list/", views.basicParams, name="basicParams"),
    path("recipe/<int:num>/", views.tasks, name="tasks"),
    path("recipe/add/", views.add_recipe, name="add_recipe"),
    path("recipe/<int:pk>/add_image", views.add_image, name="add_image"),
]

app_name = "ledger"
