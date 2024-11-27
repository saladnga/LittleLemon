# 0. Access virtual environment:

python3 -m venv path/to/venv
source path/to/venv/bin/activate
pip3 install pipenv
pip3 install django
pip3 install mysqlclient
pip3 install djangorestframework
pip3 install djoser

# 1. This path can be used to check that web application serves static HTML content with images and styles:

/restaurant/

# 2. Unit Test:

python3 manage.py test tests

# 3. Endpoints:

# a. To login and auth get token (use Insomnia to access):

/api-token-auth/

# b. To login using Djoser endpoint:

/auth/users/
/auth/token/login/
/auth/token/logout/

# 4. Menu items:

/restaurant/menu/
/restaurant/menu/{menuItemId}

# 5. Table booking:

/restaurant/booking/tables/
/restaurant/booking/tables/{bookingId}
