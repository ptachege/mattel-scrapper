
from django.urls import path
from . import views
app_name = 'imagerecovery'
urlpatterns = [
    path('', views.entry, name='entry'),
    path('fetchPrices/', views.fetchPrices, name='fetchPrices'),
    path('viewtires/', views.fetchAllTires, name='fetchAllTires'),
    path('donwload_csv/', views.donwload_csv, name='donwload_csv'),

    #
    path('fetch_theme_category/', views.fetch_theme_category,
         name='fetch_theme_category'),
    path('crawl_theme/', views.crawl_theme, name='crawl_theme'),
    path('viewlegos/', views.fetchAllLegos, name='fetchAllLegos'),
    path('donwload_csv_legos/', views.donwload_csv_legos,
         name='donwload_csv_legos'),

]
