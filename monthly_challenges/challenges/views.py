import django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 min every day!",
    "march": "Learn Django for at least 20 min!",
    "april": "April Challenge",
    "may": "May Challenge",
    "june": "June Challenge",
    "july": "time for Some Django",
    "august": "It's August go for a Holiday",
    "september": "September Challenge",
    "october": "October Challenge",
    "november": "It's November ... Time to go out",
    "december": "December is here!"

}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("Monthly_Challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if (month > len(months)):
        return HttpResponseNotFound("Invalid Month!")
    forward_month = months[month - 1]
    forward_path = reverse("Monthly_Challenge", args=[forward_month])
    return HttpResponseRedirect(forward_path)



def monthly_challenge(request, month): 
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not Supported!</h1>")
