// npm install express
const express = require("express");
const app = express();
const PORT = 8989;

// Middleware to parse JSON body
app.use(express.json());

// Home Route
app.get("/", (req, res) => {
  res.send("Home Page");
});

// --- CW1 APIs ---

// 1. POST /contact-us
app.post("/contact-us", (req, res) => {
  res.send("I am from contact us POST API");
});

// 2. PUT /about-us
app.put("/about-us", (req, res) => {
  res.send("I am from about us PUT API");
});

// 3. DELETE /services
app.delete("/services", (req, res) => {
  res.send("I am from services DELETE API");
});

// --- Employee CRUD ---

let emps = [
  { id: 1, name: "Ansh", salary: 25000 },
  { id: 2, name: "Pooja", salary: 27000 },
  { id: 3, name: "Neha", salary: 23000 },
];

// GET /employee
app.get("/employee", (req, res) => {
  res.json(emps);
});

// POST /employee
app.post("/employee", (req, res) => {
  emps.push(req.body);
  res.send("Record added successfully...");
});

// PUT /employee/:id (update salary)
app.put("/employee/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const newSalary = req.body.salary;
  const emp = emps.find((e) => e.id === id);
  if (emp) {
    emp.salary = newSalary;
    res.send("Salary updated successfully...");
  } else {
    res.status(404).send("Employee not found.");
  }
});

// DELETE /employee/:id
app.delete("/employee/:id", (req, res) => {
  const id = parseInt(req.params.id);
  emps = emps.filter((e) => e.id !== id);
  res.send("Record deleted successfully...");
});

// Start server
app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});

// http://localhost:8989/employee/1
// {"salary": 28000 }
app.put("/employee/:id", (req, res) => {
    for(let i = 0; i < emps.length; i++) {
        if(emps[i].id == req.params.id) {
            console.log("Updating salary" + req.body.salary);
            emps[i].salary = req.body.salary 
        }
    }
    res.send("Record updated successfully...")
})