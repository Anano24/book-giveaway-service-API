
# ___Book Giveaway Service API___


This README provides instructions for setting up and running the Book Giveaway Service API project. The project is built using Django 4.2.3 and provides an API for managing books, authors, genres, conditions, cover images, and user accounts. Users can create accounts, list available books, take books, and return books.



## Table of Contents

- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Project Configuration](#project-configuration)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Usage](#usage)
- [Dockerization](#Dockerization)
- [Contributing](#contributing)



## Project Structure

The project structure is organized as follows:

- **book_giveaway_service**: The main project folder.
  - **books**: Contains models and serializers for books, authors, genres, conditions, cover images, and user accounts.
  - **bookHub**: Contains views and URL patterns for taking and returning books.
  - **db.sqlite3**: The SQLite database file.




## Setting Up the Project

Follow these steps to set up the project:

1. **Clone the repository:**
    `git clone https://github.com/Anano24/your-repo.git`
2. **Navigate to the project directory:**
    `cd book_giveaway_service`
3. **Create a virtual environment (optional but recommended):**
    `python -m venv venv`
4. **Activate the virtual environment:**
    - On Windows:
    ```
    venv\Scripts\activate
    ```
    - On macOS and Linux:
    ```
    source venv/bin/activate
    ```
5. **Install Dependencies:**
    `pip install -r requirements.txt`
6. **Apply database migrations:**
    `python manage.py migrate`
7. **Create a superuser (an admin user) to manage the application:**
    `python manage.py createsuperuser`
8. **Start the development server:**
    `python manage.py runserver`

The development server will start running at [http://localhost:8000/](http://localhost:8000/).



## Project Configuration

- **settings.py**: The Django project settings are configured in this file. Key settings include the database configuration, authentication classes, CORS settings, and more. Ensure that you configure sensitive information such as the SECRET_KEY and database settings securely, especially in production.



## API Endpoints

The API endpoints for this project include:

- **/admin/**: The Django admin interface for managing data.
- **/users/**: Endpoint for creating user accounts.
- **/login/**: Endpoint for obtaining an authentication token.
- **/users/me/**: Endpoint to retrieve the current authenticated user.
- **/books/**: Endpoint for listing and creating books.
- **/authors/**: Endpoint for listing and creating authors.
- **/genre/**: Endpoint for listing and creating genres.
- **/condition/**: Endpoint for listing and creating conditions.
- **/available-books/**: Endpoint for listing available books.
- **/books/<book_id>/take/**: Endpoint for taking a book.
- **/books/<book_id>/return/**: Endpoint for returning a book.



## Testing

The project includes unit tests to ensure the correctness of the code. To run the tests, use the following command:
    `python manage.py test`




## Usage

Follow these steps to use the project:

1. **API Authentication**: To access most API endpoints, you need to obtain an authentication token by sending a POST request to **/login/** with valid user credentials.

2. **Creating User Accounts**: Users can create accounts by sending a POST request to **/users/** with their username, email, and password.

3. **Managing Books**: Users can list and create books by sending GET and POST requests to **/books/**. The API also allows filtering books by various parameters.

4. **Taking and Returning Books**: Users can take and return books by sending POST requests to **/books/<book_id>/take/** and **/books/<book_id>/return/** respectively.

5. **Managing Authors, Genres, and Conditions**: Users can list and create authors, genres, and conditions by sending GET and POST requests to **/authors/**, **/genre/**, and **/condition/** respectively.



## Dockerization

This section provides instructions for Dockerizing the Book Giveaway Service API project. Docker allows you to containerize the application, making it easier to manage and deploy in various environments.


### Setting Up Docker

Follow these steps to run the project using Docker:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anano24/your-repo.git
   cd book_giveaway_service
2. **Create a Docker image:**
    `docker build -t book-giveaway-service .`
3. **Run the Docker container:**
    `docker run -p 8000:8000 -d book-giveaway-service`
The application will be accessible at [http://localhost:8000/](http://localhost:8000/).


### Docker Compose
Alternatively, you can use Docker Compose to manage the project's containers. Here's how:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anano24/your-repo.git
   cd book_giveaway_service
2. **Build and start the containers:**
    `docker-compose up`
The development server will start running at [http://localhost:8000/](http://localhost:8000/).


### Docker Configuration

- **Environment Variables**: Some environment variables may need to be set in the Docker configuration. Refer to the `docker-compose.yml` file for details.
- **Database**: When using Docker, the project uses an SQLite database. No additional database setup is required.
- **Port**: The application is exposed on port 8000 inside the Docker container and mapped to the host port 8000.


Feel free to customize the Dockerization section to match the specifics of your project and Docker



## Contributing

Contributions to this project are welcome. If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them.
4. Create a pull request with a clear description of your changes.
