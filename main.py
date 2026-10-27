from pyscript import document, display, HTML


# Predefined sets of club members from each grade level
grade_7 = {"Ennessa Grey", "Elias Reveen", "Tiarn"}
grade_8 = {"Belladonna Fierosa", "Rosa Sylvette", "Arlette Ven"}
grade_9 = {"Xui Lin", "Xander Lin", "Mireille Rosafiere"}
grade_10 = {"Lilura Minamoto", "Jonathan Timothy", "Aiden Aoyagi"}


# Combine all grade-level sets using the union operator (|)
club_roster = grade_7 | grade_8 | grade_9 | grade_10


# Function to display the updated list of club members
def show_members():

    # Sort members alphabetically and separate them with line breaks
    members_list = "<br>".join(sorted(club_roster))

    # Count the total number of unique members
    total_members = len(club_roster)

    # Display the full member list and total number of members
    display(
        HTML(f"""
            <h3>ALL MEMBERS:</h3>
            <p>{members_list}</p>
            <p><strong>TOTAL MEMBERS: {total_members}</strong></p>
        """),
        target="confirmed-members",
        append=False
    )


# Function to add a new club member
def add_member(event):

    # Prevent the form from refreshing the webpage
    event.preventDefault()

    # Get the first and last names from the text boxes
    first_name = document.getElementById("name").value.strip().title()
    last_name = document.getElementById("surname").value.strip().title()

    # Allow the function to update the master set
    global club_roster

    # Combine the first and last names into one full name
    full_name = f"{first_name} {last_name}"

    # Create a set containing the new member
    new_member = {full_name}

    # Combine the new member with the master set using union (|)
    club_roster = club_roster | new_member

    # Display the updated members and total count
    show_members()

    # Clear both text boxes after submitting
    document.getElementById("name").value = ""
    document.getElementById("surname").value = ""