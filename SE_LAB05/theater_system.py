"""Movie theater seat reservation system."""
import hashlib
import json
import logging
import os

SHOWS = {
    "SHOW-1": {"title": "Interstellar", "seats": 20, "booked": []},
    "SHOW-2": {"title": "Dangal", "seats": 10, "booked": []},
}


def _record(system_logs, message):
    """Store a message in the given log list and in the logging module."""
    system_logs.append(message)
    logging.info(message)


def reserve_seat(show_id, seat_number, system_logs=None):
    """Reserve a seat for a show. Return True if it was booked."""
    if system_logs is None:
        system_logs = []
    show = SHOWS.get(show_id)
    if show is None:
        _record(system_logs, f"Unknown show {show_id}")
        return False
    valid = isinstance(seat_number, int) and 1 <= seat_number <= show["seats"]
    if not valid:
        _record(system_logs, f"Invalid seat {seat_number} for {show_id}")
        return False
    if seat_number in show["booked"]:
        _record(system_logs, f"Seat {seat_number} taken for {show_id}")
        return False
    show["booked"].append(seat_number)
    _record(system_logs, f"Reserved seat {seat_number} for {show_id}")
    return True


def release_seat(show_id, seat_number):
    """Release a booked seat. Return True if it was released."""
    try:
        SHOWS[show_id]["booked"].remove(seat_number)
    except (KeyError, ValueError):
        logging.warning("Cannot release seat %s for %s", seat_number, show_id)
        return False
    return True


def ticket_code(show_id, seat_number):
    """Return a short ticket code for a show and seat."""
    raw = (show_id + str(seat_number)).encode()
    return hashlib.sha256(raw).hexdigest()[:8]


def dump_reservations(file="seats.json"):
    """Save all reservations to a JSON file."""
    with open(file, "w", encoding="utf-8") as handle:
        json.dump(SHOWS, handle)


def load_reservations(file="seats.json"):
    """Load reservations from a JSON file."""
    with open(file, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    SHOWS.clear()
    SHOWS.update(data)


def print_seating_summary():
    """Print free and booked seats for every show."""
    for show in SHOWS.values():
        free = show["seats"] - len(show["booked"])
        print(f"{show['title']}: {free} seats free, "
              f"booked = {show['booked']}")


def main():
    """Run the demo reservation flow."""
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 5)
    reserve_seat("SHOW-1", 25)
    reserve_seat("SHOW-2", -1)
    reserve_seat("SHOW-2", "A7")
    release_seat("SHOW-2", 3)
    print("Ticket code:", ticket_code("SHOW-1", 5))
    raw = input("Seat number to book for SHOW-2 (Enter for 4): ") or "4"
    try:
        seat = int(raw)
    except ValueError:
        logging.warning("Invalid seat number entered: %s", raw)
    else:
        reserve_seat("SHOW-2", seat)
    dump_reservations()
    load_reservations()
    print_seating_summary()
    os.chmod("seats.json", 0o600)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s: %(message)s"
    )
    main()
