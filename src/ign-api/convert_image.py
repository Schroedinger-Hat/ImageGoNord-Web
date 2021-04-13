from flask import Flask
from flask import jsonify, abort
from flask import request
from flask_cors import CORS, cross_origin

from ImageGoNord import GoNord, NordPaletteFile

from rq import Queue
from rq.job import Job
from worker import conn
from __main__ import app, API_VERSION, q, cors

@app.route(API_VERSION + "/convert-async", methods=["POST"])
@cross_origin(origin='*')
def convert_queue():
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

  # convert_image(go_nord, image, output_path, request, response)
  job = q.enqueue(f=convert_image, job_timeout='60s', args=(go_nord, image, output_path, request, response))
  
  return job.id

def convert_image(go_nord, image, save_path, request, response):
  print("converto")
  image = go_nord.convert_image(image, save_path=save_path)
  if (request.form.get('b64_output') != None):
    print("imageto64")
    b64_image = go_nord.image_to_base64(image, 'png')
    base64_img_string = b64_image.decode('UTF-8')
    response['b64_img'] = base64_img_string

  print(response)
  return response

def setup_instance(req):
  go_nord = GoNord()

  hex_colors = []
  if (req.form.get('colors') != None):
    hex_colors = req.form.get('colors').split(',')

  if (len(hex_colors) > 0):
    go_nord.reset_palette()
    for hex_color in hex_colors:
      go_nord.add_color_to_palette(hex_color)

  if (req.form.get('is_avg') != None):
    go_nord.enable_avg_algorithm()

  if (req.form.get('avg_box_width') != None and req.form.get('avg_box_height') != None):
    go_nord.set_avg_box_data(int(req.form.get('avg_box_width')), int(req.form.get('avg_box_height')))

  if (req.form.get('blur') != None):
    go_nord.enable_gaussian_blur()

  return go_nord