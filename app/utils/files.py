import json

def save_data_to_file(data_list, filepath):
    with open(filepath, 'w') as f:
        for item in data_list:
            f.write(json.dumps(item) + '\n')