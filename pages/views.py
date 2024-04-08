from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostCreateForm, PostEditForm, CommentCreateForm


class HomeView(View):
    template = "index.html"
    posts = Post.objects.all().order_by('-created_at')[0:3]
    context = {
        'posts':posts
    }
    def get(self, request):
        return render(request, template_name=self.template, context=self.context)
    

class AboutView(View):
    template = "about.html"
    def get(self, request):
        return render(request, template_name=self.template)
    

# Temporary
class PostView(View):
    template = "post-detail.html"
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        form = CommentCreateForm()
        context = {
            'post':post,
            'comments':comments,
            'form': form
        }
        return render(request, template_name=self.template, context=context)
    

class ContactView(View):
    template = "contact.html"
    def get(self, request):
        return render(request, template_name=self.template)
    

# CRUD for Posts

class PostCreateView(LoginRequiredMixin, View):
    template = "post/post_create.html"
    form = PostCreateForm()
    def get(self, request):
        return render(request, template_name=self.template, context={'form':self.form})
    def post(self, request):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post-detail', pk=post.id)
        else:
            form = PostCreateForm()
        return render(request, 'post/post_create.html', {'form':form})


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # We are giving the values from database just to not create the post again, but change some parts
        form = PostEditForm(instance=post)
        return render(request, 'post/edit.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=pk)
        return render(request, 'post/edit.html', {'form': form})
    

class PostDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('/')
    

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=pk)