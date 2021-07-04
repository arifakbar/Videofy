from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse,reverse_lazy
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Home(request):

    allVideos = UserVideo.objects.order_by('?').all()
    
    trending5 = UserVideo.objects.filter(trendingTop5=True)
    
    d={'allVideos':allVideos,'trending5':trending5}

    if request.user.is_authenticated:
        playlist = UserPlayList.objects.filter(user=request.user).all()

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('home')

        d={'allVideos':allVideos,'playlist':playlist,'trending5':trending5}

    return render(request,'allDisplay.html',d)

def Logout(request):
    logout(request)
    return redirect('home')

def Login(request):
    errorLogin = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            errorLogin = True
    d = {'errorLogin':errorLogin}        
    return render(request,'login.html',d)

def Signup(request):
    errorUser = False
    errorPass = False

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        check = User.objects.filter(username = username)

        if check:
            errorUser = True
        elif password != cpassword:
            errorPass = True
        else:
            User.objects.create_user(username=username,email=email,password=password,is_staff=False)
            user = authenticate(username=username,password=password)
            UserProfile.objects.create(user=user)
            login(request,user)
            return redirect('home')
    d = {'errorPass':errorPass,'errorUser':errorUser}                
    return render(request,'signup.html',d)      

def UserAccount(request):

    if not request.user.is_authenticated:
        return redirect('home')

    video = UserVideo.objects.filter(user=request.user)

    if 'delVid' in request.POST:
        UserVideo.objects.filter(id = request.POST['delVid']).delete()

    d = {'video':video}
    return render(request,'account.html',d)

def EditProfile(request):

    if not request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        about = request.POST['about']
        if len(request.FILES) != 0:
            profilePic = request.FILES['profilePic']
            if profilePic:
                user = UserProfile.objects.get(user=request.user)
                user.profilePic = profilePic
                user.save()
        if about:
            UserProfile.objects.filter(user=request.user).update(about=about)
        if username:
            owner = User.objects.get (id=request.user.id)
            owner.username = username
            owner.save() 
        return redirect('userProfile')            

    return render(request,'editProfile.html')

def UploadVideo(request):
    
    if not request.user.is_authenticated:
        return redirect('home')
    
    cat = list(map(list,UserVideo.videoCat))

    if request.method == 'POST':
        vidName = request.POST['vidName']
        vidFile = request.FILES['vidFile']
        vidPoster = request.FILES['vidPoster']
        vidCat = request.POST.getlist('vidCat')
        vidDes = request.POST['vidDes']
        UserVideo.objects.create(user=request.user,video=vidFile,videoName=vidName,videoPic=vidPoster,description=vidDes,category=vidCat)

        return redirect('userProfile')

    d = {'cat':cat}    
    return render(request,'uploadVideo.html',d)

def VideoDisplay(request,videoId):
    
    video = UserVideo.objects.filter(id=videoId).first()
    comment = Comments.objects.filter(video=video,reply=None).order_by('-id')

    if request.user.is_authenticated:
        video.history.add(request.user)

    liked = False
    if video.likes.filter(id = request.user.id):
        liked = True

    disliked = False
    if video.dislikes.filter(id = request.user.id):
        disliked = True

    watchLater = False
    if video.watchLater.filter(id = request.user.id):
        watchLater = True    

    if request.method == "POST":
        content = request.POST.get('content')
        reply_id = request.POST.get('comment_id')
        comment_qs = None
        if reply_id:
            comment_qs = Comments.objects.get(id = reply_id)
        newComment = Comments.objects.create(user=request.user,video=video,content=content,reply=comment_qs)
        newComment.save()

    vCat = video.category
    vList = list(vCat)

    for k in vList:
        relatedVideo = UserVideo.objects.filter(Q(category__icontains = k) | Q(videoName__icontains = video.videoName)).exclude(id=video.id)

    total_likes = video.total_like()
    total_dislikes = video.total_dislike()
    d = {'video':video,'relatedVideo':relatedVideo,'total_likes':total_likes,'total_dislikes':total_dislikes,'liked':liked,'disliked':disliked,'watchLater':watchLater,'comment':comment}
    
    
    if request.user.is_authenticated:
        playlist = UserPlayList.objects.filter(user=request.user).all()
        d = {'video':video,'relatedVideo':relatedVideo,'total_likes':total_likes,'total_dislikes':total_dislikes,'liked':liked,'disliked':disliked,'watchLater':watchLater,'playlist':playlist,'comment':comment}
    
    if request.is_ajax():
        html = render_to_string('comment_section.html',d,request=request)
        return JsonResponse({'form':html})
    
    return render(request,'videoSingle.html',d)

