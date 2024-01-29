#!/bin/sh

# Function to check if the PostgreSQL database is available
wait_for_db() {
    until python -c "import psycopg2; \
                    conn = psycopg2.connect(host='db', \
                                            dbname='vacinacao', \
                                            user='postgres', \
                                            password='ComplexPassword123', \
                                            port=5432);"
    do
        echo "Waiting for PostgreSQL to become available..."
        sleep 1
    done
}

# Call the wait_for_db function
wait_for_db

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
