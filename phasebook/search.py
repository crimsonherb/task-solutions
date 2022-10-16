from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


# Determine if data already in the list
def check(data, data_list):
    if data not in data_list:
        return data_list.append(data)


def search_users(args):

    # If no arguements, returns all data
    if args == {}:
        return USERS

    search_result = []

    # Iterate over search arguements to determine which parameter/s are
    # to be considered and ordered accordingly
    for key, value in args.items():
        for data in USERS:
            if key == "id":
                if data[key] == value:
                    check(data, search_result)
            elif key == "name":
                if value.lower() in data[key].lower():
                    check(data, search_result)
            elif key == "age":
                if data[key] in range(int(value)-1, int(value)+2):
                    check(data, search_result)
            elif key == "occupation":
                if value.lower() in data[key].lower():
                    check(data, search_result)

    # Return list of results
    if search_result:
        return search_result
    else:
        return ['NO RESULTS']
