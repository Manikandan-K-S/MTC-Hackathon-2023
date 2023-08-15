from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import WardDetails


def landing(request):
    pass



def queries(request):
    pass




@csrf_exempt
def handle_webhooks(request):
    try:
        request_payload = json.loads(request.body)
        key = request_payload['queryResult']['parameters']['any'][0]
        event = request_payload['queryResult']['fulfillmentMessages'][0]['payload']['Event']

        if event == 'Contact':
            response_data = Contact(key.lower())
        else:
            response_data = {
                "fulfillmentText": "Enter correct input"
            }
        
        return JsonResponse(response_data)

    except json.JSONDecodeError as e:
        return JsonResponse({"error": "Invalid JSON payload"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"Missing key: {e}"}, status=400)



def Contact(ward):
    try:
        ward=ward.capitalize()
       
        ward_details = WardDetails.objects.get(area=ward)
     
       
        response_data = {
            "fulfillmentText": f"Sanitary Inspector: {ward_details.sanitary_inspector}\n"
                              f"Sanitary Supervisor: {ward_details.sanitary_supervisor}"
        }
    except WardDetails.DoesNotExist:
        response_data = {
            "fulfillmentText": "Ward details not found"
        }

    #response_data = {
    #   "fulfillmentText": "Ward details not found"}
    
    return response_data

def Complaint(query):
    pass