import logging

from lib.api.server import compress, server
import lib.api.auth
import lib.api.db
import lib.api.pysdutil
import lib.api.routes

logging.basicConfig(level=logging.DEBUG)

# Run as local dev server when executed from command line
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    compress.init_app(server)
    server.run(debug=True)
