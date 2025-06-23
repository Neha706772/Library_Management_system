
from django.contrib import admin
from django.urls import path
from library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Booklist_view.as_view(),name='home'),
    path('book/<int:pk>/', views.BookDetails_view.as_view(), name='book-detail'),
    path('insert/', views.BookCreate_view.as_view(), name='insert'),
    path('update/<int:pk>/', views.BookUpdate_view.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookDelete_view.as_view(), name='delete'),

]
