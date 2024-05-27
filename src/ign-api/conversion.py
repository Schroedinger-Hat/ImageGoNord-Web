from flask import abort
from flask import request
from flask_cors import cross_origin
from flask import Blueprint

from ImageGoNord import GoNord

from rq import Queue
from worker import conn
import os
from datetime import datetime


q = Queue(connection=conn)
API_VERSION = '/v1'

convert_async_api = Blueprint('convert_async_api', __name__)

@convert_async_api.route(API_VERSION + "/convert-async", methods=["POST"])
@cross_origin(origin='*')
def convert_queue():
  go_nord = setup_instance(request)
  output_path = ''
  response = {'success': True}
  file = None
  palette_name = 'Nordtheme'

  if (request.files.get('file') != None):
    file = request.files.get('file')
  elif (request.form.get('file_path') != None): # not used in the website
    image = go_nord.open_image(request.form.get('file_path'))
  elif (request.form.get('b64_input') != None): # not used in the website
    image = go_nord.base64_to_image(request.form.get('b64_input'))
  else:
    abort(400, 'You need to provide at least a valid image or image path')

  if (request.form.get('output_path') != None):
    output_path = request.form.get('output_path')

  if (request.form.get('palette_name') != None):
    palette_name = request.form.get('palette_name')
  
  use_model = request.form.get('is_ai') is not None
  conn.incr('conversion_count', 1)

  if is_image(file.filename):
    image = go_nord.open_image(request.files.get('file').stream)
    job = q.enqueue(f=convert_image, ttl=900, failure_ttl=900, job_timeout='180s', args=(go_nord, image, output_path, request.form.get('b64_output'), response, use_model))
  elif is_video(file.filename):
    now = datetime.now() # current date and time
    filename = now.strftime("%m%d%Y-%H%M%S")
    path_to_video = os.path.join('/tmp', 'ign-video-' + filename + '.' + file.filename.rsplit('.', 1)[1])
    file.save(path_to_video)
    job = q.enqueue(f=convert_video, ttl=900, failure_ttl=900, job_timeout='900s', args=(go_nord, palette_name, path_to_video))
  else:
    abort(400, 'No valid file: you can upload video in mp4, avi, webp and mov and images (up to 16MB)')

  return job.id

def is_video(filename):
  return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ['mp4', 'mov', 'avi', 'webm']

def is_image(filename):
  return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg']

def convert_image(go_nord, image, save_path, b64_output, response, use_model=False):
  image = go_nord.convert_image(image, save_path=save_path, use_model=use_model)
  if (b64_output != None):
    b64_image = go_nord.image_to_base64(image, 'png')
    base64_img_string = b64_image.decode('UTF-8')
    response['b64_img'] = base64_img_string

  return response

def convert_video(go_nord, palette_name, path_to_video):
  try:
    output_path = go_nord.convert_video(path_to_video, '/tmp/' + palette_name)
  finally:
    os.remove(path_to_video)

  return {'output_path': output_path}

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