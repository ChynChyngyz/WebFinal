from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from authUser import views

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('current-user/', views.CurrentUserView.as_view(), name='current_user'),
    path('all-users/', views.AllUsersView.as_view(), name='all_users')
]
