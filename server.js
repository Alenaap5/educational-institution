
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

let courses = [
  { id: 1, name: 'Веб-разработка', teacher: 'Петров С.И.' },
  { id: 2, name: 'Базы данных', teacher: 'Иванова М.П.' }
];

// Маршруты API
app.get('/api/courses', (req, res) => {
  res.json(courses);
});

app.post('/api/courses', (req, res) => {
  const newCourse = { id: courses.length + 1, ...req.body };
  courses.push(newCourse);
  res.status(201).json(newCourse);
});

app.delete('/api/courses/:id', (req, res) => {
  courses = courses.filter(c => c.id !== parseInt(req.params.id));
  res.sendStatus(204);
});

const PORT = 3000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Сервер запущен на http://192.168.50.200:${PORT}`);
});