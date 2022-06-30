from django.urls.conf import path
from app.views import login, logout, registratsiya, add, delete, edit, search, test, toplam, testqilish

urlpatterns = [
    path('testqilish/', testqilish, name='testqilish'),
    path('', login, name="login"),
    path('logout/', logout, name="logout"),
    path('registratsiya/', registratsiya, name="registratsiya"),
    # path('success', success, name='success'),

    path('add/', add, name="new_word"),
    path('delete/<int:pk>/', delete, name="delete_word"),
    path('edit/<int:pk>/', edit, name='edit_word'),
    path('search/', search, name='search_word'),
    path('test/', test, name='test'),
    path('toplam/', toplam, name='toplam')


]