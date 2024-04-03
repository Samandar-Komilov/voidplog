from django.shortcuts import render
from django.views import View


class HomeView(View):
    template = "index.html"
    def get(self, request):
        return render(request, template_name=self.template)
    

class AboutView(View):
    template = "about.html"
    def get(self, request):
        return render(request, template_name=self.template)
    

# Temporary
class PostView(View):
    template = "post.html"
    def get(self, request):
        return render(request, template_name=self.template)
    

class ContactView(View):
    template = "contact.html"
    def get(self, request):
        return render(request, template_name=self.template)