def LikeVideoView(request):

    if not request.user.is_authenticated:
        return redirect('signup')

    liked = False
    disliked = False

    if 'likeVid' in request.POST:
        video = UserVideo.objects.filter(id=request.POST.get('likeVid')).first()
        if video.likes.filter(id = request.user.id):
            video.likes.remove(request.user)
            liked = False
        else:    
            video.likes.add(request.user)
            liked = True
        if video.dislikes.filter(id = request.user.id):
            video.dislikes.remove(request.user)

        d = {
            'video':video,
            'liked':liked,
            'total_dislikes': video.total_dislike(),
            'total_likes': video.total_like()
        }
        if request.is_ajax():
            html = render_to_string('like_section.html',d,request=request)
            return JsonResponse({'form':html})
        # return HttpResponseRedirect(reverse('videoDisplay' , args=str(videoId)))

    if 'dislikeVid' in request.POST:
        video = UserVideo.objects.filter(id=request.POST.get('dislikeVid')).first()
        if video.dislikes.filter(id = request.user.id):
            video.dislikes.remove(request.user)
            disliked = False
        else:    
            video.dislikes.add(request.user)
            disliked = True
        if video.likes.filter(id = request.user.id):
            video.likes.remove(request.user)

        d = {
            'video':video,
            'disliked':disliked,
            'total_likes': video.total_like(),
            'total_dislikes': video.total_dislike()
        }  
        if request.is_ajax():
            html = render_to_string('like_section.html',d,request=request)
            return JsonResponse({'form':html})  
        # return HttpResponseRedirect(reverse('videoDisplay' , args=str(videoId)))

def WatchLaterVideos(request):

    if not request.user.is_authenticated:
        return redirect('signup')
    
    watchLater = False
    # playlist = UserPlayList.objects.filter(user=request.user).all()
    if 'watchVidLater' in request.POST:
        video = UserVideo.objects.filter(id=request.POST.get('watchVidLater')).first()
        if video.watchLater.filter(id = request.user.id):
            video.watchLater.remove(request.user)
            watchLater = False
        else:    
            video.watchLater.add(request.user)
            watchLater = True
        d = {
            'video':video,
            'watchLater':watchLater,
            # 'playlist':playlist
        }    
    if request.is_ajax():
        html = render_to_string('watchlater_section.html',d,request=request)
        return JsonResponse({'form':html})          
        # return HttpResponseRedirect(reverse('videoDisplay' , args=str(videoId)))        

def EditUploadedVideo(request,videoId):

    if not request.user.is_authenticated:
        return redirect('home')
    cat = list(map(list,UserVideo.videoCat))

    video = UserVideo.objects.filter(id = videoId).first()

    if request.method == 'POST':
        vidName = request.POST['vidName']
        vidCat = request.POST.getlist('vidCat')
        vidDes = request.POST['vidDes']
        if len(request.FILES) != 0:
            vidPoster = request.FILES['vidPoster']
            if vidPoster:
                user = UserVideo.objects.get(user=request.user)
                user.videoPic = vidPoster
                user.save()
        if vidName:
            UserVideo.objects.filter(user=request.user).update(videoName=vidName)
        if vidCat:
            UserVideo.objects.filter(user=request.user).update(category=vidCat)
        if vidDes:                
            UserVideo.objects.filter(user=request.user).update(description=vidDes)
        return redirect('userProfile')
                
    d = {'video':video,'cat':cat}
    return render(request,'editUploadedVideo.html',d)    

