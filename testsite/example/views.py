from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

'''for def get_name'''
from django.http import HttpResponseRedirect
from .forms import NameForm


def example(request):
    template = loader.get_template('example/example.html')
    return HttpResponse(template.render())


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            context = {
                'text': 'Hello, World!',
            }
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'your-name.html', {'form': form})
