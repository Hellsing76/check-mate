import requests


def get_balance_with_mock(user_id):
    try:
        api = "http://localhost:3000/api/"
        response = requests.get(api + user_id).json()
        return "Balance: ${}\nFamily balance: ${}".format(response['credit_student'], response['credit_family'])
    except requests.exceptions.ConnectionError:
        return "Connection unable to be established. Is the server online?"
    except KeyError:
        return "Invalid id. Please try again."
    except TypeError:
        return "Please enter an id"
    except KeyboardInterrupt:
        return "Goodbye"