def DisplayVideoUser(request,userId):
    vidUser  = User.objects.filter(id = userId).first()
    video = UserVideo.objects.filter(user=vidUser)
    d = {'vidUser':vidUser,'video':video}
    return render(request,'displayVideoUser.html',d)  

def UserLikedVideos(request):

    if not request.user.is_authenticated:
        return redirect('home')

    likedVid = UserVideo.objects.filter(likes__id = request.user.id).all().order_by('-id')

    if 'RemoveLike' in request.POST:
        video = UserVideo.objects.filter(id = request.POST.get('RemoveLike')).first()
        video.likes.remove(request.user)
        return redirect('likedVideos')

    if 'AddWatchLater' in request.POST:
        video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
        video.watchLater.add(request.user)
        return redirect('likedVideos')
    
    d = {'likedVid':likedVid}
    return render(request,'likedVid.html',d)     

def UserWatchLaterVideos(request):

    if not request.user.is_authenticated:
        return redirect('home')

    watchLaterVid = UserVideo.objects.filter(watchLater__id = request.user.id).all().order_by('-id')

    if 'RemoveWatchLater' in request.POST:
        video = UserVideo.objects.filter(id = request.POST.get('RemoveWatchLater')).first()
        video.watchLater.remove(request.user)
        return redirect('watchLaterVideos')

    if 'AddLike' in request.POST:
        video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
        video.likes.add(request.user)
        return redirect('watchLaterVideos')


    d = {'watchLaterVid':watchLaterVid}
    return render(request,'watchLaterView.html',d) 

def UserPlaylist(request):

    playlist = UserPlayList.objects.filter(user=request.user).all().order_by('-id')


    if 'createPlayList' in request.POST:
        playlistName = request.POST['playlistName']
        playlistDesc = request.POST['playlistDesc']
        if len(request.FILES) != 0:
            playlistPic = request.FILES['playlistPic']
            if playlistPic:
               playlist.create(name=playlistName,user=request.user,playlistPic=playlistPic,description=playlistDesc)
               return redirect('playlist')
        else:
             playlist.create(name=playlistName,user=request.user,description=playlistDesc)
             return redirect('playlist')  

    if 'deletePLaylist' in request.POST:
        UserPlayList.objects.filter(id = request.POST.get('deletePLaylist')).delete()               

    d = {'playlist':playlist}

    return render(request,'demoPlayList.html',d)

def UserPLaylistVid(request,playlistId):

    playlist = UserPlayList.objects.filter(user=request.user,id=playlistId).first()
    playlistVid = playlist.videos.all().order_by('-id')

    if 'removeVid' in request.POST:
        playlist.videos.remove(request.POST.get('removeVid'))
            
    d = {'playlistVid':playlistVid}

    return render(request,'demoPlaylistVid.html',d)   

def CreatePlaylist(request):

    if not request.user.is_authenticated:
        return redirect('signup')

    playlist = UserPlayList.objects.filter(user=request.user).all()    

    if 'createPlayList' in request.POST:
        playlistName = request.POST['playlistName']
        playlistDesc = request.POST['playlistDesc']
        if len(request.FILES) != 0:
            playlistPic = request.FILES['playlistPic']
            if playlistPic:
               playlist.create(name=playlistName,user=request.user,playlistPic=playlistPic,description=playlistDesc)
               return redirect('playlist')
        else:
             playlist.create(name=playlistName,user=request.user,description=playlistDesc)
             return redirect('playlist')    

    return render(request,'createPlaylist.html')

