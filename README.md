# @Stocpoolt

# ------------------------------------
# cajero-backend

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
• Para probar el api en Postman
• (En backend)
		uvicorn main:api --reload

o en Documentación generada por FastAPI
	http://127.0.0.1:8000/docs#/
	http://127.0.0.1:8000/redoc/

# 4.
Crear y modificar:
	-cajero-backend
		Procfile
		requirements.txt

Actualizar repositorio GitHub
Desplegar en Heroku
Probar en Postman con la URL de Heroku
• Para probar el api en Postman
• (En backend)
	uvicorn main:api --reload

# ------------------------------------

# 5.
Instalación de Node.js y NPM

	• Windows	: descargar desde https://nodejs.org/en/ el ejecutable y correrlo, seguir wizard.
	• Linux		: seguir la siguiente guía: https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/

	node --version
	npm --version

# Creación de proyecto en Vue
Instalación de CLI:
• Para poder crear proyectos en Vue
	npm install –g @vue/cli
	vue --version

• Creación del proyecto
• (En la raiz del proyecto)
	vue init webpack cajero-frontend

# •••
# Continúa en el README del frontend