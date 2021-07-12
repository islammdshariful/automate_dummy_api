from jsonpath_ng import parse


def search_created_user_in(users, username):
    return [user for user in users if user['username'] == username][0]


def search_nodes_using_json_path(users, json_path):
    jsonpath_expr = parse(json_path)
    return [match.value for match in jsonpath_expr.find(users)]
