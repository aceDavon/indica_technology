# Company API

The Company API is a Django REST Framework project that provides endpoints for managing company data. It allows clients to retrieve a list of companies with their respective information.

## Features

- Retrieve a list of companies

## Getting Started

To get started with the Company API, follow these steps:

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Unzip the project file `takeHomeTest.zip`

2. cd takeHomeTest
3. ```python
     python -m venv .virt

     source .virt/bin/activate

     pip install -r requirements.txt

     cd indica_technology

     ./manage.py makemigrations

     ./manage.py migrate

     ./manage.py createsuperuser

     .manage.py runserver

   ```

### API Endpoints

1. List Companies: `/api`

- Example:

  ```json
  {
    "data": [
      {
        "name": "Indica Technology",
        "icon_url": "https://source.unsplash.com/random",
        "page_links": {
          "services": "https://example.com/services"
        }
      }
    ],
    "status": 200
  }
  ```

### Sources

This project is available on Github at:
> [aceDavon](https://github.com/acedavon/indica_technology)
