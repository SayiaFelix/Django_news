from django.conf.urls import include,url
from my_app.views import *

urlpatterns = [
    # ... other urls
    url('app/', indexView),
    url('post/', create_post,name='create'),
    url('post/ajax/friend', postFriend, name = "post_friend"),
    url('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),
    # path("", FriendView.as_view(), name = "friend_cbv"),
    # ...
]