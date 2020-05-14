from django import forms
from apps.tasks.models import Task


class TaskForm(forms.ModelForm):

    data_tarefa = forms.DateField(label='Data da Tarefa',
                                  help_text='Data de execução da tarefa',
                                  widget=forms.DateInput(format='%d/%m/%Y',
                                                         attrs={'placeholder': 'DD/MM/YYYY'}))
    title = forms.CharField(label='Tarefa',
                            help_text='Descrição da tarefa',
                            widget=forms.TextInput(attrs={'placeholder': 'Adicione uma nova tarefa...'}))

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['usuario', ]
