import os
from astrapy import DataAPIClient, Database
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

def connect_to_database() -> Database:
    """
    Connects to a DataStax Astra database.
    This function retrieves the database endpoint and application token from the
    environment variables `API_TOKEN` and `DB_URL`.

    Returns:
        Database: An instance of the connected database.

    Raises:
        RuntimeError: If the environment variables `API_TOKEN` or
        `DB_URL` are not defined.
    """
    endpoint = os.environ.get("DB_URL")
    token = os.environ.get("API_TOKEN")
    
    if not token or not endpoint:
        raise RuntimeError(
            "Environment variables API_TOKEN and DB_URL must be defined"
        )

    # Create an instance of the `DataAPIClient` class with your token.
    client = DataAPIClient(token)

    # Get the database specified by your endpoint.
    database = client.get_database(endpoint)

    print(f"Connected to database {database.info().name}")

    return database