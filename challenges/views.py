from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenge = {
         'January' : 'January challenege',
         'February' : 'February challenege',
         'March' : 'March challenege',
         'April' : 'April challenege',
         'May' : 'May challenege',
         'June' : 'June challenege',
         'July' : 'July challenege',
         'August' : 'August challenege',
         'September' : 'September challenege',
         'October' : 'October challenege',
         'November' : 'November challenege',
         'December' : None,
}

# ** HTML as string
# def index(request):
#          # *Hardcoding
#          # response_data = """
#          #          <ul>
#          #                   <li><a href="challenges/January">January</a></li>
#          #          </ul>         
#          # """
         
#          # *Avoiding Hardcoding
#          list_items = ""
#          months = list(monthly_challenge.keys())
         
#          for month in months:
#                   month_path = reverse('month-challenge', args = [month])
#                   list_items += f'<li><a href=\"{month_path}\">{month.capitalize()}</a></li>'
         
#          response_data = f"<ul>{list_items}</ul>"
#          return HttpResponse(response_data)

# ** HTML from Template File
def index(request):
         list_items = ""
         months = list(monthly_challenge.keys())
         
         return render(request, "challenges/index.html", {
                                                               'months': months,
                                                               }
                  )
         

def monthly_challenges(request, month):                # arg month is bcoz <month> in urls.py
         try:
                  challenge_text = monthly_challenge[month]
                  
                  #sending string to website is not realistic. Mostly html+css is sent back
                  # response_data = f"<h1>{challenge_text}</h1>" # sending html in sting
                  # * Sending back HTML file
                  return render(request, "challenges/challenge.html", {"text":challenge_text, "month":str(month).upper()})
         except:
                  return HttpResponseNotFound(f"<h1>Month - {month} Not Supported</h1>")
         

def monthly_challenges_by_number(request, month):
         months = list(monthly_challenge.keys())   # returns list of dict keys
         if month > len(months):
                  return HttpResponseNotFound("Invalid month number: " + str(month))
         redirected_month = months[month-1]
         redirect_path = reverse('month-challenge', args = [redirected_month])   # reverse used to prevent hrdcoding
         return HttpResponseRedirect(redirect_path)          # challenge/{month}
         # return HttpResponseRedirect("/challenges/" + redirected_month)          # hardcoded - /challenges/{month}

         