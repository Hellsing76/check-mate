import requests
import json


def get_barcode(barcodeid):
    try:
        api = "http://db.nca.edu.ni/api/api_ewapp.php?"
        requirements = {'staff_username':"",
                    'staff_password':"",
                    'barcode':"",
                    "is_upc":bool
                    }


        r = requests.get(api+barcodeid).json()
        return "Balance: ${}\nFamily balance: ${}\nTransaction history: {}".format(r['credit_student'], r['credit_family'], r['transactions'])
    except requests.exceptions.ConnectionError:
        return "Connection unable to be established. Is the server online?"
    except KeyError:
        return "Invalid id. Please try again."
    except TypeError:
        return "Please enter an id"
    except KeyboardInterrupt:
        return "Goodbye"














