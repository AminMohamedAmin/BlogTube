from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post, Post_Like, Post_Comment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views import View
# Create your views here.


def home(request):
    post = Post.objects.all()
    pop1 = post.order_by('-likes')
    pop2 = post.order_by('puplish')
    context = {
        'post':post,
        'pop1':pop1,
        'pop2': pop2,
    }
    return render(request, 'blog.html', context)

def up_sighn(request):
    try:
        if User.objects.filter(email=request.POST['email']) and not User.objects.filter(username=request.POST['name']):
            messages.error(request, 'Email exist, try Login', extra_tags='error')
            return redirect('home')
        else:
            user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['pass'])
            user.save()
            messages.success(request, 'Successfully Signed, Login now ', extra_tags='success')
            return redirect('home')
    except:
        if User.objects.filter(email=request.POST['email']) and User.objects.filter(username=request.POST['name']).exists() == True:
            messages.error(request, 'User exist, try Login', extra_tags='error')
        else:
            messages.error(request, 'User exist, try another', extra_tags='error')
        return redirect('home')


def in_log(request):
    u = request.POST['namee']
    p = request.POST['passs']
    result = authenticate(username=u, password=p)
    if result is not None:
        login(request,result)
        messages.success(request, 'Successfully Login', extra_tags='success')
        return redirect('home')
    else:
        messages.error(request, 'User not exist or Password is wrong, Sighnup first', extra_tags='error')
        return redirect('home')


def out_log(request):
    logout(request)
    return redirect('home')


def post_detail(request, id):
    post = Post.objects.get(id=id)
    like = Post_Like.objects.filter(user=request.user.id)
    postlike = Post_Like.objects.filter(post=post.id)
    postcomment = Post_Comment.objects.filter(post=post.id)
    p = Post_Like.objects.filter(user=request.user.id, post=post.id).exists()

    context = {
        'post':post,
        'like': like,
        'postlike': postlike,
        'postcomment':postcomment,
        'p':p
    }
    return render(request, 'detail.html', context)


def add_like(request, id):
    user = request.user.id
    post = Post.objects.get(id=id).id
    new = Post_Like()
    new.user = user
    new.post = post


    if Post_Like.objects.filter(user=user, post=post).exists() == False:
        new.save()
        neww = Post.objects.get(id=id)
        neww.likes +=1
        neww.save()
        return HttpResponseRedirect('../../detail/%d/' % post)
    else:
        old = Post_Like.objects.get(post=post, user=user)
        old.delete()
        oldd = Post.objects.get(id=id)
        oldd.likes -= 1
        oldd.save()
        return HttpResponseRedirect('../../detail/%d/' % post)

def add_comment(request, id):
    user = request.user.username
    post = Post.objects.get(id=id).id
    comment = request.POST['review']
    new = Post_Comment()
    new.user = user
    new.post = post
    new.comment = comment

    new.save()
    return HttpResponseRedirect('../../detail/%d/' % post)


