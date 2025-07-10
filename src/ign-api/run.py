from ImageGoNord import GoNord
from flask import Flask
from flask import jsonify, abort
from flask import request, send_file
from flask_cors import CORS, cross_origin

from rq import Queue
from rq.job import Job
from worker import conn

from conversion import convert_async_api
import os

q = Queue(connection=conn)
API_VERSION = '/v1'
API_VERSION_URL = '/' + API_VERSION

app = Flask(__name__)
CORS(app, resources={r"/v1/*": {"origins": "https://ign.schroedinger-hat.org"}})
app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['MAX_CONTENT_LENGTH'] = 128 * 1000 * 1000 # 128MB

app.register_blueprint(convert_async_api)

@app.route(API_VERSION + "/status", methods=["GET"])
@cross_origin(origin='*')
def get_api_status():
  return jsonify({'ok': True, 'count': str(conn.get('conversion_count'))})

@app.route(API_VERSION + "/quantize", methods=["POST"])
@cross_origin(origin='*')
def quantize():
  go_nord = setup_instance(request)
  output_path = ''
  response = {'success': True}

  if (request.files.get('file') != None):
    image = go_nord.open_image(request.files.get('file').stream)
  elif (request.form.get('file_path') != None):
    image = go_nord.open_image(request.form.get('file_path'))
  elif (request.form.get('b64_input') != None):
    image = go_nord.base64_to_image(request.form.get('b64_input'))
  else:
    abort(400, 'You need to provide at least a valid image or image path')

  if (request.form.get('width') and request.form.get('height')):
    image = go_nord.resize_image(image)

  if (request.form.get('output_path') != None):
    output_path = request.form.get('output_path')

  image = go_nord.quantize_image(image, save_path=output_path)
  
  if (request.form.get('b64_output') != None):
    b64_image = go_nord.image_to_base64(image, 'png')
    base64_img_string = b64_image.decode('UTF-8')
    response['b64_img'] = base64_img_string
  
  return jsonify(response)

@app.route(API_VERSION + "/convert", methods=["POST"]) # not used in website
@cross_origin(origin='*')
def convert():
  go_nord = setup_instance(request)
  output_path = ''
  response = {'success': True}

  if (request.files.get('file') != None):
    image = go_nord.open_image(request.files.get('file').stream)
  elif (request.form.get('file_path') != None):
    image = go_nord.open_image(request.form.get('file_path'))
  elif (request.form.get('b64_input') != None):
    image = go_nord.base64_to_image(request.form.get('b64_input'))
  else:
    abort(400, 'You need to provide at least a valid image or image path')

  if (request.form.get('width') and request.form.get('height')):
    image = go_nord.resize_image(image)

  if (request.form.get('output_path') != None):
    output_path = request.form.get('output_path')

  image = go_nord.convert_image(image, save_path=output_path)
  
  if (request.form.get('b64_output') != None):
    b64_image = go_nord.image_to_base64(image, 'png')
    base64_img_string = b64_image.decode('UTF-8')
    response['b64_img'] = base64_img_string
  
  return jsonify(response)


@app.route(API_VERSION + "/get-job", methods=["GET"])
@cross_origin(origin='*')
def get_job_result():
  job = Job.fetch(request.args.get('job_id'), connection=conn)
  result = job.result
  f = None
  if result == None:
    result = False
  elif 'output_path' in result:
    f = send_file(result['output_path'], as_attachment=True, cache_timeout=0)
    os.remove(result['output_path'])

  return jsonify({'status': job.get_status(), 'result': result}) if f == None else f

def setup_instance(req):
    go_nord = GoNord()

    hex_colors = []
    if req.form.get('colors'):
        hex_colors = req.form.get('colors').split(',')

    if len(hex_colors) > 0:
        go_nord.reset_palette()
        for hex_color in hex_colors:
            go_nord.add_color_to_palette(hex_color)

    if req.form.get('is_avg'):
        go_nord.enable_avg_algorithm()

    if req.form.get('avg_box_width') and req.form.get('avg_box_height'):
        go_nord.set_avg_box_data(int(req.form.get('avg_box_width')), int(req.form.get('avg_box_height')))

    if req.form.get('blur'):
        go_nord.enable_gaussian_blur()

    return go_nord


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, threaded=True)
