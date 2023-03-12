const express = require("express");
const logger = require('morgan')
const path = require('path');
const session = require("express-session")
const passport = require("passport")
const LocalStrategy = require("passport-local").Strategy
const PORT = 4000;
const BodyParser = require("body-parser")
const { Pool } = require("pg");
const CookieParser = require('cookie-parser')


const pool = new Pool({
    host: "db-postgresql-nyc1-07777-do-user-10755856-0.b.db.ondigitalocean.com",
    user: "doadmin",
    password: "AVNS_vTq8woZ41dehfRBnKRt",
    database: "matcher",
    ssl: {
        require: true, // This will help you. But you will see nwe error
        rejectUnauthorized: false // This line will fix new error
      },
    port: 25060
})

    
app = express();


app.use(CookieParser())

app.set("view engine", "ejs")
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

app.get('/home', (req, res) =>{
    res.render('home')
})

app.get('/home/student', (req, res) => {
    res.render('student')
})
app.post('/home/student', (req, res) => {
    email = req.body.email
    subject = req.body.subject 
})

app.get('/home/tutor', (req, res) => {
    res.render('tutor')
})
app.post('/home/tutor', (req, res) => {
    email = req.body.email
    subject = req.body.subject
    amount = req.body.amount
})








app.get('/register', (req, res) => {
 res.render('register')
})



app.listen(PORT, ()=> {
    console.log("Listening on port " + PORT);
});



  