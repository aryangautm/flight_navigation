# Naviator

## Enhancing Flight Navigation Mechanism for Optimal Route Planning and Risk Mitigation

Naviator is an advanced flight navigation system designed to calculate the best possible paths between two airports, providing real-time updates on weather, distance, and time. It also performs risk assessments using weather data to ensure a safe and efficient journey.

## Features

- **Optimal Route Planning**: Calculates the most efficient routes between airports to minimize travel time and distance.
- **Real-Time Weather Updates**: Provides up-to-date weather information affecting the flight path.
- **Distance and Time Estimates**: Offers accurate distance and estimated time of arrival based on current flight conditions.
- **Risk Assessment**: Analyzes weather data to assess and mitigate potential risks along the route.
- **User-Friendly Interface**: Easy to use interface for inputting departure and destination airports.

## Tech Stack

- **Backend**: Django
- **Frontend**: React (Vite, Tailwind CSS)
- **Database**: PostgreSQL
- **Datasets**: Flight routes and airports data

## Docker Installation

1. **Build**:
   - Build and run the compose project:
    ```bash
    docker compose up --build
    ```
   - Access the server at localhost:3000
    
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aryangautm/flight_navigation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd flight_navigation
    ```
3. Create a Virtual Environment and Install the backend dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Install the frontend dependencies:
    ```bash
    cd flightend
    npm install
    cd ..
    ```
5. Set up the PostgreSQL database:
    - Ensure PostgreSQL is installed and running.
    - Create a .env file in the base directory (Refer sample.env)
    - Add the DATABASE_URL in the .env file.

6. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Load datasets for flight routes and airports:
    ```bash
    python manage.py loaddata flight_routes.json
    python manage.py loaddata airports.json
    ```
8. Run the development server:
    - Start the Django server:
        ```bash
        python manage.py runserver
        ```
    - Start the Vite development server for React:
        ```bash
        cd frontend
        npm run dev
        ```

## Usage

1. Open your browser and navigate to `http://localhost:8000` for the backend API and `http://localhost:5173` for the frontend interface.
2. Enter the IATA codes for the departure and destination airports.
3. View the optimal route, along with weather updates, distance, time estimates, and risk assessment.

## Future Scope

- **Integration with Air Traffic Control Systems**: Enhance route planning by integrating with real-time air traffic data.
- **Machine Learning for Improved Risk Assessment**: Utilize machine learning algorithms to predict and mitigate potential risks more accurately.
- **Mobile Application**: Develop a mobile app to provide navigation updates and alerts on-the-go.
- **Multi-Language Support**: Add support for multiple languages to cater to a global audience.
- **User Preferences and Profiles**: Allow users to save preferences and frequently traveled routes for quicker access.

## Contributing

We welcome contributions to improve Naviator! Here are some ways you can help:

- Report bugs and issues
- Suggest new features or enhancements
- Submit pull requests with improvements or fixes

---

Enhance your flight navigation experience with Naviator - ensuring optimal routes and safety in the skies!
