<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div class="container" id="assignment">
        <nav class="mt-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Admin</a></li>
                <li class="breadcrumb-item"><a href="#" class="current">Course Assignment</a></li>
            </ol>
        </nav>
        <div class="row">
            <div class="col">
                <p class="title">Course Assignment</p>
            </div>
        </div>
        <div class="row bg-primary">
            <div class="col-11 p-2">
                <div class="row">
                    <div class="col-4">
                        <input v-on:keyup="searchStudent" v-model="studentInput" class="form-control" type="text" placeholder="Name" aria-label="Name" />
                    </div>
                    <div class="col-4">
                        <input v-on:keyup="searchCourse" v-model="courseInput" class="form-control" type="text" placeholder="Course" aria-label="Course" />
                    </div>
                    <div class="col-4">
                        <select v-if="!classes.length" class="form-select" disabled>
                            <option selected>Select a Class</option>
                        </select>
                        <select v-else class="form-select" id="classDropdown">
                            <option selected>Select a Class</option>
                            <option v-for="classitem in classes" v-bind:value="classitem.classID">Class {{ classitem.classID }}</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="col-1 p-2 text-center">
                <button class="btn btn-default" type="button">
                    Assign
                </button>
            </div>
        </div>
        <div class="row">
            <div class="col-11 p-2">
                <div class="row">
                    <div class="col-4">
                        <div v-if="studentInput.length">
                            <table class="table table-hover">
                                <tbody v-for="student in studentSearchList">
                                    <tr>
                                        <td @click="selectStudent(student.studentName)">{{ student.studentName }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="col-4">
                        <div v-if="courseInput.length">
                            <table class="table table-hover">
                                <tbody v-for="course in courseSearchList">
                                    <tr>
                                        <td @click="selectCourse(course.courseName, course.courseID)">{{ course.courseName }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="col-4">
                    </div>
                </div>
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        // Initialise URLs
        var getCoursesURL = "http://localhost:2222/courses"
        var getStudentsURL = "http://localhost:2222/students"
        var getCourseClassListURL = "http://localhost:2222/classList/"

        // Get Course Details
        var assignment = new Vue({
            el: '#assignment',
            data: {
                courses: [],
                courseInput: "",
                selectedCourse: "",
                courseSearchList: [],

                students: [],
                studentInput: "",
                selectedStudent: "",
                studentSearchList: [],

                classes: []
            },
            created: function() {
                // Get Courses
                fetch(getCoursesURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.courses;

                        for (record of result) {
                            this.courses.push(record);
                        }
                    })

                // Get Students
                fetch(getStudentsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.students;

                        for (record of result) {
                            this.students.push(record);
                        }
                    })
            },
            methods: {
                searchCourse: function() {
                    this.courseSearchList = [];
                    this.classes = [];

                    if (this.courseInput == "") {
                        this.courseSearchList.push(this.courses)
                        return
                    } else {
                        for (course of this.courses) {
                            if (course.courseName.toLowerCase().includes(this.courseInput)) {
                                this.courseSearchList.push(course)
                            }
                        }
                    }
                },
                selectCourse: function(courseName, courseID) {
                    this.courseInput = courseName
                    this.courseSearchList = [];

                    this.classes = [];
                    // Get Selected Course Classes
                    fetch(getCourseClassListURL + courseID)
                        .then(response => response.json())
                        .then(data => {
                            result = data.data.classes;

                            for (record of result) {
                                this.classes.push(record);
                            }
                        })
                },

                searchStudent: function() {
                    this.studentSearchList = [];
                    if (this.studentInput == "") {
                        return
                    } else {
                        for (student of this.students) {
                            if (student.studentName.toLowerCase().includes(this.studentInput)) {
                                this.studentSearchList.push(student)
                            }
                        }
                    }
                },
                selectStudent: function(studentName) {
                    this.studentInput = studentName
                    this.studentSearchList = [];
                },
                forceAssign: function() {
                    alert("clicked")
                    let jsonData = JSON.stringify({
                        "regStudentID": this.selectedStudent,
                        "regCourseID": this.selectedCourse,
                        "regClassID": document.getElementById("classDropdown").value,
                        "regStatus": "accepted"
                    });
                    fetch(assignURL, {
                            method: "POST",
                            headers: {
                                "Content-type": "application/json"
                            },
                            body: jsonData
                        })
                        .then(response => response.json())
                        .then(data => {
                            result = data;
                            console.log(result)
                        })

                }
            }
        })
    </script>
</body>

</html>