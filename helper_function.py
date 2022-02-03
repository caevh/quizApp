def form_variable_managment(username,password,remeber_me=''):
    user_name=username
    password=password
    remeber_me=remeber_me
    if remeber_me == True or remeber_me == False:
        return user_name, password, remeber_me
    else:
        return user_name, password
