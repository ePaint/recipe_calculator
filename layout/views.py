from django.shortcuts import render


def not_found(request, exception):
    print("404 error")
    return render(request, "layout/404.html")


def server_error(request):
    print("500 error")
    return render(request, "layout/500.html")


def not_ready(request):
    print("Not ready")
    return render(request, "layout/not_ready.html")


def base(request):
    return render(request, "layout/base.html")


def home(request):
    return render(request, "layout/home.html")
