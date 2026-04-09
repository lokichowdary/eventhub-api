# EventHub API

## Overview

EventHub is a REST API built using Django and Django REST Framework for managing event ticket bookings.
Users can browse events, reserve seats, and cancel reservations while preventing overbooking.

---

## Setup Instructions

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

### Events

* **GET** `/api/events/` → List all events
* **POST** `/api/events/` → Create a new event
* **GET** `/api/events/?status=upcoming` → Filter by status
* **GET** `/api/events/?venue=bangalore` → Filter by venue

---

### Reservations

* **POST** `/api/reservations/` → Create reservation
* **GET** `/api/reservations/?event_id=1` → Filter by event
* **POST** `/api/reservations/{id}/cancel/` → Cancel reservation

---

## Features

* Create and manage events
* Reserve seats with validation
* Prevent overbooking
* Cancel reservations and restore seats
* Filter events and reservations
* Request logging middleware

---

## Design Decision

Seat deduction is handled inside the serializer `create()` method.
This ensures that reservation creation and seat updates happen together, maintaining data consistency.

---

## Edge Cases Handled

* Cannot reserve seats for completed/cancelled events
* Cannot reserve more seats than available
* Cannot cancel an already cancelled reservation

---

## Screenshots

Include the following screenshots:

* Successful event creation
* Successful reservation (201 Created)
* Overbooking error (400 Bad Request)
* Successful cancellation


---

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## Project Structure

```
eventhub/
├── manage.py
├── eventhub/
├── event_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── middleware.py
```

---

## Author

Sai Lokesh M
