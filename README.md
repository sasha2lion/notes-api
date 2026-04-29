# Notes API (Simulation)

Backend-style API for managing notes.

## Features

- Create note
- Get all notes
- Update note
- Delete note
- Input validation
- Error handling

## API Example

POST /notes  
GET /notes  
PUT /notes/1  
DELETE /notes/1  

## Example Response

{
  "data": {
    "id": 1,
    "text": "Hello"
  }
}

## Structure

app/
  models.py
  service.py
  routes.py

tests/

## Tech

- Python
- API simulation
- Modular architecture


## Status

Learning project demonstrating backend concepts.

## Search

GET /search?q=text
