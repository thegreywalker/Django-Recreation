from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "December is here!",
    "movember": None

}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    }) 


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
        return render(request, "challenges/challenge.html", {
            'challenge_text': challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        # or 

        raise Http404()
