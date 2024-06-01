# YesBroker

YesBroker is a Django-based web application designed to streamline property browsing, favoriting, and meeting scheduling processes. With intuitive user interfaces and powerful backend functionalities, YesBroker offers a seamless experience for both property seekers and real estate professionals.

![YesBroker Demo](<yesbroker demo.gif>)
## Tech Stack

- Django


## Installation and Setup

To get started with YesBroker on your local machine, follow these simple steps:

1. **Clone the Repository**: Clone the YesBroker repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/YesBroker.git
   ```

2. **Navigate to Project Directory**: Change directory to the YesBroker project folder:

   ```
   cd YesBroker
   ```

3. **Install Dependencies**: Use pip to install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

4. **Run Migrations**: Apply migrations to create the necessary database schema:

   ```
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**: Create a superuser to access the Django admin panel:

   ```
   python manage.py createsuperuser
   ```

6. **Run the Development Server**: Start the Django development server:

   ```
   python manage.py runserver
   ```

7. **Access the Application**: Open your web browser and navigate to `http://localhost:8000` to access YesBroker.

## Routes

### Property Routes

- Property Detail: `/<int:pk>/`
- Property List: `/<str:slug>/`
- PDF Rendering: `/pdf/pdf/`
- Contact Page: `/contact/contact/`

### Project Routes

- Project Filters: `/`
- Address Search: `/search/`
- Premium Services: `/premium-services/`
- Developers: `/developers/`

### User Routes

- User Registration: `/register/`
- User Profile: `/profile/`
- User Login: `/login/`
- User Logout: `/logout/`
- Password Reset: `/password-reset/`, `/password-reset/done/`, `/password-reset-confirm/<uidb64>/<token>/`, `/password-reset-complete/`
- Favorite Add: `/fav/<int:id>/`, `/fav/property/<int:id>/`
- Favorite List: `/favourites/`

With YesBroker, streamline your property search, favorites management, and meeting scheduling effortlessly!