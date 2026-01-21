# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as file:
        content = file.read()
    if not content.strip().startswith('['):
        content = '[' + content + ']'

    data = json.loads(content)

    total_sum = sum(item["score"] * item["weight"] for item in data)
    return round(total_sum, 3)

if __name__ == "__main__":
    print(task())
