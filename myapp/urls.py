from . import views
from django.urls import path

urlpatterns = [    
	path('', views.index, name='index'),
    path('book-list', views.bookList, name='book-list'),
    path('book-create', views.bookCreate, name='book-create'),
    path('book-update/<int:id>', views.bookUpdate, name='book-update'),
    path('book-delete/<int:id>', views.bookDelete, name='book-delete'),

    path('person-list', views.personList, name='person-list'),    
    path('person-create', views.personCreate, name='person-create'),  
    path('person-update/<int:pk>', views.personUpdate, name='person-update'),
    path('person-delete/<int:pk>', views.personDelete, name='person-delete'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]