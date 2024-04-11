from django.shortcuts import render, redirect

# @login_required(login_url='/auth/login')


def home(request):

    # return redirect('login')

    return render(request, "base.html", {})
