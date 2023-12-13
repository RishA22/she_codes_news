from django.urls import path
from . import views
# from .views import stories_by_author
# from .views import edit_story
# Author's view
# from .views import AccountView

app_name = 'news'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index')
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.StoryView.as_view(), name='story')
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'), #Changes name to create_story
    path('add-story/', views.AddStoryView.as_view(), name='create_story'),
    # EditStoryFeature
    path('edit-story/<int:pk>/', views.edit_story, name='edit_story'),
    #Account View
    # path('account/', views.AccountView.as_view(), name='account')
    # Add the new pattern for viewing stories by author
    # path('author/<str:username>/', stories_by_author, name='stories_by_author')
]

