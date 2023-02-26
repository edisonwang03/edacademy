from app import app # executed file
from app.models import User, Course

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Course': Course}