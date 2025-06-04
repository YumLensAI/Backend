from flask import Blueprint, request

from app.services.benchmark import save_benchmark

benchmark_bp = Blueprint('benchmark', __name__)

@benchmark_bp.route('/benchmarks/local', methods=['POST'])
def save_benchmark_local():
    return save_benchmark(request, path='benchmarks/local')

@benchmark_bp.route('/benchmarks/backend', methods=['POST'])
def save_benchmark_backend():
    return save_benchmark(request, path='benchmarks/backend')