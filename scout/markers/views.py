from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from scout.markers import forms
from scout.markers.models import Marker


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


@login_required
def marker_edit_view(request, pk):
    """
    Render the marker edit form

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    marker = get_object_or_404(Marker.objects.all(), pk=pk)

    if request.method == 'POST':
        form = forms.MarkerForm(request.POST, instance=marker)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.MarkerForm(instance=marker)

    return render(request, 'form.html', {
        'form': form
    })