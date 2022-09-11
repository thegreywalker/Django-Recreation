from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def month_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if (month > len(months)):
        return HttpResponseNotFound("Invalid Month!")
    forward_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{forward_month}")



def monthly_challenge(request, month): 
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not Supported!")
