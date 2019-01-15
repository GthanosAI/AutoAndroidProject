#
echo "genrate keystore"
keytool -genkeypair -alias appkey -keystore app.keystore

# make project
python CreateProject.py
