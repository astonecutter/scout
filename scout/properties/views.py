import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from scout.markers.models import Marker

from scout.properties import forms
from scout.properties.models import Property


@login_required
def home_view(request):
    """
    Render the map and the property list

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    properties = Property.objects.all()
    markers = Marker.objects.all()
    marker_json = json.dumps(
        tuple(p.to_dict() for p in properties) + tuple(m.to_dict() for m in markers))

    return render(request, 'home.html', {
        'properties': properties,
        'markers': markers,
        'markers_json': marker_json
    })


@login_required
def property_list_view(request):
    """
    Render the property list

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    properties = Property.objects.all()

    return render(request, 'properties/list.html', {
        'properties': properties
    })


@login_required
def property_add_view(request):
    """
    Render the property add form

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    if request.method == 'POST':
        form = forms.PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.PropertyForm()

    return render(request, 'form.html', {
        'form': form
    })


@login_required
def property_edit_view(request, pk):
    """
    Render the property edit form

    :type request: django.http.HttpRequest
    :rtype: django.http.HttpResponse
    """

    property = get_object_or_404(Property.objects.all(), pk=pk)

    if request.method == 'POST':
        form = forms.PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.PropertyForm(instance=property)

    return render(request, 'form.html', {
        'form': form
    })


