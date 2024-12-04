from django.urls import path
from .views import (
    home_view, articles_view,
    article_detail_view, about_view, contact_view, category_view
)

urlpatterns = [
    path('', home_view),
    path('articles/', articles_view),
    path('articles/<int:pk>/', article_detail_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('category/<str:category_name>/', category_view)
]