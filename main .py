def load_events():
    events = []
    try:
        with open('events.txt', 'r') as f:
            for line in f:
                event_data = line.strip().split(',')
                event = {
                    'name': event_data[0],
                    'date': event_data[1],
                    'time': event_data[2],
                    'location': event_data[3],
                    'description': event_data[4],
                    'attendees': [] if len(event_data) < 6 else event_data[5].split(';')
                }
                events.append(event)
    except FileNotFoundError:
        pass
    return events


def save_events(events):
    with open('events.txt', 'w') as f:
        for event in events:
            event_data = [
                event['name'],
                event['date'],
                event['time'],
                event['location'],
                event['description'],
                ';'.join(event['attendees']) if 'attendees' in event else ''
            ]
            f.write(','.join(event_data) + '\n')


def add_event(events, event):
    for e in events:
        if e['location'] == event['location'] and e['date'] == event['date'] and e['time'] == event['time']:
            print("Another event already scheduled at this time and location.")
            return
    events.append(event)
    print("\nEvent added successfully.\n")


def update_event(events, event_name, field, new_value):
    found = False
    for event in events:
        if event['name'] == event_name:
            if field in event:
                event[field] = new_value
                print("\n")
                print(f"Event '{event_name}' {field} updated successfully.")
                print("\n")
                found = True
                break
            else:
                print("\n")
                print(f"Invalid field: '{field}'.")
                print("\n")
    if not found:
        print("\n")
        print(f"Event '{event_name}' not found.")
        print("\n")


def delete_event(events, event_name):
    for event in events:
        if event['name'] == event_name:
            events.remove(event)
            print("\n")
            print(f"Event '{event_name}' deleted successfully.")
            print("\n")
            return
    print("\n")
    print(f"Event '{event_name}' not found.")
    print("\n")


def register_attendees(events, event_name, attendee):
    for event in events:
        if event['name'] == event_name:
            if 'attendees' not in event:
                event['attendees'] = []
            event['attendees'].append(attendee)
            print("\n")
            print(f"{attendee} registered successfully for event '{event_name}'.")
            print("\n")
            return
    print("\n")
    print(f"Event '{event_name}' not found.")
    print("\n")

def update_attendee(events, event_name, old_name, new_name):
    for event in events:
        if event['name'] == event_name and 'attendees' in event:
            if old_name in event['attendees']:
                index = event['attendees'].index(old_name)
                event['attendees'][index] = new_name
                print("\n")
                print(f"Attendee information updated: {old_name} -> {new_name}")
                print("\n")
                return
            else:
                print("\n")
                print(f"Attendee '{old_name}' not found for event '{event_name}'.")
                print("\n")
                return
    print("\n")
    print(f"Event '{event_name}' not found or does not have any attendees.")
    print("\n")

def delete_attendee(events, event_name, attendee):
    for event in events:
        if event['name'] == event_name and 'attendees' in event:
            if attendee in event['attendees']:
                event['attendees'].remove(attendee)
                print("\n")
                print(f"{attendee} removed successfully from event '{event_name}'.")
                print("\n")
                return
            else:
                print("\n")
                print(f"Attendee '{attendee}' not found for event '{event_name}'.")
                print("\n")
                return
    print("\n")
    print(f"Event '{event_name}' not found or does not have any attendees.")
    print("\n")

def print_schedule(events):
    if not events:
        print("\n")
        print("No events scheduled.")
    else:
        print("\n")
        print("Event Schedule:\n------------------------------")
        for event in events:
            print(f"Event: {event['name']}\nDate: {event['date']}\nTime: {event['time']}\nLocation: {event['location']}\nDescription: {event['description']}\n")
            if 'attendees' in event:
                print("Attendees:", ', '.join(event['attendees']))
            print("-" * 30)


def update_event_menu(events, event_name):
    print("\nUpdate event details:")
    print("1. Update event name")
    print("2. Update event date")
    print("3. Update event time")
    print("4. Update event location")
    print("5. Update event description")
    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter new event name: ")
        update_event(events, event_name, 'name', new_name)
    elif choice == '2':
        new_date = input("Enter new event date (YYYY-MM-DD): ")
        update_event(events, event_name, 'date', new_date)
    elif choice == '3':
        new_time = input("Enter new event time (HH:MM): ")
        update_event(events, event_name, 'time', new_time)
    elif choice == '4':
        new_location = input("Enter new event location: ")
        update_event(events, event_name, 'location', new_location)
    elif choice == '5':
        new_description = input("Enter new event description: ")
        update_event(events, event_name, 'description', new_description)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    events = load_events()

    while True:
        print("\nMenu:")
        print("1. Add an event")
        print("2. Update event details")
        print("3. Delete an event")
        print("4. Register attendees for an event")
        print("5. Update attendee information")
        print("6. Delete attendee from an event")
        print("7. Print event schedule")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            location = input("Enter event location: ")
            description = input("Enter event description: ")
            add_event(events, {'name': name, 'date': date, 'time': time, 'location': location, 'description': description})
        elif choice == '2':
            event_name = input("Enter the name of the event to update: ")
            update_event_menu(events, event_name)
        elif choice == '3':
            event_name = input("Enter the name of the event to delete: ")
            delete_event(events, event_name)
        elif choice == '4':
            event_name = input("Enter the name of the event to register attendees: ")
            attendee = input("Enter name of attendee: ")
            register_attendees(events, event_name, attendee)
        elif choice == '5':
            event_name = input("Enter the name of the event: ")
            old_name = input("Enter the name of the attendee to update: ")
            new_name = input("Enter the new name for the attendee: ")
            update_attendee(events, event_name, old_name, new_name)
        elif choice == '6':
            event_name = input("Enter the name of the event: ")
            attendee = input("Enter the name of the attendee to delete: ")
            delete_attendee(events, event_name, attendee)
        elif choice == '7':
            print_schedule(events)
        elif choice == '8':
            save_events(events)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
