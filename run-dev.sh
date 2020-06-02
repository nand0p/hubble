#!/bin/sh

cd app
ls -la

export FLASK_APP=index.py
export FLASK_ENV=development
export FLASK_DEBUG=1

flask run --port=5000
