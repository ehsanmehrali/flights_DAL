from sqlalchemy import create_engine, text
from query import QUERY_FLIGHT_BY_ID, QUERY_FLIGHT_BY_DATE, QUERY_DELAYED_FLIGHT_BY_AIRLINE

# Define the database URL
DATABASE_URL = "sqlite:///data/flights.sqlite3"

# Create the engine
engine = create_engine(DATABASE_URL)


def execute_query(query: str, params: dict) -> list[tuple]:
    """
    Execute an SQL query with the params provided in a dictionary,
    and returns a list of records (dictionary-like objects).
    If an exception was raised, print the error, and return an empty list.
    """
    try:
        with engine.connect() as conn:
            results =  conn.execute(text(query), params)
            rows = results.fetchall()
            return rows
    except Exception as e:
        print("Query error:", e)
        return []


def get_flight_by_id(flight_id: int) -> list[tuple]:
    """
    Searches for flight details using flight ID.
    :param flight_id: Flight ID as an integer.
    :return: If the flight was found, returns a list with a single record.
    """
    params = {'id': flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params)


def get_flights_by_date(day: int, month: int, year: int) -> list[tuple]:
    """
    Searches for flight details using flight date.
    :param day: Flight day as an int.
    :param month: Flight month as an int.
    :param year: Flight year as an int.
    :return: A list of tuples(flights) if there is any.
    """
    params = {'day': day, 'month': month, 'year': year}
    return execute_query(QUERY_FLIGHT_BY_DATE, params)


def get_delayed_flights_by_airline(airline: str) -> list[tuple]:
    params = {'airline': airline}
    return execute_query(QUERY_DELAYED_FLIGHT_BY_AIRLINE, params)