from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip
from datetime import datetime, date


def index(request):
    if 'first_name' in request.session:
        return redirect('/success')
    return render(request, "first_app/index.html")

def success(request):
    if 'first_name' in request.session:
        trip_user = Trip.objects.filter(user=request.session['id'])
        other_trips = Trip.objects.exclude(user=request.session['id'])
        # print trip_user[0].destination
        # for trip in other_trips:
        #     print trip.user.filter(id=1)
        context = {
            'trips': trip_user,
            'other_trips': other_trips
        }
        return render(request, "first_app/success.html", context)
    return redirect('/')

def registration(request):
    if request.method == "POST":
        result = User.objects.registration(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            messages.success(request, 'Registration successful')
    return redirect("/")


def login(request):
    if request.method == "POST":
        result = User.objects.login(request)
        if result[0] == False:
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)
        else:
            request.session['first_name']= result[1].first_name
            request.session['id'] = result[1].id
            return redirect('/success')
    return redirect("/")


def logout(request):
    if 'first_name' in request.session:
        request.session.pop('first_name')
    return redirect('/')

def add(request):
    if 'first_name' in request.session:
        return render(request, 'first_app/add.html')
    return redirect('/')

def table(request):
    if 'first_name' in request.session:
        trip = Trip.objects.trip_validation(request)
        if trip[0] == False:
            for error in trip[1]:
                messages.add_message(request, messages.INFO, error)
                return redirect('/travels/add')
        else:
            return redirect('/success')
    return redirect('/')

def destination(request, tid):
    if 'first_name' in request.session:
        destination = Trip.objects.get(id=tid)
        context = {
            "destination": destination
        }
        return render(request, "first_app/destination.html", context)
    return redirect('/')

def join(request, id, tid):
    if 'first_name' in request.session:
        user = User.objects.get(id=id)
        trip = Trip.objects.get(id=tid)
        trip.user.add(user)
        # joined_user = JoinUser.objects.create(trip=trip, user=user)
        return redirect('/success')
    return redirect('/')
