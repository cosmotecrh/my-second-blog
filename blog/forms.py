from django import forms
from .models import MBO22,ADC22,PDI22#PDI22G
from django.core.exceptions import ValidationError
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class uploadForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password","first_name","last_name"]

class readForm(forms.Form):
    name = forms.CharField(max_length=50)
    boss = forms.CharField(max_length=50)
    FN = forms.CharField(max_length=50)
    LN = forms.CharField(max_length=50)
    PW = forms.CharField(max_length=50)


# 例外処理
from django.core.exceptions import ObjectDoesNotExist

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

Achoice=[('0','aprovar'),('1','pede ele/ela para corrigir'),]


class DeptForm(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('DEPT',)
        lables = {'DEPT':"escolhe seu departamento"}

class MBO22Q1Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A1','MBO22AP','MBO22B1','MBO22BP','MBO22C1','MBO22CP','MBO22D1','MBO22DP','MBO22E1','MBO22EP','MBO22F1','MBO22FP','MBO22G1','MBO22GP')
        labels = {'MBO22A1':"meta1",'MBO22B1':"meta2",'MBO22C1':"meta3",'MBO22D1':"meta4",'MBO22E1':"meta5",'MBO22F1':"meta6",'MBO22G1':"meta7",'MBO22AP':"peso% de meta1",'MBO22BP':"peso% de meta2",'MBO22CP':"peso% de meta3",'MBO22DP':"peso% de meta4",'MBO22EP':"peso% de meta5",'MBO22FP':"peso de meta6",'MBO22GP':"peso% de meta7"}
        widgets = {
            'MBO22A1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22AP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22BP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22CP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22DP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22EP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22FP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22GP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }

class MBO22Q2Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A2','MBO22B2','MBO22C2','MBO22D2','MBO22E2','MBO22F2','MBO22G2')
        labels = {'MBO22A2':"meta1",'MBO22B2':"meta2",'MBO22C2':"meta3",'MBO22D2':"meta4",'MBO22E2':"meta5",'MBO22F2':"meta6",'MBO22G2':"meta7"}
        widgets = {
            'MBO22A2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO22Q3Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A3','MBO22B3','MBO22C3','MBO22D3','MBO22E3','MBO22F3','MBO22G3')
        labels = {'MBO22A3':"meta1",'MBO22B3':"meta2",'MBO22C3':"meta3",'MBO22D3':"meta4",'MBO22E3':"meta5",'MBO22F3':"meta6",'MBO22G3':"meta7"}
        widgets = {
            'MBO22A3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO22Q4Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO22A4','MBO22AR','MBO22B4','MBO22BR','MBO22C4','MBO22CR','MBO22D4','MBO22DR','MBO22E4','MBO22ER','MBO22F4','MBO22FR','MBO22G4','MBO22GR')
        labels = {'MBO22A4':"meta1",'MBO22B4':"meta2",'MBO22C4':"meta3",'MBO22D4':"meta4",'MBO22E4':"meta5",'MBO22F4':"meta6",'MBO22G4':"meta7",'MBO22AR':"pontuação",'MBO22BR':"pontuação",'MBO22CR':"pontuação",'MBO22DR':"pontuação",'MBO22ER':"pontuação",'MBO22FR':"pontuação",'MBO22GR':"pontuação"}
        widgets = {
            'MBO22A4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22B4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22C4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22D4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22E4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22F4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22G4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO22AR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22BR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22CR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22DR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22ER':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22FR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO22GR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }



class ADC22CForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC22G1C','ADC22G1OC','ADC22G2C','ADC22G2OC','ADC22G3C','ADC22G3OC','ADC22G4C','ADC22G4OC','ADC22G5C','ADC22G5OC','ADC22G6C','ADC22G6OC','ADC22G7C','ADC22G7OC','ADC22E1C','ADC22E1OC','ADC22E2C','ADC22E2OC')
        labels = {'ADC22G1C':"auto avaliação",'ADC22G1OC':"observação por colaborador",'ADC22G2C':"auto avaliação",'ADC22G2OC':"observação por colaborador",'ADC22G3C':"auto avaliação",'ADC22G3OC':"observação por colaborador",'ADC22G4C':"auto avaliação",'ADC22G4OC':"observação por colaborador",'ADC22G5C':"auto avaliação",'ADC22G5OC':"observação por colaborador",'ADC22G6C':"auto avaliação",'ADC22G6OC':"observação por colaborador",'ADC22G7C':"auto avaliação",'ADC22G7OC':"observação por colaborador",'ADC22E1C':"auto avaliação",'ADC22E1OC':"observação por colaborador",'ADC22E2C':"auto avaliação",'ADC22E2OC':"observação por colaborador"}
        widgets = {
            'ADC22E1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22E2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G3OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G3C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G4OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G4C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G5OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G5C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G6OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G6C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G7OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G7C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }
        

class ADC22AOForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC22G1A','ADC22G1O','ADC22G2A','ADC22G2O','ADC22G3A','ADC22G3O','ADC22G4A','ADC22G4O','ADC22G5A','ADC22G5O','ADC22G6A','ADC22G6O','ADC22G7A','ADC22G7O','ADC22E1A','ADC22E1O','ADC22E2A','ADC22E2O')
        labels = {'ADC22G1A':"avaliação por avaliador/a",'ADC22G1O':"observação por avaliador/a",'ADC22G2A':"avaliação por avaliador/a",'ADC22G2O':"observação por avaliador/a",'ADC22G3A':"avaliação por avaliador/a",'ADC22G3O':"observação por avaliador/a",'ADC22G4A':"avaliação por avaliador/a",'ADC22G4O':"observação por avaliador/a",'ADC22G5A':"avaliação por avaliador/a",'ADC22G5O':"observação por avaliador/a",'ADC22G6A':"avaliação por avaliador/a",'ADC22G6O':"observação por avaliador/a",'ADC22G7A':"avaliação por avaliador/a",'ADC22G7O':"observação por avaliador/a",'ADC22E1A':"avaliação por avaliador/a",'ADC22E1O':"observação por avaliador/a",'ADC22E2A':"avaliação por avaliador/a",'ADC22E2O':"observação por avaliador/a"}
        widgets = {
            'ADC22E1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22E2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22E2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G3O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G3A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G4O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G4A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G5O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G5A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G6O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G6A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC22G7O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC22G7A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }


class PDI22Form(forms.ModelForm):

    class Meta ():

        model = PDI22
        fields = ('PDI22G1C','PDI22G2C','PDI22G3C','PDI22G1PD','PDI22G2PD','PDI22G3PD','PDI22E1PD','PDI22E2PD','PDI22G1','PDI22G2','PDI22G3','PDI22E1','PDI22E2')
        labels = {'PDI22G1C':"foco1",'PDI22G2C':"foco2",'PDI22G3C':"foco3",'PDI22G1PD':"ponto-a-desenvolver-1",'PDI22G2PD':"ponto-a-desenvolver-2",'PDI22G3PD':"ponto-a-desenvolver-3",'PDI22E1PD':"ponto-a-desenvolver-4",'PDI22E2PD':"ponto-a-desenvolver-5",'PDI22G1':"PDI-1",'PDI22G2':"PDI-2",'PDI22G3':"PDI-3",'PDI22E1':"PDI-4",'PDI22E2':"PDI-5"}
        widgets = {
            'PDI22G1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G3PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G3':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22E2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI22G1C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI22G2C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI22G3C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            }


#class PDI22GForm(forms.ModelForm):

#    class Meta ():

#        model = PDI22
#        fields = ('PDI22G1C','PDI22G1PD','PDI22G1','PDI22G2C','PDI22G2PD','PDI22G2','PDI22G3C','PDI22G3PD','PDI22G3','PDI22E1C','PDI22E1PD','PDI22E1','PDI22E2C','PDI22E2PD','PDI22E2')
#        fields = ('PDI22G1PD','PDI22G1','PDI22G2PD','PDI22G2','PDI22G3PD','PDI22G3')

#class PDI22EForm(forms.ModelForm):

#    class Meta ():

#        model = PDI22
#        fields = ('PDI22G1C','PDI22G1PD','PDI22G1','PDI22G2C','PDI22G2PD','PDI22G2','PDI22G3C','PDI22G3PD','PDI22G3','PDI22E1C','PDI22E1PD','PDI22E1','PDI22E2C','PDI22E2PD','PDI22E2')
#        fields = ('PDI22E1PD','PDI22E1','PDI22E2PD','PDI22E2')


#class PDI22GCForm(forms.ModelForm):
#    PDI22G1C = forms.ModelChoiceField(queryset=ADC22GRH.objects.values('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7'), blank=True)
#    PDI22G2C = forms.ModelChoiceField(queryset=ADC22GRH.objects.values('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7'), blank=True)
#    PDI22G3C = forms.ModelChoiceField(queryset=ADC22GRH.objects.values('ADC22G1','ADC22G2','ADC22G3','ADC22G4','ADC22G5','ADC22G6','ADC22G7'), blank=True)
    
#    class Meta ():

#        model = PDI22G
#        fields = ('PDI22G1C','PDI22G2C','PDI22G3C')

class MBO23Q1Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO23A1','MBO23AP','MBO23B1','MBO23BP','MBO23C1','MBO23CP','MBO23D1','MBO23DP','MBO23E1','MBO23EP','MBO23F1','MBO23FP','MBO23G1','MBO23GP')
        labels = {'MBO23A1':"meta1",'MBO23B1':"meta2",'MBO23C1':"meta3",'MBO23D1':"meta4",'MBO23E1':"meta5",'MBO23F1':"meta6",'MBO23G1':"meta7",'MBO23AP':"peso% de meta1",'MBO23BP':"peso% de meta2",'MBO23CP':"peso% de meta3",'MBO23DP':"peso% de meta4",'MBO23EP':"peso% de meta5",'MBO23FP':"peso de meta6",'MBO23GP':"peso% de meta7"}
        widgets = {
            'MBO23A1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23B1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23C1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23D1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23E1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23F1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23G1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23AP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23BP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23CP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23DP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23EP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23FP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23GP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }

class MBO23Q2Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO23A2','MBO23B2','MBO23C2','MBO23D2','MBO23E2','MBO23F2','MBO23G2')
        labels = {'MBO23A2':"meta1",'MBO23B2':"meta2",'MBO23C2':"meta3",'MBO23D2':"meta4",'MBO23E2':"meta5",'MBO23F2':"meta6",'MBO23G2':"meta7"}
        widgets = {
            'MBO23A2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23B2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23C2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23D2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23E2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23F2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23G2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO23Q3Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO23A3','MBO23B3','MBO23C3','MBO23D3','MBO23E3','MBO23F3','MBO23G3')
        labels = {'MBO23A3':"meta1",'MBO23B3':"meta2",'MBO23C3':"meta3",'MBO23D3':"meta4",'MBO23E3':"meta5",'MBO23F3':"meta6",'MBO23G3':"meta7"}
        widgets = {
            'MBO23A3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23B3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23C3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23D3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23E3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23F3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23G3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO23Q4Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO23A4','MBO23AR','MBO23B4','MBO23BR','MBO23C4','MBO23CR','MBO23D4','MBO23DR','MBO23E4','MBO23ER','MBO23F4','MBO23FR','MBO23G4','MBO23GR')
        labels = {'MBO23A4':"meta1",'MBO23B4':"meta2",'MBO23C4':"meta3",'MBO23D4':"meta4",'MBO23E4':"meta5",'MBO23F4':"meta6",'MBO23G4':"meta7",'MBO23AR':"pontuação",'MBO23BR':"pontuação",'MBO23CR':"pontuação",'MBO23DR':"pontuação",'MBO23ER':"pontuação",'MBO23FR':"pontuação",'MBO23GR':"pontuação"}
        widgets = {
            'MBO23A4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23B4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23C4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23D4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23E4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23F4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23G4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO23AR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23BR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23CR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23DR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23ER':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23FR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO23GR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }



class ADC23CForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC23G1C','ADC23G1OC','ADC23G2C','ADC23G2OC','ADC23G3C','ADC23G3OC','ADC23G4C','ADC23G4OC','ADC23G5C','ADC23G5OC','ADC23G6C','ADC23G6OC','ADC23G7C','ADC23G7OC','ADC23E1C','ADC23E1OC','ADC23E2C','ADC23E2OC')
        labels = {'ADC23G1C':"auto avaliação",'ADC23G1OC':"observação por colaborador",'ADC23G2C':"auto avaliação",'ADC23G2OC':"observação por colaborador",'ADC23G3C':"auto avaliação",'ADC23G3OC':"observação por colaborador",'ADC23G4C':"auto avaliação",'ADC23G4OC':"observação por colaborador",'ADC23G5C':"auto avaliação",'ADC23G5OC':"observação por colaborador",'ADC23G6C':"auto avaliação",'ADC23G6OC':"observação por colaborador",'ADC23G7C':"auto avaliação",'ADC23G7OC':"observação por colaborador",'ADC23E1C':"auto avaliação",'ADC23E1OC':"observação por colaborador",'ADC23E2C':"auto avaliação",'ADC23E2OC':"observação por colaborador"}
        widgets = {
            'ADC23E1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23E1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23E2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23E2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G3OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G3C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G4OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G4C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G5OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G5C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G6OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G6C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G7OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G7C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }
        

class ADC23AOForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC23G1A','ADC23G1O','ADC23G2A','ADC23G2O','ADC23G3A','ADC23G3O','ADC23G4A','ADC23G4O','ADC23G5A','ADC23G5O','ADC23G6A','ADC23G6O','ADC23G7A','ADC23G7O','ADC23E1A','ADC23E1O','ADC23E2A','ADC23E2O')
        labels = {'ADC23G1A':"avaliação por avaliador/a",'ADC23G1O':"observação por avaliador/a",'ADC23G2A':"avaliação por avaliador/a",'ADC23G2O':"observação por avaliador/a",'ADC23G3A':"avaliação por avaliador/a",'ADC23G3O':"observação por avaliador/a",'ADC23G4A':"avaliação por avaliador/a",'ADC23G4O':"observação por avaliador/a",'ADC23G5A':"avaliação por avaliador/a",'ADC23G5O':"observação por avaliador/a",'ADC23G6A':"avaliação por avaliador/a",'ADC23G6O':"observação por avaliador/a",'ADC23G7A':"avaliação por avaliador/a",'ADC23G7O':"observação por avaliador/a",'ADC23E1A':"avaliação por avaliador/a",'ADC23E1O':"observação por avaliador/a",'ADC23E2A':"avaliação por avaliador/a",'ADC23E2O':"observação por avaliador/a"}
        widgets = {
            'ADC23E1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23E1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23E2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23E2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G3O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G3A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G4O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G4A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G5O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G5A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G6O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G6A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC23G7O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC23G7A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }


class PDI23Form(forms.ModelForm):

    class Meta ():

        model = PDI22
        fields = ('PDI23G1C','PDI23G2C','PDI23G3C','PDI23G1PD','PDI23G2PD','PDI23G3PD','PDI23E1PD','PDI23E2PD','PDI23G1','PDI23G2','PDI23G3','PDI23E1','PDI23E2')
        labels = {'PDI23G1C':"foco1",'PDI23G2C':"foco2",'PDI23G3C':"foco3",'PDI23G1PD':"ponto-a-desenvolver-1",'PDI23G2PD':"ponto-a-desenvolver-2",'PDI23G3PD':"ponto-a-desenvolver-3",'PDI23E1PD':"ponto-a-desenvolver-4",'PDI23E2PD':"ponto-a-desenvolver-5",'PDI23G1':"PDI-1",'PDI23G2':"PDI-2",'PDI23G3':"PDI-3",'PDI23E1':"PDI-4",'PDI23E2':"PDI-5"}
        widgets = {
            'PDI23G1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23G2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23G3PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23E1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23E2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23G1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23G2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23G3':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23E1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23E2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI23G1C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI23G2C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI23G3C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            }

###############################################################################################################3
##################################################################################################################
###############################################################################################################3
##################################################################################################################
###############################################################################################################3
##################################################################################################################

class MBO24Q1Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO24A1','MBO24AP','MBO24B1','MBO24BP','MBO24C1','MBO24CP','MBO24D1','MBO24DP','MBO24E1','MBO24EP','MBO24F1','MBO24FP','MBO24G1','MBO24GP')
        labels = {'MBO24A1':"meta1",'MBO24B1':"meta2",'MBO24C1':"meta3",'MBO24D1':"meta4",'MBO24E1':"meta5",'MBO24F1':"meta6",'MBO24G1':"meta7",'MBO24AP':"peso% de meta1",'MBO24BP':"peso% de meta2",'MBO24CP':"peso% de meta3",'MBO24DP':"peso% de meta4",'MBO24EP':"peso% de meta5",'MBO24FP':"peso de meta6",'MBO24GP':"peso% de meta7"}
        widgets = {
            'MBO24A1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24B1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24C1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24D1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24E1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24F1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24G1':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24AP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24BP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24CP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24DP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24EP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24FP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24GP':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }

class MBO24Q2Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO24A2','MBO24B2','MBO24C2','MBO24D2','MBO24E2','MBO24F2','MBO24G2')
        labels = {'MBO24A2':"meta1",'MBO24B2':"meta2",'MBO24C2':"meta3",'MBO24D2':"meta4",'MBO24E2':"meta5",'MBO24F2':"meta6",'MBO24G2':"meta7"}
        widgets = {
            'MBO24A2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24B2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24C2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24D2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24E2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24F2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24G2':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO24Q3Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO24A3','MBO24B3','MBO24C3','MBO24D3','MBO24E3','MBO24F3','MBO24G3')
        labels = {'MBO24A3':"meta1",'MBO24B3':"meta2",'MBO24C3':"meta3",'MBO24D3':"meta4",'MBO24E3':"meta5",'MBO24F3':"meta6",'MBO24G3':"meta7"}
        widgets = {
            'MBO24A3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24B3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24C3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24D3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24E3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24F3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24G3':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            }
        
class MBO24Q4Form(forms.ModelForm):

    class Meta():
        model = MBO22
        fields = ('MBO24A4','MBO24AR','MBO24B4','MBO24BR','MBO24C4','MBO24CR','MBO24D4','MBO24DR','MBO24E4','MBO24ER','MBO24F4','MBO24FR','MBO24G4','MBO24GR')
        labels = {'MBO24A4':"meta1",'MBO24B4':"meta2",'MBO24C4':"meta3",'MBO24D4':"meta4",'MBO24E4':"meta5",'MBO24F4':"meta6",'MBO24G4':"meta7",'MBO24AR':"pontuação",'MBO24BR':"pontuação",'MBO24CR':"pontuação",'MBO24DR':"pontuação",'MBO24ER':"pontuação",'MBO24FR':"pontuação",'MBO24GR':"pontuação"}
        widgets = {
            'MBO24A4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24B4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24C4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24D4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24E4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24F4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24G4':forms.Textarea(attrs={'rows':3, 'cols':50, 'style': 'border-color:white; font-size:x-small'}),
            'MBO24AR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24BR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24CR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24DR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24ER':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24FR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            'MBO24GR':forms.NumberInput(attrs={'style': 'width:8ch; border-color:white'}),
            }



class ADC24CForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC24G1C','ADC24G1OC','ADC24G2C','ADC24G2OC','ADC24G3C','ADC24G3OC','ADC24G4C','ADC24G4OC','ADC24G5C','ADC24G5OC','ADC24G6C','ADC24G6OC','ADC24G7C','ADC24G7OC','ADC24E1C','ADC24E1OC','ADC24E2C','ADC24E2OC')
        labels = {'ADC24G1C':"auto avaliação",'ADC24G1OC':"observação por colaborador",'ADC24G2C':"auto avaliação",'ADC24G2OC':"observação por colaborador",'ADC24G3C':"auto avaliação",'ADC24G3OC':"observação por colaborador",'ADC24G4C':"auto avaliação",'ADC24G4OC':"observação por colaborador",'ADC24G5C':"auto avaliação",'ADC24G5OC':"observação por colaborador",'ADC24G6C':"auto avaliação",'ADC24G6OC':"observação por colaborador",'ADC24G7C':"auto avaliação",'ADC24G7OC':"observação por colaborador",'ADC24E1C':"auto avaliação",'ADC24E1OC':"observação por colaborador",'ADC24E2C':"auto avaliação",'ADC24E2OC':"observação por colaborador"}
        widgets = {
            'ADC24E1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24E1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24E2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24E2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G1OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G1C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G2OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G2C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G3OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G3C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G4OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G4C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G5OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G5C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G6OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G6C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G7OC':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G7C':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }
        

class ADC24AOForm(forms.ModelForm):

    class Meta ():

        model = ADC22
        fields = ('ADC24G1A','ADC24G1O','ADC24G2A','ADC24G2O','ADC24G3A','ADC24G3O','ADC24G4A','ADC24G4O','ADC24G5A','ADC24G5O','ADC24G6A','ADC24G6O','ADC24G7A','ADC24G7O','ADC24E1A','ADC24E1O','ADC24E2A','ADC24E2O')
        labels = {'ADC24G1A':"avaliação por avaliador/a",'ADC24G1O':"observação por avaliador/a",'ADC24G2A':"avaliação por avaliador/a",'ADC24G2O':"observação por avaliador/a",'ADC24G3A':"avaliação por avaliador/a",'ADC24G3O':"observação por avaliador/a",'ADC24G4A':"avaliação por avaliador/a",'ADC24G4O':"observação por avaliador/a",'ADC24G5A':"avaliação por avaliador/a",'ADC24G5O':"observação por avaliador/a",'ADC24G6A':"avaliação por avaliador/a",'ADC24G6O':"observação por avaliador/a",'ADC24G7A':"avaliação por avaliador/a",'ADC24G7O':"observação por avaliador/a",'ADC24E1A':"avaliação por avaliador/a",'ADC24E1O':"observação por avaliador/a",'ADC24E2A':"avaliação por avaliador/a",'ADC24E2O':"observação por avaliador/a"}
        widgets = {
            'ADC24E1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24E1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24E2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24E2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G1O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G1A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G2O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G2A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G3O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G3A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G4O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G4A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G5O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G5A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G6O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G6A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            'ADC24G7O':forms.Textarea(attrs={'rows':2, 'cols':75, 'style': 'border-color:white; font-size:x-small'}),
            'ADC24G7A':forms.Select(attrs={'style': 'width:15ch; height:7ch; border-color:white; background-color:white'}),
            }


class PDI24Form(forms.ModelForm):

    class Meta ():

        model = PDI22
        fields = ('PDI24G1C','PDI24G2C','PDI24G3C','PDI24G1PD','PDI24G2PD','PDI24G3PD','PDI24E1PD','PDI24E2PD','PDI24G1','PDI24G2','PDI24G3','PDI24E1','PDI24E2')
        labels = {'PDI24G1C':"foco1",'PDI24G2C':"foco2",'PDI24G3C':"foco3",'PDI24G1PD':"ponto-a-desenvolver-1",'PDI24G2PD':"ponto-a-desenvolver-2",'PDI24G3PD':"ponto-a-desenvolver-3",'PDI24E1PD':"ponto-a-desenvolver-4",'PDI24E2PD':"ponto-a-desenvolver-5",'PDI24G1':"PDI-1",'PDI24G2':"PDI-2",'PDI24G3':"PDI-3",'PDI24E1':"PDI-4",'PDI24E2':"PDI-5"}
        widgets = {
            'PDI24G1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24G2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24G3PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24E1PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24E2PD':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24G1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24G2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24G3':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24E1':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24E2':forms.Textarea(attrs={'rows':3, 'cols':71, 'style': 'border-color:white; font-size:x-small'}),
            'PDI24G1C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI24G2C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            'PDI24G3C':forms.Select(attrs={'style': 'width:39ch; height:14ch; border-color:white; background-color:white'}),
            }
