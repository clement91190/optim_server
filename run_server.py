import os
from optim_server import app
import optim_server.urls

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = (port == 5000)
    app.run(host='0.0.0.0', port=port, debug=debug)
