from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD='postgresql',
    usuario="moredev",
    senha="123456",
    servidor="localhost:5442",
    database="postgres"
)

db = SQLAlchemy(app)
app.secret_key = "moredevs"
