# lib/badges_and_schedules.py

def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    return [f"Hello, {speaker}! You'll be assigned to room {index + 1}!" for index, speaker in enumerate(speakers)]

def printer(names):
    # Print badges
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    # Print room assignments
    rooms = assign_rooms(names)
    for room in rooms:
        print(room)
