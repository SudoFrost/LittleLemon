from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tabels', views.BookingViewSet, basename='tabels')

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', include(router.urls)),
]
