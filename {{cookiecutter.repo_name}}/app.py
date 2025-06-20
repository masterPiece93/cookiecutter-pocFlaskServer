import logging
from flask import Flask
from src.generic_routes import generic_bp
from src.api.sample_api_routes import sample_api_bp
from src.api.v1.sample_versioned_routes import sample_api_v1_bp
from src.api.v2.sample_versioned_routes import sample_api_v2_bp
from commandline import parser

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Line 16 debuger is working")

app = Flask(__name__)
app.config.from_object('setup.config.Config')

# Route Registration
app.register_blueprint(generic_bp)
app.register_blueprint(sample_api_bp, url_prefix="/api")
app.register_blueprint(sample_api_v1_bp, url_prefix="/api/v1")
app.register_blueprint(sample_api_v2_bp, url_prefix="/api/v2")

if __name__ == '__main__':

    # Commandline Arguments
    args = parser.parse_args()
    execution_type: str = args.execute # Fetching commandline args

    # Running Server
    app.run(
        host="0.0.0.0",
        port=app.config["PORT"]
    )
