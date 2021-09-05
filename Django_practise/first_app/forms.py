from django import forms
from django.core import validators
from first_app import models

#custom validator function
def even_or_not(value):
    if value%2 == 1:
        raise forms.ValidationError("Please insert an even number")

"""
class user_form(forms.Form):
    #user_name = forms.CharField(label="Full Name", initial="Saralya") #html code e value field er kaj ta ekhane kore initial
    #user_email = forms.EmailField(label="User Email", widget = forms.TextInput(attrs= {"placeholder":"Enter your email", "style":"width:300px"})) 
    #html er j functionality fula python e directly apply kora jay na segula widget er maddhome kora hoy
    #attrs holo akta dictionary jekhane key and value er maddhome placeholder er kaj kora hoise (different type er kaj kora jay)
    #user_dob = forms.DateField(label="Date of birth", widget= forms.TextInput(attrs={"type":"date"}))
    #boolean_field = forms.BooleanField(required=False)
    #char_field = forms.CharField(max_length=15, min_length=5)
    
    #choices = (('','---Select option---'),('1','First'),('2','Second'),('3','Third'))
    #choice_field = forms.ChoiceField(choices=choices)
    #choices tuple tar 1st parameter ta database e save hoy, 2nd ta front end e show hoy

    #choices1 = (('A','A'),('B','B'),('C','C'))
    #choice_field1 = forms.ChoiceField(choices=choices1, widget=forms.RadioSelect)

    #choices2 = (('','---Select option---'),('1','First'),('2','Second'),('3','Third'))
    #choice_field2 = forms.MultipleChoiceField(choices=choices2)

    #choices3 = (('A','A'),('B','B'),('C','C'))
    #choice_field3 = forms.MultipleChoiceField(choices=choices3, widget=forms.CheckboxSelectMultiple)

    #validators example
    #name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    #number_field = forms.IntegerField(validators=[validators.MaxValueValidator(15), validators.MinValueValidator(5)])
    #number_field = forms.IntegerField(validators=[even_or_not])

    user_email = forms.EmailField()
    user_vmail = forms.EmailField()

    def clean(self):
        all_cleaned_data = super().clean()
        #super() function ta parent class (user_form) er sob data fetch kore ei variable e save korbe
        user_email = all_cleaned_data['user_email']
        user_vmail = all_cleaned_data['user_vmail']

        if user_email != user_vmail:
            raise forms.ValidationError("Fields Don't match")
"""

#model onujayi form create
class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"  #model tar sob gula field er jonno form create hobe
        #fields = ('first_name', 'last_name',)  #jodi form e particular kichu field rakhte chai
        #exclude = ['last_name']  #jodi form e kichu field baad diye baki gula rakhte chai

        
