from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ID = :id"
# QUERY_FLIGHT_BY_DATE = "SELECT flights.ID as FLIGHT_ID, flights.ORIGIN_AIRPORT, flights.DESTINATION_AIRPORT, flights.AIRLINE as AIRLINE, flights.DEPARTURE_DELAY as DELAY FROM flights WHERE flights.YEAR = :year AND flights.MONTH = :month AND flights.DAY = :day"

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
    If the flight was found, returns a list with a single record.
    """
    params = {'id': flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params)


# def get_flights_by_date(day: int, month: int, year: int):
#     params = {'day': day, 'month': month, 'year': year}
#     print(execute_query(QUERY_FLIGHT_BY_DATE, params))
