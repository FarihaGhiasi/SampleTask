from sqlalchemy import create_engine


connection_string = 'postgresql://postgres:fariha@localhost:5432/mydb'

try:
    # Create a database engine and establish a connection
    engine = create_engine(connection_string)
    connection = engine.connect()

    # If the connection is successful, print a success message
    print("Connected to the PostgreSQL database.")

    # Close the connection

except Exception as e:
    print(f"Failed to connect to the database: {e}")





