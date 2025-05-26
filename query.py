QUERY_FLIGHT_BY_ID = """
SELECT 
    flights.ID,  
    flights.ORIGIN_AIRPORT,
    flights.DESTINATION_AIRPORT,
    airlines.AIRLINE,
    flights.DEPARTURE_DELAY as DELAY 
FROM flights 
    JOIN airlines ON flights.AIRLINE = airlines.ID 
WHERE flights.ID = :id; """

QUERY_FLIGHT_BY_DATE = """
SELECT 
    flights.ID, 
    flights.ORIGIN_AIRPORT, 
    flights.DESTINATION_AIRPORT, 
    airlines.AIRLINE, 
    flights.DEPARTURE_DELAY as DELAY 
FROM flights 
    JOIN airlines ON flights.AIRLINE = airlines.ID
WHERE flights.YEAR = :year AND flights.MONTH = :month AND flights.DAY = :day
"""

QUERY_DELAYED_FLIGHT_BY_AIRLINE ="""
SELECT 
    flights.ID, 
    flights.ORIGIN_AIRPORT, 
    flights.DESTINATION_AIRPORT,
    airlines.AIRLINE,
    flights.DEPARTURE_DELAY as DELAY 
FROM flights 
    JOIN airlines ON flights.AIRLINE = airlines.ID 
WHERE flights.DEPARTURE_DELAY IS NOT NULL AND flights.DEPARTURE_DELAY != '' AND flights.DEPARTURE_DELAY >= 20 AND airlines.airline = :airline 
"""