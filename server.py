from flask import render_template

@app.route('/')
def index():
    # Получаем статистику из базы данных
    stats = {
        'student_count': Student.query.count(),
        'teacher_count': Teacher.query.count(),
        'course_count': Course.query.count(),
    }
    
    # Пример последних действий (можно заменить реальными данными)
    recent_actions = [
        {'icon': 'person-plus', 'color': 'primary', 'description': 'Добавлен новый студент: Иванов И.И.', 'time': '10 мин назад'},
        {'icon': 'journal-plus', 'color': 'info', 'description': 'Создан новый курс: Веб-разработка', 'time': '1 час назад'},
        {'icon': 'calendar-check', 'color': 'success', 'description': 'Занятие по Python завершено', 'time': '3 часа назад'}
    ]
    
    return render_template('index.html', 
                         student_count=stats['student_count'],
                         teacher_count=stats['teacher_count'],
                         course_count=stats['course_count'],
                         recent_actions=recent_actions)
                         @app.route('/students')
def students():
    students = Student.query.all()  # Получаем студентов из БД
    return render_template('student.html', students=students)
    @app.route('teacher')
def teachers():
    teachers = Teacher.query.all()  # Получаем преподавателей из БД
    return render_template('teacher.html', teachers=teachers)
    @app.route('courses')
def courses():
    courses = Course.query.all()  # Получаем курсы из БД
    return render_template('courses.html', courses=courses)
    @app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Обработка данных формы
        new_student = Student(
            last_name=request.form['lastName'],
            first_name=request.form['firstName'],
            # ... остальные поля
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('students'))
    return render_template('student_add.html')

    from flask import request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Конфигурация загрузки файлов
UPLOAD_FOLDER = 'static/uploads/students'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            # Обработка загрузки фото
            photo_path = None
            if 'photo' in request.files:
                file = request.files['photo']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    unique_filename = f"{datetime.now().timestamp()}_{filename}"
                    save_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    file.save(save_path)
                    photo_path = f"uploads/students/{unique_filename}"
            
            # Преобразование дат
            admission_date = datetime.strptime(request.form['admission_date'], '%Y-%m-%d').date()
            birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date() if request.form['birth_date'] else None
            
            # Создание нового студента
            new_student = Student(
                last_name=request.form['last_name'],
                first_name=request.form['first_name'],
                middle_name=request.form['middle_name'],
                group=request.form['group'],
                course=int(request.form['course']),
                student_id=request.form['student_id'],
                admission_date=admission_date,
                email=request.form['email'],
                phone=request.form['phone'],
                address=request.form['address'],
                birth_date=birth_date,
                performance=float(request.form['performance']) if request.form['performance'] else None,
                notes=request.form['notes'],
                photo_path=photo_path
            )
            
            db.session.add(new_student)
            db.session.commit()
            
            # Обработка выбранных курсов
            selected_courses = request.form.getlist('courses')
            for course_id in selected_courses:
                course = Course.query.get(int(course_id))
                if course:
                    new_student.courses.append(course)
            
            db.session.commit()
            
            flash('Студент успешно добавлен!', 'success')
            return redirect(url_for('students'))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Ошибка при добавлении студента: {str(e)}', 'danger')
    
    # Для GET запроса - отображаем форму
    courses = Course.query.all()
    return render_template('student_add.html', courses=courses)
    from extensions import csrf
csrf.init_app(app)