from pyscript import document, display, HTML

def check_membership(e):
    document.getElementById("confirmed-members").innerHTML = ""

    grade_7 = {"Ennessa Grey", "Elias Reveen", "Tiarn "}
    grade_8 = {"Belladonna Fierosa", "Rosa Sylvette", "Arlette Ven"}
    grade_9 = {"Xui M. Lin", "Xander M. Lin", "Mireille Rosafiere"}
    grade_10 = {"Lilura Minamoto", "Jonathan Timothy III", "Aiden Aoyagi"}

    club_roster = grade_7 | grade_8 | grade_9 | grade_10

def add_member(e):
    first_name = document.getElementById("name").value.strip()
    last_name = document.getElementById("surname").value.strip()

