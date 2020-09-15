from ImageGoNord import GoNord
from flask import Flask
from flask import jsonify, abort
from flask import request
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from werkzeug.datastructures import FileStorage

API_VERSION = 'v1'
API_VERSION_URL = '/' + API_VERSION

app = Flask(__name__)
cors = CORS(app)
api = Api(app, version=API_VERSION, prefix=API_VERSION_URL, title='Image go nord API')

success_model = api.model('StatusModel', {
    'ok': fields.Boolean
})


@api.route('/status', doc={'description': 'Check server online'})
class StatusEndpoint(Resource):

    @api.response(200, 'Success, server online', success_model)
    def get(self):
        return {'ok': True}


parser = api.parser()

# How is it used?
parser.add_argument('file_path', type=str, help='Image File path', location='form')
parser.add_argument('file', help='File posted by form', type=FileStorage, location='files')
parser.add_argument('b64_input', help='Image in base 64 format', type=str, location='form')

# How is used without it?
parser.add_argument('b64_output', help='Should it return base64 image?', type=bool, location='form')

# How is it used?
# convert_parser.add_argument('output_path', help='Define output path', type=str, location='b64_input')

# TODO: Check code for this feature
# convert_parser.add_argument('width', type=bool, help=' Resize image if defined height too', location='form')
# convert_parser.add_argument('height', type=bool, help=' Resize image if defined width too', location='form')

converted_image_model = api.model('ConvertedImage', {
    'success': fields.Boolean,
    'b64_img': fields.String,
})


@api.route('/convert', doc={'description': 'Covert image api posting images'})
class ConvertEndpoint(Resource):

    @api.expect(parser)
    @api.response(200, 'Success, image converted', converted_image_model)
    @api.response(400, 'Validation Error, something go wrong')
    def post(self):
        go_nord = setup_instance(request)
        output_path = ''
        response = {'success': True}

        if request.files.get('file'):
            image = go_nord.open_image(request.files.get('file').stream)
        elif request.form.get('file_path'):
            image = go_nord.open_image(request.form.get('file_path'))
        elif request.form.get('b64_input'):
            image = go_nord.base64_to_image(request.form.get('b64_input'))
        else:
            abort(400, 'You need to provide at least a valid image or image path')

        if request.form.get('width') and request.form.get('height'):
            image = go_nord.resize_image(image)

        if request.form.get('output_path'):
            output_path = request.form.get('output_path')

        image = go_nord.convert_image(image, save_path=output_path)

        if request.form.get('b64_output'):
            b64_image = go_nord.image_to_base64(image, 'jpeg')
            base64_img_string = b64_image.decode('UTF-8')
            response['b64_img'] = base64_img_string

        return response


@api.route('/quantize', doc={'description': 'Quantize image using pillow'})
class ConvertEndpoint(Resource):

    @api.expect(parser)
    @api.response(200, 'Success, image quantized', converted_image_model)
    @api.response(400, 'Validation Error, something go wrong')
    def post(self):

        go_nord = setup_instance(request)
        output_path = ''
        response = {'success': True}

        if request.files.get('file'):
            image = go_nord.open_image(request.files.get('file').stream)
        elif request.form.get('file_path'):
            image = go_nord.open_image(request.form.get('file_path'))
        elif request.form.get('b64_input'):
            image = go_nord.base64_to_image(request.form.get('b64_input'))
        else:
            abort(400, 'You need to provide at least a valid image or image path')

        if request.form.get('width') and request.form.get('height'):
            image = go_nord.resize_image(image)

        if request.form.get('output_path'):
            output_path = request.form.get('output_path')

        image = go_nord.quantize_image(image, save_path=output_path)

        if request.form.get('b64_output'):
            b64_image = go_nord.image_to_base64(image, 'jpeg')
            base64_img_string = b64_image.decode('UTF-8')
            response['b64_img'] = base64_img_string

        return response


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
    app.run(port=8000, threaded=True)
