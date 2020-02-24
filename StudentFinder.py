import LocationCalculator

COURSE_HALF_SIZE = 10


def students_in_classes(students, classes):
    """Check for students in classes"""
    students_in_classes_result = []
    for class_room in classes:
        geo_location_box = LocationCalculator.get_geo_location_box(class_room["longitude"],
                                                                   class_room["latitude"],
                                                                   COURSE_HALF_SIZE)
        for student in students:
            if geo_location_box.is_in_box(student["latitude"], student["longitude"]):
                students_in_classes_result.append(student)
                print('Student {} is in class {}'.format(student["name"], class_room["name"]))
    return students_in_classes_result


def student_clusters_in_classes(students, classes, cluster_size):
    """Check for students in classes with minimum attendance (cluster_size)"""
    class_students_dict = {}
    for class_room in classes:
        geo_location_box = LocationCalculator.get_geo_location_box(class_room["longitude"],
                                                                   class_room["latitude"],
                                                                   COURSE_HALF_SIZE)
        for student in students:
            if geo_location_box.is_in_box(student["latitude"], student["longitude"]):
                add_student_to_class(class_students_dict, class_room["classroom"], student)
                print('Student {} is in class {}'.format(student["name"], class_room["name"]))

    students_in_classes_result = filter_students_by_class_attendance(class_students_dict, cluster_size)
    return students_in_classes_result


def add_student_to_class(class_students_dict, classroom_name, student):
    """Add student to class_students_dict using classroom_name as key"""
    if classroom_name in class_students_dict:
        class_students_dict[classroom_name].append(student)
    else:
        class_students_dict[classroom_name] = [student]


def filter_students_by_class_attendance(class_students_dic, attendance):
    """Return students in classes with at least minimum attendance"""
    filtered_students = []
    for classroom in class_students_dic.keys():
        classroom_attendance = len(class_students_dic[classroom])
        if classroom_attendance >= attendance:
            print('classroom {} has {} students or more'.format(classroom_attendance, attendance))
            filtered_students.extend(class_students_dic[classroom])
    print('filtered students: {}'.format(filtered_students))
    return filtered_students
