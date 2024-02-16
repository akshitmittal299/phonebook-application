from django.urls import path
from . import views
urlpatterns=[
    path('update/<int:contact_id>/',views.update, name="update_contact"),
    path('contacts/', views.contacts , name="contacts"),
    path('add_contact/' ,views.add_contact,name='add_contact'),
    path('delete/<int:contact_id>/',views.delete, name='delete'),
    path('search_contact/',views.search_contact, name='search_contact'),
    path("",views.index,name = "home")
]
