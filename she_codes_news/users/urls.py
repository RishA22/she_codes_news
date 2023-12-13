from django.urls import path
from .views import CreateAccountView
from .views import AccountView
# Filter
from .views import user_profile

app_name ='users'

urlpatterns = [    
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    # 2 paths
    #Account View
    # path('account/', AccountView.as_view(), name='account')
    path('account/', AccountView.as_view(), name='account'),
    # Filter
    # path('profile/<str:username>/', user_profile, name='user_profile'),
    ]

