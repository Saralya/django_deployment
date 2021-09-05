from django.shortcuts import render
from django.http import HttpResponse
from first_app import models
from first_app import forms
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#def home(request):
   #return HttpResponse("<h1>This is Homepage</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")

#def contact(request):
    #return HttpResponse("<h1>This is Contact Page</h1> <a href='/first_app/'>Homepage</a> <a href='/first_app/about/'>About</a>")  
    #href er vitor /first_app/ dile seta home page e redirect kore
    #href er vitor /first_app/about/ dewa hoise karon prothom /first_app/ ta home page e redirect korbe, erpor about/ diye about page e redirect korbe

#def about(request):
    #return HttpResponse("<h1>About Us</h1> <a href='/first_app/'>Homepage</a> <a href='/first_app/contact/'>Contact</a>")


#uporer method ta efficient na..template baniye html file call korbo 
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    dictionary = {
        'text_1': 'I am a text sent from views.py',
        'musician': musician_list,
        }
    return render(request, 'first_app/index.html', context=dictionary)


def form(request):
    """
    new_form = forms.user_form() #ei new_form er vitor akta empty form store hoise
    dictionary = {
        'test_form': new_form,
        'heading_1': "This form is created using django library",
    }

    if request.method == "POST":
        new_form = forms.user_form(request.POST)  
        #user jokhon form e input dibe, tokhn input data soho form ta new_form e store hobe
        dictionary.update({'test_form': new_form})
        #input dewar por jodi kono error thake tahole seta soho form update korate hobe..nahole warning message ta front end e show hobe na

        if new_form.is_valid():
            #user_name = new_form.cleaned_data["user_name"] #cleaned_data[] form theke data fetch kore 
            #user_dob = new_form.cleaned_data["user_dob"]
            user_email = new_form.cleaned_data["user_email"]
            
            #dictionary.update({"user_name":user_name})
            #dictionary.update({"user_dob":user_dob})
            dictionary.update({"user_email":user_email})
            #dictionary.update({"boolean_field":new_form.cleaned_data["boolean_field"]})
            #dictionary.update({"char_field":new_form.cleaned_data["char_field"]})
            #dictionary.update({"choice_field":new_form.cleaned_data["choice_field"]})
            #dictionary.update({"choice_field1":new_form.cleaned_data["choice_field1"]})
            #dictionary.update({"choice_field2":new_form.cleaned_data["choice_field2"]})
            #dictionary.update({"choice_field3":new_form.cleaned_data["choice_field3"]})
            #dictionary.update({"choice_field3":new_form.cleaned_data["choice_field3"]})
            #dictionary.update({"name":new_form.cleaned_data["name"]})
            #dictionary.update({"number_field":new_form.cleaned_data["number_field"]})
            dictionary.update({"field": "Fields match"})
            dictionary.update({"form_submitted":"Yes"})
    
    """
    new_form = forms.MusicianForm() # akta empty form newa holo

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST) # form e input dewar por oi data soho form ta new_form e save hobe

        if new_form.is_valid():
            new_form.save(commit=True)  #ei line diye form er input gula model e save hobe
            return index(request)

    dictionary = {
        'test_form': new_form,
        'heading_1': 'Add new musician'

    }


    return render(request, 'first_app/form.html', context=dictionary)


# Class based view (Template view)
class HomeView(TemplateView):
    template_name = 'first_app/home.html' # template_name is a built in variable for template viewing

    def get_context_data(self, **kwargs): 
    # kwargs diye basically dictionary (key:value pair) bujhay
    # args diye sudhu value bujhay
    # ** diye bujhay j kono songkhok arguement nite parbe
        context = super().get_context_data(**kwargs)
        # super() function ta get_context_data theke sob data niye context variable e store korbe
        context["sample_text_1"] = "This is sample text 1" 
        return context



# CRUD operations using class based views:

class ContentView(ListView):  # kono model er data gula dekhanor jonno ListView use hoy
    context_object_name = 'musician_list'  # context_object_name is a built in dictionary (same as context)
    model = models.Musician
    template_name = 'first_app/content.html'


class MusicianDetail(DetailView):  # DetailView by default id receive korte pare and.. 
    # oi id dhore model er respective object gular details show kore
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'


class AddMusician(CreateView):  # CreateView class ta Kono model er jonno object create korar form baniye dey
    model = models.Musician
    fields = ('first_name', 'last_name', 'instrument') # model er kon kon field er jonno input nibo seta select kore dewa jay
    template_name = 'first_app/musician_form.html'


class UpdateMusician(UpdateView): # UpdateView class ta musician_form er input soho edit korar form banabe
    model = models.Musician
    fields = ('last_name', 'instrument') # model er kon kon field edit kora jabe seta select kore dewa jay
    template_name = 'first_app/musician_form.html'



    
class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy("first_app:content")
    template_name = 'first_app/delete_musician.html'
