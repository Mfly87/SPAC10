from app import app

import json

def setup_app():
    
    _host = "127.0.0.1"
    _port = "5000"

    with open('config.json') as f:
        _config: dict[str,any] = json.load(f)
        _dict: dict[str,str] = _config.get("flask_app", dict())
        
        _host = _dict.get("host", _host)
        _port = _dict.get("port", _port)

    app.run(debug=True, host=_host, port=_port)