# @Stocpoolt
# cajero-api

# 1.

pip install fastapi
pip install uvicorn
pip install pydantic

# 2.
Crear y modificar:
	-cajero-backend
		__init__.py
		main.py
		-db
			__init__.py
			user_db.py
			transaction_db.py
		-models
			__init__.py
			user_models.py
			transaction_models.py

# 3.
Probar las funcionalidades del main.py en Postman
o en Documentación generada por FastAPI
	http://127.0.0.1:8000/docs#/
	http://127.0.0.1:8000/redoc/

# 4.
Crear y modificar:
	-cajero-bachend
		Procfile
		requirements.txt

Actualizar repositorio GitHub
Desplegar en Heroku
Probar en Postman con la URL de Heroku

























	-- Dec13 Instalación de Node.js y NPM

	• Windows	: descargar desde https://nodejs.org/en/ el ejecutable y correrlo, seguir wizard.
	• Linux		: seguir la siguiente guía: https://linuxize.com/post/how-to-install-nodejs-on-ubuntu-18.04/

node --version
npm --version

• Para probar el api en Postman
• (En backend)
uvicorn main:api --reload

• Para poder crear proyectos en Vue
npm install –g @vue/cli
vue --version

• Creación del proyecto
vue init webpack cajero-frontend

# •••
# Continúa en el README del frontend