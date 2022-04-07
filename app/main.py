from app.course_and_lesson import CourseAndLesson  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    course_and_lesson_json = (
        CourseAndLesson().get_course_and_lesson().text
    )  # pragma: no cover
    print(course_and_lesson_json)  # pragma: no cover
