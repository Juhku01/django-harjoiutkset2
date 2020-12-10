# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from django import models
from django import forms
from django import urls
from django.contrib.auth import get_user_model

User = get_user_model()

class PostList(SelectRelatedMixin,generic.ListView):    
    model = models.Post
    select_related = ('user','group')

class UserPosts(generic.ListView):
    model = model.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user',group)

    def get_queryset(self):
        queryset = super().get_gueryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    field =('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):

    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazY('post:all')

    def get_queryset(self):
        gueryset = super().get_gueryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Dleted')
        return super().delete(*args,**kwargs)
