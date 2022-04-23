from django.urls import path

app_name = "search"

from products.views import (
                        SearchProductView, 
                    )
urlpatterns = [
    path('', SearchProductView.as_view(), name='list'),
]