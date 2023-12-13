# from django.shortcuts import render
#Author's View
# from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

from django.contrib.auth.mixins import LoginRequiredMixin


class AccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'users/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = CustomUser.objects.get(pk=self.request.user.pk)
        return context
    
# Filter
from django.shortcuts import render
from django.contrib.auth import get_user_model
from news.models import NewsStory

def user_profile(request, username):
    user = get_user_model().objects.get(username=username)
    user_stories = NewsStory.objects.filter(author=user)

    return render(request, 'user/profile.html', {'user': user, 'user_stories': user_stories})



    #Author's view
# class AccountView(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'news/account.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_profile'] = self.request.user.profile  # Assuming you have a profile model
#         return context
