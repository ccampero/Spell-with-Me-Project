from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Speller, Word
from .forms import StudyForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'
    
def about(request):
    return render(request, 'about.html')

@login_required
def speller_index(request):
    spellers = Speller.objects.filter(user=request.user)
    return render(request, 'spellers/index.html', {'spellers': spellers})

@login_required
def speller_detail(request, speller_id):
    speller = Speller.objects.get(id=speller_id)
    words_speller_doesnt_have = Word.objects.exclude(id__in = speller.words.all().values_list('id'))
    study_form = StudyForm()  
    study_word_options = range(1, 101)  
    return render(request, 'spellers/detail.html', {
        'speller': speller,
        'study_form': study_form,
        'study_word_options': study_word_options,
        'words': words_speller_doesnt_have
    })

@login_required
def add_study(request, speller_id):
    
    form = StudyForm(request.POST)
   
    if form.is_valid():
        print('valid')
        new_study = form.save(commit=False)
        new_study.speller_id = speller_id
        new_study.save()
    return redirect('speller-detail', speller_id=speller_id)

@login_required   
def associate_word(request, speller_id, word_id):
    Speller.objects.get(id=speller_id).words.add(word_id)
    return redirect('speller-detail', speller_id=speller_id)

@login_required
def remove_word(request, speller_id, word_id):
   speller = Speller.objects.get(id=speller_id)
   word = Word.objects.get(id=word_id)
   speller.words.remove(word)
   
   return redirect('speller-detail', speller_id=speller.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )

class SpellerCreate(LoginRequiredMixin, CreateView):
    model = Speller
    fields = ['name','description', 'age']
    success_url = '/spellers/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class SpellerUpdate(LoginRequiredMixin, UpdateView):
    model = Speller
    fields = ['description', 'age', 'grade']
    
class SpellerDelete(LoginRequiredMixin, DeleteView):
    model = Speller
    success_url = '/spellers/'    
   
   
class WordCreate(LoginRequiredMixin, CreateView):
    model = Word
    fields = '__all__' 

class WordList(LoginRequiredMixin, ListView):
    model = Word
    
class WordDetail(LoginRequiredMixin, DetailView):
    model = Word

class WordUpdate(LoginRequiredMixin, UpdateView):
    model = Word
    fields = ['name', 'color', 'grade']

class WordDelete(LoginRequiredMixin, DeleteView):
    model = Word
    success_url = '/words/'
