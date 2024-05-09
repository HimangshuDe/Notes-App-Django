echo "BUILD START"
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt
python3.11 manage.py collectstatic --noinput --clear
python3.11 manage.py makemigrations
python3.11 manage.py migrate
python3.11 manage.py createsuperuser --noinput --username=admin --email=admin@admin.com
echo "BUILD END"