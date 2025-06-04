from flask import Flask

from app.routes.predict import predict_bp
from app.routes.benchmark import benchmark_bp

app = Flask(__name__)

app.register_blueprint(predict_bp)
app.register_blueprint(benchmark_bp)

@app.route('/')
def health_check():
    return "Ok"