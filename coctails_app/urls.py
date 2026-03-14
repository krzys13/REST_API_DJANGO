from django.urls import path

from . import views

urlpatterns = [
    path("coctail/", views.coctail_list, name="coctail_list"),
    path("coctail/<int:coctail_id>/detail", views.coctail_detail, name = "coctail_detail"),
    path("coctail/create", views.coctail_create, name="coctail_create"),
    path("coctail/insert", views.coctail_insert, name="coctail_insert"),
    #path("coctail/<int:coctail_id>/edit", views.coctail_edit, name = "coctail_edit"),
]