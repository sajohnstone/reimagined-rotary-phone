# Third-party imports...
import json
import logging

from app.course import Course
from app.lesson import Lesson

log = logging.getLogger(__name__)

BASEURL = "https://staging-rest.edapp.com/v2/catalog/courses"


class CourseAndLesson:
    def get_course_and_lesson(self):
        course_response = Course().get_course()
        if course_response.ok:
            course_items = json.loads(course_response.text)
            course_index = 0
            return_value = [None] * len(course_items["items"])
            for course_item in course_items["items"]:
                return_value[course_index] = course_item
                course_id = course_item["id"]
                lesson_response = Lesson().get_lessons(course_id)
                if lesson_response.ok:
                    lesson = json.loads(lesson_response.text)
                    return_value[course_index]["lesson"] = lesson
                else:
                    return {"Error": "Lesson API return non 200 response"}
                course_index = course_index + 1
            return return_value
        return {"Error": "Course API return non 200 response"}
