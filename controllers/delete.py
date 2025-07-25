from flask import Flask, render_template, redirect, Response, request, Blueprint
from models.models import *

delete = Blueprint("delete", __name__)
