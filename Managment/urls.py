from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
      path('create-event/', views.create_event, name='create-event'),
      path('create-venue/', views.create_venue, name='create-venue'),
      path('view-event/',views.get_evet_all,name='veiw-event'),
      path('view-venue/', views.get_venue_all, name='view-venue'),
      path('view-venue/venue/<int:venue_id>/',views.venue_details,name='venue-details'),
      path('view-event/event/<int:event_id>/', views.event_details, name='event-details'),
      path('view-description/<int:eventId>/',views.generateAicontent,name='view-discription'),
]
urlpatterns += staticfiles_urlpatterns()