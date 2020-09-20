# Mule_jvm4.0
Flask web application used for Mulesoft JVM provision for internal use

simple flask web application

This is flask web application used to provision the JVM and update the Database accordingly.

gunicorn app:app -c gunicorn.conf.py --daemon

Command to start Gunicorn

gunicorn <application_file>:app -c <config_file> --daemon
