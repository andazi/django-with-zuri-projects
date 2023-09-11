from django.http import JsonResponse
#from .models import MyEndPoint
from django.utils import timezone


# Create your views here.

def get_data(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get("track")
    
    current_day = timezone.now().strftime("%A")

    current_utc_time = timezone.now(timezone.utc).isoformat()
    github_fil_url = ""
    github_repo_url =  "https://github.com/andazi/django-with-zuri-projects"
    status_code =  200
    
    context = {
        "slack_name" : slack_name,
        "current_day" : current_day,
        "utc_time" : current_utc_time,
        "track" : track,
        "github_file_url" : github_fil_url,
        "github_repo_url" : github_repo_url,
        "status_code" : status_code,
    }
    
    return JsonResponse(context)

print(timezone.now())
