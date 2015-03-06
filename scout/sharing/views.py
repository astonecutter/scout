from djangae.contrib.gauth.models import GaeDatastoreUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from scout.sharing import forms


@login_required
def user_list_view(request):
    """
    Render the user list

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    return render(request, 'users/list.html', {
        'users': GaeDatastoreUser.objects.all()
    })


@login_required
def user_add_view(request):
    """
    Render the user add form

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sharing:list')
    else:
        form = forms.UserForm()

    return render(request, 'form.html', {
        'form': form
    })


@login_required
def user_edit_view(request, pk):
    """
    Render the user edit form

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    user = get_object_or_404(GaeDatastoreUser.objects.all(), pk=pk)

    if request.method == 'POST':
        form = forms.UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('sharing:list')
    else:
        form = forms.UserForm(instance=user)

    return render(request, 'form.html', {
        'form': form
    })