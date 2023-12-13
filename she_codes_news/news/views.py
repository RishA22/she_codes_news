from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.shortcuts import render, get_object_or_404, redirect
# EditStoryFeature
from .forms import EditStoryForm
# Filter
# from django.contrib.auth import get_user_model

#Author's View
# from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        if self.request.user.is_authenticated: #Login/out feature
            form.instance.author = self.request.user
            return super().form_valid(form)
        # Log in/out feature
        else:
            # Handle the case where the user is not authenticated
            # You might want to redirect to the login page or show a message
            return render(self.request, 'news/not_authenticated.html')
        
# New Feature: EditStoryForm    
# def edit_story(request, pk):
#     story = get_object_or_404(NewsStory, pk=pk)

#     form = EditStoryForm(instance=story)
#     if request.method == 'POST':
#         form = EditStoryForm(request.POST, instance=story)
#         if form.is_valid():
#             form.save()
#             return redirect('news:index')
#     else:
#         form = EditStoryForm(instance=story)
#     return render(request, 'news/edit_story_form.html', {'form': form, 'story': story})

def edit_story(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)

    # Check if the user is authenticated before allowing access to the edit form
    if not request.user.is_authenticated or request.user != story.author:
        return render(request, 'news/access_denied.html')

    if request.method == 'POST':
        form = EditStoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('news:index')
        else:
            # Redirect back to the story view with an error message
            return redirect('news:story', pk=pk)  # Adjust the URL pattern if needed
    else:
        form = EditStoryForm(instance=story)

    return render(request, 'news/edit_story_form.html', {'form': form, 'story': story})

# Filter
# def stories_by_author(request, username):
#     author = get_user_model().objects.get(username=username)
#     user_stories = NewsStory.objects.filter(author=author)

#     return render(request, 'news/stories_by_author.html', {'author': author, 'user_stories': user_stories})

    #Author's view
# class AccountView(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'news/account.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_profile'] = self.request.user.profile  # Assuming you have a profile model
#         return context
