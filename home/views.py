from django.shortcuts import (
    render ,  
    redirect
)
from ProfileApp.models import (
    Profile,
    Follower
)
from .models import (
    Post , 
    Comments, 
    Like, 
    Story
)
from django.shortcuts import get_object_or_404
from .forms import (
     CommentsForm, 
     NewPostForm,
     PostEditForm
)
from django.views.generic import ListView, View
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime 
from django.utils import timezone
# Create your views here.
class IndexView(ListView, LoginRequiredMixin):
    model = Post
    template_name='home/index.html'
    def get(self, request):
        if request.user.is_authenticated : 
            form = CommentsForm    
            # posts from people you followed
            user = Profile.objects.get(user=self.request.user)
            profile_page = Profile.objects.all() 
            following = user.following.all()
            following_ids = []
            for x in following:
                following_ids.append(x.id)  
            following_ids.append(user.id)
            posts_qs = Post.objects.filter(author__id__in=following_ids).order_by('-date')

            #notification
            all_posts = Post.objects.filter(author=request.user)
            notification = []
            for post in all_posts:
                like_qs = Like.objects.filter(po=post).order_by('-date')
                comments_qs = Comments.objects.filter(po=post).order_by('-date')

                for like in like_qs:
                    if like.user == request.user :
                        pass
                    else:
                        notification.append(like)
                for comment in comments_qs:
                    if comment.user == request.user :
                        pass
                    else:
                        notification.append(comment)
            followers_qs = Follower.objects.filter(influncer=request.user).order_by('-date')
            for follower in followers_qs:
                    if follower == request.user :
                        pass
                    else:
                        notification.append(follower)
                # notification.sort(key = lambda date: datetime.strptime(date, "%m%d%Y %I:%M"))

            # stories 

            me = Profile.objects.get(user=request.user)
            my_following = me.following.all()
            my_following_stories = []
            for following in my_following:
                stories_qs = Story.objects.filter(author=following.user)
                active = False 
                now = timezone.now()
                for active_story in stories_qs : 
                    if active_story.end_date <= now:
                            active_story.active = False
                            active_story.save()
                    if active_story.active == True :
                        active = True
                    else :
                        pass
                if stories_qs.exists():
                    if active == True:
                        my_following_stories.append(following.id) 
                    else:
                        pass

            all_stories = Profile.objects.filter(user__id__in=my_following_stories)
            # my stories
            my_profile = Profile.objects.get(user=request.user)
            my_profile_stories = Story.objects.filter(author=my_profile.user)
            now = timezone.now()
            for my_sotry in my_profile_stories:
                if my_sotry.end_date <= now:
                    my_sotry.active = False
                    my_sotry.save()

            #new post form

            post_form = NewPostForm

            context = {
                'title':'InstaClone',
                'profile':profile_page,
                'profile_stories':profile_page,
                'form':form,
                'posts':posts_qs, 
                'notifications':notification,
                'my_stories':my_profile,
                'stories':all_stories,
                'post_form':post_form
                }
            return render(self.request,'home/posts.html', context)
        else :
            return redirect('login')

@login_required
def AddCommentView(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        form = CommentsForm(request.POST)
        if form.is_valid():
            post_comment = form.cleaned_data.get('post_comment')
            comments = Comments(
                user=request.user,
                comment = post_comment,
                po = post
            )
            comments.save()      
            return redirect('index')

@login_required
def LikeAndDislikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
  
    like = Like(
        user=request.user,
        po=post
        )
    liker = Like.objects.filter(po=post, user=request.user)
    if liker:
        post.post_likes_number -=1
        post.save()
        liker.delete()     
    else: 
        post.post_likes_number +=1
        post.save()
        like.save()      
    return redirect('index')
   
@login_required
def StoriesDetiels(request, pk):
    now = timezone.now()
    profile = get_object_or_404(Profile, id=pk)
    stories = []
    stories_qs = Story.objects.filter(author=profile.user)
    for story in stories_qs :
        if story.active == True:
            stories.append(story)

    for my_story in stories:
        my_story.views += 1
        my_story.collor = 'B'
        my_story.save()

    context = {
            'stories':stories,
            'first_story':stories,
            'profile_stories':profile,
        }

    if len(stories)>0:

        context.update({
            'stories':stories[1:],
            'first_story':stories[0],
            'profile_stories':profile,
        }) 

    return render(request, 'home/story_detiels.html', context)

@login_required
def exploreView(request):

    posts = Post.objects.all().order_by('-post_likes_number')

    all_posts = Post.objects.filter(author=request.user)
    notification = []
    for post in all_posts:
        like_qs = Like.objects.filter(po=post)
        comments_qs = Comments.objects.filter(po=post)
        for like in like_qs:
            if like.user == request.user :
                pass
            else:
                notification.append(like)
        for comment in comments_qs:
            if comment.user == request.user :
                pass
            else:
                notification.append(comment)
    context={
        'posts':posts,
        'notifications':notification
        
    }

    return render(request, 'home/explore.html', context)

@login_required
def SearchView(request):
    profiles = User.objects.all()
    myFilter = request.GET.get('myUsers')
    if myFilter != ' ' and myFilter is not None:
        profiles = profiles.filter(username__icontains=myFilter)

    context = {
        'myUsers':profiles,
    }

    return render (request, 'home/search.html', context)

@login_required
def AddPostView(request):
    print(f'this is request post {request.POST}')
    if request.method == 'POST':
        print(f'this is request post after {request.POST}')
        form = NewPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            image = form.cleaned_data.get('image')
            discription = form.cleaned_data.get('discription')
            post_type = form.cleaned_data.get('post_type')
            print(f'this is request post valid {request.POST}')
            if post_type == 'F':
                Post.objects.create(
                    author = request.user,
                    image = image,
                    discription = discription
                )
            else:
                Story.objects.create(
                    author = request.user,
                    image = image,
                    discription = discription
                )
            return redirect('index')

def DeletPostView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.author == request.user:
        post.delete()
        return redirect('index')
    
def EditPostView(request, pk):
    post = Post.objects.get(id=pk)
    context = {
            'post':post,
        }

    if post.author == request.user:
        form = PostEditForm (instance = post)
        if request.method == 'POST':
            form = PostEditForm(request.POST, instance=post.discription)
            if form.is_valid():
                 form.save()
                 return redirect('index')
        else : 
            form = PostEditForm

        context.update({
            'form':form
        }) 
        return render(request,'home/editpost.html', context)
    else:
        return redirect('index')
   





