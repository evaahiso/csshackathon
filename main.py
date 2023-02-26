import time, os
from flask import Flask, render_template, request
# import Response

app = Flask(__name__)
app.static_folder = os.path.abspath('static')
app.template_folder = os.path.abspath(
  '/home/minjing/mysite/static')

# need to be user input.
# points = 200000
# n = request.args['steps'] #gets steps from health app
# request.

# 5 points = 1 char

def generate_building(building_file_path, num_of_char):
    with open('/home/minjing/mysite/static/' + building_file_path, 'r', encoding='utf-8') as file:
        building_lines = [line.rstrip() for line in file]
        building_lines.reverse()
        building_char_total = sum(len(line) for line in building_lines)

    char_printed = 0
    char_printed_total = 0

    if char_printed_total < building_char_total:
        for line in building_lines:
            for element in line:
                if char_printed < num_of_char:
                    yield element
                    time.sleep(0.01)
                    char_printed += 1
                else:
                    break
            yield "\n"

def generate(num_of_char):
    building_files = [
        "building1.txt", "building2.txt", "building3.txt", "building4.txt",
        "building5.txt"
    ]

    response = ""
    for file in building_files:
        response += "".join(generate_building(file, num_of_char))

    return response

@app.route('/')
def index():
    n = request.args.get('steps')
    if n is not None:
        num_of_char = int(n) // 5
    else:
        num_of_char = 0

    return generate(num_of_char)


if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 105)
