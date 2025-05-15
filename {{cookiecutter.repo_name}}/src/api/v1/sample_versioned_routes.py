"""README
This is where we start writing our api's


- You may rename the variables according to your needs .
    for e.g :
        you may rename `sample_api_v1_bp` to `module_v1`

- In case you don't require versioning altogether , you may move out
    this file & delete the `/v1` folder altogether
    - consequently , you'll just have to modify the import statement in `app.py` file .

NOTE : remove this comment ( in triple quotes ) after you have read and understood . 
"""

from flask import (
    Blueprint,
    jsonify
)

__version__ = "v1"

sample_api_v1_bp = Blueprint(
    'sample_api_v1',
    __name__,
)

# You may remove the below api :
@sample_api_v1_bp.route('/sample-route', methods=['GET'])
def sample_route():
    """This is for demonstration"""
    return jsonify({"message": f"this is a sample api : version : {__version__}"})

# Start writing your api's here ...