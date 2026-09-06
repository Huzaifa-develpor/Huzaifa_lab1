# Travel Agent (Flight Booking Agent)
# PEAS: Performance = cheapest/fastest flight | Environment = flight data
#       Actuators = display/book flight | Sensors = user input
# Agent Type: Goal-Based Agent

# ---------------- ENVIRONMENT ----------------
FLIGHT_DATABASE = [
    {"id": "F101", "from": "Karachi", "to": "Lahore",    "price": 12000, "time": "08:00 AM"},
    {"id": "F102", "from": "Karachi", "to": "Lahore",    "price": 9500,  "time": "01:30 PM"},
    {"id": "F103", "from": "Karachi", "to": "Lahore",    "price": 15000, "time": "07:00 PM"},
    {"id": "F201", "from": "Karachi", "to": "Islamabad", "price": 13500, "time": "09:15 AM"},
    {"id": "F202", "from": "Karachi", "to": "Islamabad", "price": 11000, "time": "04:45 PM"},
    {"id": "F301", "from": "Lahore",  "to": "Islamabad", "price": 7000,  "time": "10:00 AM"},
    {"id": "F302", "from": "Lahore",  "to": "Karachi",   "price": 9800,  "time": "06:20 PM"},
]


# ---------------- SENSORS ----------------
def sense_user_request():
    print("=" * 50)
    print("   TRAVEL AGENT - Flight Booking Assistant")
    print("=" * 50)
    departure = input("Enter your departure city: ").strip().title()
    destination = input("Enter your destination city: ").strip().title()
    return departure, destination


def sense_preference():
    print("\nHow should I choose your flight?")
    print("  1. Cheapest flight")
    print("  2. Earliest flight")
    choice = input("Enter choice (1/2): ").strip()
    return "cheapest" if choice != "2" else "earliest"


# ---------------- AGENT ----------------
class TravelAgent:
    def __init__(self, flight_database):
        self.flight_database = flight_database
        self.state = {}

    def search_flights(self, departure, destination):
        matches = [
            f for f in self.flight_database
            if f["from"] == departure and f["to"] == destination
        ]
        self.state["from"] = departure
        self.state["to"] = destination
        self.state["matches"] = matches
        return matches

    def choose_best_flight(self, matches, preference):
        if preference == "earliest":
            return sorted(matches, key=lambda f: f["time"])[0]
        return sorted(matches, key=lambda f: f["price"])[0]


# ---------------- ACTUATORS ----------------
def display_flights(matches):
    print(f"\n{len(matches)} flight(s) found:\n")
    for f in matches:
        print(f"  [{f['id']}]  {f['from']} -> {f['to']}  |  "
              f"Rs. {f['price']}  |  Departure: {f['time']}")


def book_flight(flight):
    print("\nBooking your flight...")
    print(f"  Flight {flight['id']} ({flight['from']} -> {flight['to']}) "
          f"at {flight['time']} for Rs. {flight['price']}")
    print("Flight booked successfully! Have a safe journey.")


def display_no_flights():
    print("\nSorry, no flights are available for this route.")


# ---------------- MAIN ----------------
def run_travel_agent():
    agent = TravelAgent(FLIGHT_DATABASE)

    departure, destination = sense_user_request()
    matches = agent.search_flights(departure, destination)

    if not matches:
        display_no_flights()
        return

    display_flights(matches)
    preference = sense_preference()
    best_flight = agent.choose_best_flight(matches, preference)
    book_flight(best_flight)


if __name__ == "__main__":
    run_travel_agent()
