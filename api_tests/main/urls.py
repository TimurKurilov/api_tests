from user.views import UserDataView, UserDataUsernameView
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user_data', UserDataView)
router.register('user_data_username', UserDataUsernameView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
