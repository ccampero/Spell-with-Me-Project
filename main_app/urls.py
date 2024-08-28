from django.urls import include, path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('spellers/', views.speller_index, name='speller-index'),
    path('spellers/<int:speller_id>/', views.speller_detail, name='speller-detail'),
    path('spellers/create/', views.SpellerCreate.as_view(), name='speller-create'),
    path('spellers/<int:pk>/update/', views.SpellerUpdate.as_view(), name='speller-update'),
    path('spellers/<int:pk>/delete/', views.SpellerDelete.as_view(), name='speller-delete'),
    path(
        'spellers/<int:speller_id>/add-study/', 
        views.add_study, 
        name='add-study'
    ),
    path('words/create/', views.WordCreate.as_view(), name='word-create'),
    path('words/<int:pk>/', views.WordDetail.as_view(), name='word-detail'),
    path('words/', views.WordList.as_view(), name='word-index'),
    path('words/<int:pk>/update/', views.WordUpdate.as_view(), name='word-update'),
    path('words/<int:pk>/delete/', views.WordDelete.as_view(), name='word-delete'),
    path('spellers/<int:speller_id>/associate-word/<int:word_id>/', views.associate_word, name='associate-word'),
    path('spellers/<int:speller_id>/remove-word/<int:word_id>/', views.remove_word, name='remove-word'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),

]