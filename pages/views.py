from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from .models import Post
from .forms import PostCreateForm


class HomeView(View):
    template = "index.html"
    posts = Post.objects.all().order_by('-created_at')[:3]
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
        context = {
            'post':post
        }
        return render(request, template_name=self.template, context=context)
    

class ContactView(View):
    template = "contact.html"
    def get(self, request):
        return render(request, template_name=self.template)
    

# CRUD for Posts

class PostCreateView(View):
    template = "post/post_create.html"
    form = PostCreateForm()
    def get(self, request):
        return render(request, template_name=self.template, context={'form':self.form})
    def post(self, request):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("Your credentials are wrong!")