// В файле main.js или в <script>
async function loadAndRenderCourses() {
    const courses = await loadCourses();
    renderCourses(courses); // Ваша существующая функция рендеринга
  }
  
  async function handleAddCourse() {
    const courseData = {
      name: document.getElementById('courseName').value,
      teacher: document.getElementById('courseTeacher').value,
      schedule: document.getElementById('courseSchedule').value,
      room: document.getElementById('courseRoom').value,
      students: document.getElementById('courseStudents').value
    };
    
    await addCourse(courseData);
    await loadAndRenderCourses();
  }
  
  async function handleDeleteCourse(id) {
    if (confirm('Вы уверены, что хотите удалить этот курс?')) {
      await deleteCourse(id);
      await loadAndRenderCourses();
    }
  }
  
  // Сделаем функции глобальными для вызова из HTML
  window.addCourse = handleAddCourse;
  window.deleteCourse = handleDeleteCourse;