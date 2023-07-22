from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        # context['latest_stories'] = NewsStory.objects.all()[:4]
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
        form.instance.author = self.request.user
        return super().form_valid(form)

class SearchArticlesView(generic.TemplateView):
    template_name = 'news/search_articles.html'

class SearchResultsView(generic.ListView):
    model = NewsStory
    template_name = 'news/search_results.html'
    context_object_name = 'search'
    # success_url = reverse_lazy('news:search_articles')

    def get_queryset(self):
        username = self.request.GET.get('username')
        if username:
            queryset = NewsStory.objects.filter(author__username__icontains=username)
        else:
            queryset = NewsStory.objects.none()
        return queryset