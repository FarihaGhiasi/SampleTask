from sqlalchemy import create_engine


connection_string = 'postgresql://postgres:postgres@db:5432/user_db'

try:
    # Create a database engine and establish a connection
    engine = create_engine(connection_string)
    connection = engine.connect()

    # If the connection is successful, print a success message
    print("Connected to the PostgreSQL database.")

except Exception as e:
    print(f"Failed to connect to the database: {e}")





