openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=DO/ST=SantoDomingo/L=SantoDomingo/O=Django-Angular-App/OU=IT/CN=backend"
