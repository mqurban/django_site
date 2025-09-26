from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


from django.shortcuts import render, redirect
from .forms import PostForm

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # saves to database
            return redirect('post_list')  # go back to post list after saving
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

