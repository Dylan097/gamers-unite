from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('new_post/', views.NewPost.as_view(), name='new_post'),
    path('share_post/<int:id>', views.SharePost.as_view(), name='share'),
    path('like/<int:id>', views.PostLike.as_view(), name='post_like'),
    path('follow/<int:id>/<int:post_id>', views.FollowUser.as_view(), name='follow'),
    path('edit/<int:id>', views.EditPost.as_view(), name='edit_post'),
    path('post/<int:id>/<int:comment_id>', views.EditComment.as_view(), name='edit_comment'),
    path('delete/<int:id>/<int:comment_id>/<str:model>', views.Delete.as_view(), name='delete')
]
