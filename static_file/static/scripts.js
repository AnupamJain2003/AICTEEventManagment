 body = document.querySelector("body");

 function showContent(contentId) {
    // Hide all content
    contents = document.querySelectorAll('.content');
    contents.forEach(content => content.style.display = 'none');

    // Show the selected content
    document.getElementById(contentId).style.display = 'block';

    // If the selected content is the event content, load events
   
}
function displayEventList(events) {
    const eventList = document.querySelector('.event-list');

   
   
    // Create new event cards and append them to the event list
    events.forEach(event => {
      eventCard = document.createElement('div');
        eventCard.className = 'event-card';
        eventCard.id = `eventCard${event.id}`;
        eventCard.setAttribute('data-event-id', event.id);

        eventCard.innerHTML = `
            <h2>Name: ${event.name}</h2>
            <p>Date: ${event.date}</p>
            <p>Host: ${event.host}</p>
        `;

        eventList.appendChild(eventCard);
    });
}
document.getElementById('eventsButton').addEventListener('click', () => {
    // Fetch the list of events
    fetch('http://127.0.0.1:8000/managment/view-event/')
        .then(response => response.json())
        .then(events => {
            // Display the list of events
            displayEventList(events);
        })
        .catch(error => console.error('Error fetching event list:', error));
});
document.getElementById('venueButton').addEventListener('click', () => {
    // Fetch the list of venue
    fetch('http://127.0.0.1:8000/managment/view-venue/')
        .then(response => response.json())
        .then(venues => {
            // Display the list of venues
            displayVenueList(venues);
        })
        .catch(error => console.error('Error fetching venue list:', error));
});

function displayVenueList(venues) {
    const venueList = document.querySelector('.venue-list');

   
   
    // Create new venue cards and append them to the event list
    venues.forEach(venue => {
      venueCard = document.createElement('div');
        venueCard.className = 'venue-card';
        venueCard.id = `venue-card${venue.id}`;
        venueCard.setAttribute('data-venue-id', venue.id);

        venueCard.innerHTML = `
            <h2>${venue.name}</h2>
            <p>Status: ${venue.status}</p>
        `;

        venueList.appendChild(venueCard);
    });
}

function loadEventDetails(eventId) {
    // Use AJAX to fetch event details
    fetch(`http://127.0.0.1:8000/managment/view-event/event/${eventId}/`)
        .then(response => response.json())
        .then(data => {
            console.log(data.name);
            // Update the HTML elements with fetched data
            document.querySelector(".eventName").textContent = `Event Name: ${data.name}`;
            document.querySelector(".eventDate").textContent = `Date: ${data.date}`;
         
            document.querySelector(".eventDescription").textContent = `Description: ${data.description}`;
            document.querySelector(".eventHost").textContent = `Host: ${data.host}`;
            document.querySelector(".eventStudents").textContent = `Number of Students: ${data.num_students}`;
        })
        .catch(error => console.error('Error fetching event details:', error.message));
}

// Modify your existing code to call loadEventDetails on event card click
document.querySelector('.event-list').addEventListener('click', (event) => {
    const eventCard = event.target.closest('.event-card');
    if (eventCard) {
        const eventId = eventCard.getAttribute('data-event-id');
        console.log('Hi')
        loadEventDetails(eventId);
    }
});
// Modify your existing code to call loadVenueDetails on venue card click
document.querySelector('.venue-list').addEventListener('click', (event) => {
    const venueCard = event.target.closest('.venue-card');
    if (venueCard) {
       
        const venueId = venueCard.getAttribute('data-venue-id');
        console.log(venueId);
        loadVenueDetails(venueId);
    }
});

function loadVenueDetails(venueId) {
    // Use AJAX to fetch venue details
    fetch(`http://127.0.0.1:8000/managment/view-venue/venue/${venueId}/`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Update the HTML elements with fetched data
            document.getElementById("venue-Name").textContent = `Venue:${data.Name}`;
            document.getElementById("venueStatus").textContent = `Status: ${data.Status}`;
            document.getElementById("venueBookingDate").textContent = `Booking Date: ${data.Booking_date}`;
            document.getElementById("venueTotalCapacity").textContent = `Total Capacity: ${data.Capacity}`;
            document.getElementById("venueEvent").textContent = `Event Name: ${data.evnetName}`;
        })
        .catch(error => console.error('Error fetching venue details:', error.message));
}

// Add this to your scripts.js file

function AiGenerator(){
    var inputElement=document.getElementById('aiId');
    var inputValue = inputElement.value;
    console.log(inputValue);
    fetch(`http://127.0.0.1:8000/managment/view-description/${inputValue}/`) .then(response => response.json())
    .then(data=>{
        console.log(data);
        renderEventDetails(data);
    }).catch(error => console.error('Error fetching venue details:', error.message));

}

function renderEventDetails(data) {
    const container = document.getElementById('aiGeneratedContent');

    // Create a div to hold the HTML content
    const contentDiv = document.createElement('div');
    contentDiv.innerHTML = data.description;

    // Append the content to the container
    container.appendChild(contentDiv);
}


// Rest of your JavaScript code...



