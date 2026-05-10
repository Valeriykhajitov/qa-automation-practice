def register_player(name, email):
    if name is None or email is None:
        return "Error: please fill required fields!"
    elif len(name) <= 3:
        return "Error: the name is too short"
    else:
        return f"User {name} is registered. Email: {email}"

def test_successful_registration():
    assert register_player("Dingus", "dingus@game.com") == "User Dingus is registered. Email: dingus@game.com"

def test_none_email():
    assert register_player("Dingus", None) == "Error: please fill required fields!"

def test_short_name():
    assert register_player("Al", "al@game.com") == "Error: the name is too short"