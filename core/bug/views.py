from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError

from django.contrib.auth.models import User
from .models import Bug

from django.shortcuts import render

def error_page(request, error_code, error_message=None):
    context = {
        'error_code': error_code,
        'error_message': error_message,
    }
    return render(request, 'error_page.html', context)


def leaderboard(request):
    # Query the database to get the count of bugs created by each user
    users_with_bug_count = User.objects.annotate(created_bug_count=Count('bug'))
    for user in users_with_bug_count:
        print(f"User: {user.username}, Created Bug Count: {user.created_bug_count}")

    context = {
        'leaderboard_data': users_with_bug_count,
    }
    return render(request, 'leaderboard/leaderboard.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('/')  # Replace 'home' with the name of your home page URL
        else:
            # Handle invalid login credentials (e.g., display an error message)
            return render(request, 'auth/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'auth/login.html')

def reg_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email=request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists./ Invalid')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email
                )
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('/')  # Change 'home' to the URL name of your home page.
            User.set_password(password1)
            User.save()
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'auth/reg.html')


def succese(request):
    # return render(request, "home/all_bugs.html")
    queryset = Bug.objects.select_related('user')

    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(bugTitle__icontains=search_query)

    context = {'home': queryset}
    return render(request, "home/all_bugs.html", context)

@login_required  # Ensure that only logged-in users can access this view
def home(request):
    if request.method == "POST":
        data = request.POST
        bugTitle = data.get('bugTitle')
        bugDescription = data.get('bugDescription')
        tag = data.get('tag')
        subscribers = data.get('subscribers')
        assign_to = data.get('assign_to')

        try:
            # Create the bug and associate it with the currently logged-in user
            Bug.objects.create(
                bugTitle=bugTitle,
                bugDescription=bugDescription,
                tag=tag,
                subscribers=subscribers,
                assign_to=assign_to,
                user=request.user  # Associate the bug with the logged-in user
            )
        except IntegrityError as e:
            # Handle the UNIQUE constraint violation error
            error_message = 'A bug with the same title already exists. Please choose a different title.'
            return redirect(request, "error.html", {'error_message': error_message})
        return redirect('/')

    # Filter bugs based on the currently logged-in user
    queryset = Bug.objects.filter(user=request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(bugTitle__icontains=request.GET.get('search'))

    context = {'home': queryset}
    return render(request, "home/register_bug.html", context)


def delete_bug(request, slug):
    bug = Bug.objects.get(slug=slug)
    bug.delete()
    return redirect('/suc-cese/')

def update_bug(request, bugTitle):
    queryset = Bug.objects.get(slug=bugTitle)  # Use slug for lookup

    if request.method == "POST":
        data = request.POST
        bugTitle = data.get('bugTitle')
        bugDescription = data.get('bugDescription')
        tag = data.get('tag')
        subscribers = data.get('subscribers')
        assign_to = data.get('assign_to')

        queryset.bugTitle = bugTitle
        queryset.bugDescription = bugDescription
        queryset.tag = tag
        queryset.subscribers = subscribers
        queryset.assign_to = assign_to

        queryset.save()
        return redirect('/suc-cese/')

    context = {'home': queryset}
    return render(request, "home/update_bug.html", context)
