import plotly.graph_objs as go
import pymongo
import stripe
from flask import *
from pymongo import *

app = Flask(__name__)  # init flask app
app.debug = True  # debug
app.secret_key = "My-School-MS"  # secret key
app.config["SECURITY_PASSWORD_SALT"] = "My-School-MS"
app.config[
    "STRIPE_PUBLIC_KEY"
] = "pk_test_51Hdf6IJzMECqGOD86djVmO4RmD2d1kKPHzxFWSN3koXkPcUDeusLHdx7ls7ZMmjyg12edFvDD9ODMKlJmlWfWpGa00AsOAIFuT"  # adding the STRIPE_PUBLIC_KEY to the flask app config
app.config[
    "STRIPE_SECRET_KEY"
] = "sk_test_51Hdf6IJzMECqGOD8M4GG7fkfxyKVCT52KSrSmMbas5iRW8baYKh3CmlQGFlV5wE3tx2Z8CvF5GLiHv8YyXAyW2w800d1zcUezW"  # adding the STRIPE_SECRET_KEY to the flask app config
stripe.api_key = app.config["STRIPE_SECRET_KEY"]
cluster = MongoClient(
    "mongodb://ranuga:ranuga@ms-shard-00-00.xrgdr.mongodb.net:27017,ms-shard-00-01.xrgdr.mongodb.net:27017,ms-shard-00-02.xrgdr.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-fwaf6t-shard-0&authSource=admin&retryWrites=true&w=majority"
)
from WEB.help_funcs import *

hp = Help_Funcs()
from WEB.routes import *
