from django.http import HttpResponse

def index(request):         
         response_data = f"""<ul>
                                    <li><a href="admin">ADMIN</a></li>
                                    <li><a href="challenges">CHALLENGES</a></li>
                           </ul>
         """
         return HttpResponse(response_data)