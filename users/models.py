from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from multiselectfield import MultiSelectField

# Create your models here.

class UserVideo(models.Model):
    videoCat = (
        ('Music','Music'),
        ('Movies','Movies'),
        ('Gaming','Gaming'),
        ('Education','Education'),
        ('Fashion','Fashion'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,default=1)
    video = models.FileField(null=True,blank=True)
    videoName = models.CharField(max_length=50,null=True,blank=True)
    videoPic = models.ImageField(null=True,blank=True)
    description = models.TextField(max_length=800,null=True,blank=True)
    likes = models.ManyToManyField(User,related_name='video_likes',null=True,blank=True)
    dislikes = models.ManyToManyField(User,related_name='video_dislikes',null=True,blank=True)
    category = MultiSelectField(choices=videoCat,max_choices=4,default=1)
    watchLater = models.ManyToManyField(User,related_name='watch_later',null=True,blank=True)
    history = models.ManyToManyField(User,related_name='user_history',null=True,blank=True)
    trending = models.BooleanField(null=True,blank=True,default=False)
    trendingTop5 = models.BooleanField(null=True,blank=True,default=False)

    def total_like(self):
        return self.likes.count()
    def total_dislike(self):
        return self.dislikes.count()    
    def __str__(self):
        return self.user.username + ' --- ' + self.videoName
    

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    about = models.TextField(max_length=300,null=True,blank=True,default="")
    subscribers = models.IntegerField(default=0,null=True,blank=True)
    profilePic = models.ImageField(null=True,blank=True,upload_to='ProfilePic',default='') 
    

    def __str__(self):
        return self.user.username

class UserPlayList(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    playlistPic = models.ImageField(null=True,blank=True,upload_to='PlaylistPic',default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,default=1)
    videos = models.ManyToManyField(UserVideo,related_name='user_playlist')
    description = models.TextField(max_length=800,null=True,blank=True)

    def total_videos(self):
        return self.videos.count()

    def __str__(self):
        return self.name

class Comments(models.Model):
    video = models.ForeignKey(UserVideo,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.ForeignKey('Comments',null=True,related_name='replies',on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.video.videoName , str(self.user.username))
            
    
