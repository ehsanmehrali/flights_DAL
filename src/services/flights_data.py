import os
from sqlalchemy import create_engine, text

# Define the database URL
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATABASE_URL = f"sqlite:///{os.path.join(ROOT_DIR, 'data', 'flights.sqlite3')}"

# Create the engine
engine = create_engine(DATABASE_URL)

def build_get_flight_queries(where= None) -> str:
    query = f"""
SELECT 
    flights.ID,  
    flights.ORIGIN_AIRPORT,
    flights.DESTINATION_AIRPORT,
    airlines.AIRLINE,
    flights.DEPARTURE_DELAY as DELAY 
FROM flights 
    JOIN airlines ON flights.AIRLINE = airlines.ID
    {where}
    """
    return query


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
    Searches for flight details using flight id filter.
    :param flight_id: Flight ID as an integer.
    :return: A list with a single record of tuple(flight details) if there is any.
    """
    params = {'id': flight_id}
    where = "WHERE flights.ID = :id"
    query_flight_by_id = build_get_flight_queries(where)
    return execute_query(query_flight_by_id, params)


def get_flights_by_date(day: int, month: int, year: int) -> list[tuple]:
    """
    Searches for flight details using flight date filter.
    :param day: Flight day as an int.
    :param month: Flight month as an int.
    :param year: Flight year as an int.
    :return: A list of tuples(flights details) if there is any.
    """
    params = {'day': day, 'month': month, 'year': year}
    where = "WHERE flights.YEAR = :year AND flights.MONTH = :month AND flights.DAY = :day"
    query_flight_by_id = build_get_flight_queries(where)
    return execute_query(query_flight_by_id, params)


def get_delayed_flights_by_airline(airline: str) -> list[tuple]:
    """
    Searches for delayed flights details using airline name filter.
    :param airline: Airline name.
    :return: A list of tuples(delayed flights details) if there is any.
    """
    params = {'airline': airline}
    where = "WHERE flights.DEPARTURE_DELAY IS NOT NULL AND flights.DEPARTURE_DELAY != '' AND flights.DEPARTURE_DELAY >= 20 AND airlines.airline = :airline"
    query_delayed_flights_by_airline = build_get_flight_queries(where)
    return execute_query(query_delayed_flights_by_airline, params)


def get_delayed_flights_by_airport(origin_airport: str) -> list[tuple]:
    """
    Searches for delayed flights details using origin airport name filter.
    :param origin_airport: IATA code of the origin airport.
    :return: A list of tuples(delayed flights details) if there is any.
    """
    params = {'airport': origin_airport}
    where = ""
    query_delayed_flights_by_origin_airport = build_get_flight_queries(where)
    return execute_query(query_delayed_flights_by_origin_airport, params)
