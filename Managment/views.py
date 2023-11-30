from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
from .models import Event,Venue
from transformers import GPT2LMHeadModel, GPT2Tokenizer
def create_event(request):
    if request.method == 'POST':
          
          name = request.POST.get('eventName')
          date = request.POST.get('eventDate')
          description = request.POST.get('description')
          num_students = request.POST.get('numStudents')
          host = request.POST.get('host')
          
          event = Event(name=name, date=date, description=description, num_students=num_students, host=host)
          event.save()
          messages.success(request, 'Event was created succesfully.')
          stored_messages = [str(message) for message in messages.get_messages(request)]
          

          return render(request,'Templates\Home\home.html',{messages:stored_messages})   

    return render(request, 'Templates\Home\home.html')

def create_venue(request):
     
     if request.method == 'POST':
          name=request.POST.get('venueName')
          bookingDate=request.POST.get('bookingDate')
          status=request.POST.get('status')
          totalcapacity=request.POST.get('totalcapacity')
          eventName=request.POST.get('eventNa')
          venue=Venue(name=name, booking_date=bookingDate,status=status,total_capacity=totalcapacity,event=eventName)
          venue.save()
          messages.success(request, 'Venue was created succesfully.')
          stored_messages = [str(message) for message in messages.get_messages(request)]
          #messages.clear(request)
          return render(request,'Templates\Home\home.html',{messages:stored_messages})   
     return render(request, 'Templates\Home\home.html')

# def get_evet_all(request):
#       if request.method == 'GET':
#            all_detail=Event.objects.all()
#            return render(request,'Templates\Home\home.html',{'all_details':all_detail})
def get_evet_all(request):
    if request.method == 'GET':
        all_detail = Event.objects.all()
        events_data = [
            {
                'id': event.id,
                'name': event.name,
                'date': event.date,
                'host': event.host,
                # Add more fields as needed
            }
            for event in all_detail
        ]
        return JsonResponse(events_data, safe=False)
def get_venue_all(request):
      if request.method == 'GET':
           all_detail=Venue.objects.all()
           venue_data = [
            {
                'id': venue.id,
                'name': venue.name,
                'status':venue.status,
                # Add more fields as needed
            }
            for venue in all_detail
        ]
           return JsonResponse(venue_data, safe=False)


# def event_details(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     print(event)
#     return render(request, 'Templates\Home\home.html', {'event_details': event})
def get_event_details(event_id):
     event = get_object_or_404(Event, id=event_id)
     event_data = {'name': event.name,
        'date': event.date,
    
        'description': event.description,
        'host': event.host,
        'num_students': event.num_students,
        # Add more fields as needed
     }
     return event_data

def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event_data = {
        'name': event.name,
        'date': event.date,
    
        'description': event.description,
        'host': event.host,
        'num_students': event.num_students,
        # Add more fields as needed
    }
    return JsonResponse(event_data)
def venue_details(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    event=get_event_details(venue.event)
    print(event)
    venue_data = {
        'Name': venue.name,
        'Status': venue.status,
    
        'Booking_Date': venue.booking_date,
        'Capacity': venue.total_capacity,
          'evnetName':event['name']
    }
    #print(venue_data)
    return JsonResponse(venue_data)
def generate_event_description(name,short_description, event_date, event_host):
    # Load pre-trained GPT-2 model and tokenizer
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    # Create input text for event description
    input_text = f"Event Name:{name}\n Description: {short_description}\nDate: {event_date}\nHost: {event_host}"

    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate AI content
    outputs = model.generate(input_ids, max_length=500, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)

    # Decode the generated output
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded_output
def generateAicontent(request,eventId):
     event=get_event_details(eventId)
     description=generate_event_description(event['name'],event['description'],event['date'],event['host'])
     description=description.replace('\n','<br>')
     description_data={'description':description}
     return JsonResponse(description_data)

     
