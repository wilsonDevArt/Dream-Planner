
from django import forms
from .models import List_of_Dream, Steps_to_Concretize
from django.contrib.auth.models import User



class AddDreamForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(),disabled=True, widget=forms.HiddenInput())
    dream = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Dream", "class":"form-control"}), label="")
    schedule = forms.CharField(initial="0", widget=forms.HiddenInput())
    done = forms.BooleanField(required=False, widget=forms.HiddenInput(), label="")
    
    class Meta:    
        model = List_of_Dream            
        fields = "__all__"      
        
        
class AddStepForm(forms.ModelForm):
    dream = forms.ModelChoiceField(queryset=List_of_Dream.objects.all(),disabled=True)
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Step", "class":"form-control"}), label="What is the step to achive it?")    
    time_line = forms.CharField(initial="0", widget=forms.widgets.TextInput(attrs={"placeholder":"Step", "class":"form-control"}), label="How much time it will take?")    
    step_done = forms.BooleanField(required=False, widget=forms.HiddenInput(), label="")
    
    class Meta:    
        model = Steps_to_Concretize
        exclude = ("user",)  
