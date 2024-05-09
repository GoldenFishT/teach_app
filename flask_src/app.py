from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, abort

app = Flask(__name__)
api = Api(app)

lesson_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'teacher': fields.String,
    'content': fields.String
}

class Lesson(object):
    def __init__(self, id,title, teacher, content):
        self.id = id
        self.title = title
        self.teacher = teacher
        self.content = content

    def __repr__(self):
        return f'{self.id}: {self.title} by {self.teacher}'

lessons = []
for i in range(3):
    l = Lesson(i, 'titles'+str(i), 'teachers'+str(i), 'content'+str(i))
    lessons.append(l)

def abort_if_id_doesnot_exist(lesson_id):
    if lesson_id not in range(len(lessons)):
        abort(404, message=f"Lesson {lesson_id} doesn't exist.")
        
class AllLessons(Resource):
    @marshal_with(lesson_fields)
    def get(self, **kwargs):
        return lessons

class SingleLesson(Resource):
    @marshal_with(lesson_fields)
    def get(self, lesson_id=None,**kwargs):
        if lesson_id:
            print(lesson_id)
            abort_if_id_doesnot_exist(lesson_id)
            return lessons[lesson_id]
        return None



api.add_resource(AllLessons,
                 '/',
                 '/lessons')
api.add_resource(SingleLesson,
                 '/<int:lesson_id>',
                 '/lessons/<int:lesson_id>')

if __name__ == '__main__':
    app.run(debug=True)