def AddVidToPlayList(request,playlistId,videoId):

    playlist = UserPlayList.objects.filter(user=request.user,id=playlistId).first()
    video = UserVideo.objects.filter(id = videoId).first()
    playlist.videos.add(video)
    # if request.is_ajax():
    #     html = render_to_string('watchlater_section.html',request=request)
    #     return JsonResponse({'form':html})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # Convert this to ajax

def EducationCat(request):
    video = UserVideo.objects.filter(category__contains = 'Education')
    
    if request.user.is_authenticated:
        if 'AddLike' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
            video.likes.add(request.user)
            return redirect('educationCat')

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('educationCat')    

    d = {'video':video}
    return render(request,'EducationCat.html',d)

def FashionCat(request):
    video = UserVideo.objects.filter(category__contains = 'Fashion')
    
    if request.user.is_authenticated:
        if 'AddLike' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
            video.likes.add(request.user)
            return redirect('fashionCat')

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('fashionCat')    

    d = {'video':video}
    return render(request,'FashionCat.html',d)

def GamesCat(request):
    video = UserVideo.objects.filter(category__contains = 'Gaming')
    
    if request.user.is_authenticated:
        if 'AddLike' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
            video.likes.add(request.user)
            return redirect('gamesCat')

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('gamesCat')    

    d = {'video':video}
    return render(request,'GamesCat.html',d)

def MusicCat(request):
    video = UserVideo.objects.filter(category__contains = 'Music')
    
    if request.user.is_authenticated:
        if 'AddLike' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
            video.likes.add(request.user)
            return redirect('musicCat')

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('musicCat')    

    d = {'video':video}
    return render(request,'MusicCat.html',d)

def MoviesCat(request):
    video = UserVideo.objects.filter(category__contains = 'Movies')
    
    if request.user.is_authenticated:
        if 'AddLike' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
            video.likes.add(request.user)
            return redirect('moviesCat')

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('moviesCat')    

    d = {'video':video}
    return render(request,'MoviesCat.html',d)                

def Trending(request):
    video = UserVideo.objects.filter(trending=True)
    
    if request.user.is_authenticated:
        if 'AddLike' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddLike')).first()      
            video.likes.add(request.user)
            return redirect('trending')

        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user)
            return redirect('trending')    

    d = {'video':video}
    return render(request,'trending.html',d)                


def Search(request):
    query = request.GET['query']
    if query == "":
        videos = 0
    else:    
        videos = UserVideo.objects.filter(Q(videoName__icontains = query) | Q(category__icontains = query)) 
    d = {'videos':videos}
    if request.user.is_authenticated:
        playlist = UserPlayList.objects.filter(user=request.user).all()
        d = {'playlist':playlist,'videos':videos}
    return render(request,'search.html',d)

def SearchSecond(request):
    queries = request.GET['queries']
    if queries == "":
        videos = 0
    else: 
        videos = UserVideo.objects.filter(Q(videoName__icontains = queries) | Q(category__icontains = queries))
    d = {'videos':videos}
    if request.user.is_authenticated:
        playlist = UserPlayList.objects.filter(user=request.user).all()
        if 'AddWatchLater' in request.POST:
            video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
            video.watchLater.add(request.user) 
            d = {'playlist':playlist,'videos':videos}
    return render(request,'search.html',d)       

def History(request):

    if not request.user.is_authenticated:
        return redirect('signup')

    HistoryVid = UserVideo.objects.filter(history__id = request.user.id)

    if 'RemoveFromHistory' in request.POST:
        video = UserVideo.objects.filter(id = request.POST.get('RemoveFromHistory')).first()
        video.history.remove(request.user)
        return redirect('history')

    if 'AddWatchLater' in request.POST:
        video = UserVideo.objects.filter(id = request.POST.get('AddWatchLater')).first()      
        video.watchLater.add(request.user)
        return redirect('history')

    # if 'clearHistory' in request.POST:
        

    d = {'HistoryVid':HistoryVid}

    return render(request,'history.html',d)


def Themes(request):

    if not request.user.is_authenticated:
        return redirect('home')

    return render(request,'themes.html')    