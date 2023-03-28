# build_files.sh
echo "building"
pip install -r requirements.txt
python manage.py collectstatic
python manage.py runserver
