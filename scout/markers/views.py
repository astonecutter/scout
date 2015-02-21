from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from scout.properties import forms


@login_required
def marker_add_view(request):
    """
    Render the marker add form

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    if request.method == 'POST':
        form = forms.MarkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.MarkerForm()

    return render(request, 'form.html', {
        'form': form
    })