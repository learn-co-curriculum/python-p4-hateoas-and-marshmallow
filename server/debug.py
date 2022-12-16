#!/usr/bin/env python3

from app import app
from models import db, Newsletter

if __name__ == '__main__':
    
    db.init_app(app)
    with app.app_context():
        import ipdb; ipdb.set_trace()
