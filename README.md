# Django Poll and Survey Application

A comprehensive Poll and Survey application built using Django and Django REST Framework (DRF). This project enables users to create, manage, and participate in polls/surveys with real-time analytics for poll results.

## Features

- User authentication and registration using JWT
- Create and manage polls and survey questions
- Submit answers to polls
- Real-time poll result visualization (chart-based)
- Permissions to restrict multiple submissions by the same user
- Full API documentation (Postman)

## Technologies Used

- **Django** - Web framework for building the backend
- **Django REST Framework (DRF)** - For creating APIs
- **JWT** - For user authentication
- **Matplotlib** - For generating chart-based analytics for poll results
- **SQLite** - Database for development

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django 4.x or higher
- Django REST Framework
- Matplotlib for charts
- JWT (JSON Web Token) for authentication

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-repo/poll-survey-app.git
   cd poll-survey-app
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**

   - The API will be available at `http://127.0.0.1:8000/`
   - Admin dashboard at `http://127.0.0.1:8000/admin`

## API Documentation

The API documentation is available via Postman and can be accessed using this link:

[Postman API Documentation](https://documenter.getpostman.com/view/37679430/2sAXxV7WJz)

### Key Endpoints

Here are some of the key API endpoints:

- **User Registration**  
  `POST /api/users/register/`  
  Registers a new user.

- **Login**  
  `POST /api/users/login/`  
  Logs in a user and returns a JWT token.

- **Polls**  
  `GET /api/polls/`  
  Lists all polls.  
  `POST /api/polls/`  
  Creates a new poll (Admin only).

- **Poll Detail**  
  `GET /api/polls/{poll_id}/`  
  Retrieves details of a specific poll.

- **Submit Poll Answer**  
  `POST /api/polls/{poll_id}/submit/`  
  Submits answers to a poll.

- **Poll Results (Chart-based)**  
  `GET /api/polls/{poll_id}/results/`  
  Displays poll results with charts.

## Permissions

- Only authenticated users can submit answers to polls.
- A user can submit answers to a poll only once (based on custom permissions).
- Admin users can create and manage polls.

## JWT Authentication

To authenticate with JWT, use the `Authorization` header with the token:

```bash
Authorization: Bearer <your-token>
```

## Poll Result Analytics

Real-time chart-based analytics for poll results are generated using Matplotlib. Once users submit their answers, results are visualized in bar charts.

## How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
