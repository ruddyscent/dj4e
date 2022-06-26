from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def sessfun(request):
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    if num_visits > 5:
        del request.session["num_visits"]
    resp = HttpResponse("view count=" + str(num_visits))
    resp.set_cookie("dj4e_cookie", "98ba58ed", max_age=1000)
    return resp
