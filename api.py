import requests


def get_credit_with_login(username, password):
    # function using NCAI login to get credit_student and credit_family
    try:
        if username in '' or password in '':
            return "Please enter a username and password"
        api = "http://db.nca.edu.ni/api/api_ewapp.php?mode=student&query=login&username={}&password={}".format(username, password)
        response = requests.get(api).json()
        if response['login_status'] is 0:
            return "Invalid login. Please try again."
        return "Your balance: ${}\nFamily balance: ${}".format(response['credit_student'], response['credit_family'])
    except requests.exceptions.ConnectionError:
        return "Connection unable to be established.\nIs the server online?"


def get_credit_with_mock(user_id):
    try:
        api = "http://localhost:3000/api/"
        response = requests.get(api + user_id).json()
        return "Your balance: ${}\nFamily balance: ${}".format(response['credit_student'], response['credit_family'])
    except requests.exceptions.ConnectionError:
        return "Connection unable to be established. Is the server online?"
    except KeyError:
        return "Invalid id. Please try again."
    except TypeError:
        return "Please enter an id"


def get_credit_with_scanner():
    # function for use with the real API system
    pass
