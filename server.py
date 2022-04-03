#!/usr/bin/env python3

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(filename='secrets_manager.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.WARNING)


def init_app():
    from Api.api import app
    app.run(host='0.0.0.0',
            port=os.environ.get("PORT", 5000),
            debug=bool(strtobool(os.getenv('DEBUG', 'False'))),
            use_reloader=True)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Server started...")
    init_app()
