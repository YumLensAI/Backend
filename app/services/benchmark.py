import os
from flask import jsonify

from app.utils.files import save_data_to_file
from app.utils.id_generator import gen_benchmark_id

def save_benchmark(request, path):
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({'error': 'Payload must be a list of objects'}), 400
    try:
        os.makedirs(path, exist_ok=True)
        benchmark_id = gen_benchmark_id()
        filename = f'{path}/{benchmark_id}.jsonl'
        save_data_to_file(data, filename)
        return jsonify({'benchmark-id': benchmark_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500