from django.urls import path
from .views import *

urlpatterns = [
    path('login/',Login,name='login'),
    path('signup/',Signup,name='signup'),
    path('logout/',Logout,name='logout'),
    path('editProfile/',EditProfile,name='editProfile'),
    path('userProfile/',UserAccount,name='userProfile'),
    path('uploadVideo/',UploadVideo,name='uploadVideo'),
    path('videoDisplay/<int:videoId>/',VideoDisplay,name='videoDisplay'),
    path('editUploadedVideo/<int:videoId>/',EditUploadedVideo,name='editUploadedVideo'),
    path('displayVideoUser/<int:userId>/',DisplayVideoUser,name='displayVideoUser'),
    path('like/',LikeVideoView,name='like_video'),
    path('liked_videos/',UserLikedVideos,name='likedVideos'),
    path('watch-later/',WatchLaterVideos,name='watch_later'),
    path('watchLaterVideos/',UserWatchLaterVideos,name='watchLaterVideos'),
    path('playlist',UserPlaylist,name='playlist'),
    path('playlistVid/<int:playlistId>/',UserPLaylistVid,name='playlistVid'),
    path('addVidToPlaylist/<int:playlistId>/<int:videoId>/',AddVidToPlayList,name='addVidToPlaylist'),
    path('createPlaylist/',CreatePlaylist,name='createPlaylist'),
    path('educationCat',EducationCat,name='educationCat'),
    path('gamesCat',GamesCat,name='gamesCat'),
    path('musicCat',MusicCat,name='musicCat'),
    path('moviesCat',MoviesCat,name='moviesCat'),
    path('fashionCat',FashionCat,name='fashionCat'),
    path('search/',Search,name='search'),
    path('trending/',Trending,name='trending'),
    path('search2/',SearchSecond,name='search2'),
    path('history/',History,name='history'),
    path('themes/',Themes,name='themes')

]