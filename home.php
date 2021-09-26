<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Home | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div class="container-fluid p-0">
        <div class="jumbotron jumbotron-fluid home-jumbotron text-shadow" style="background-image:url(images/cover.jpg)">
            <h1 class="display-4">STAY AHEAD OF THE GAME<br>UPSKILL YOURSELF TODAY</h1>
        </div>
    </div>
    <div class="container">
        <div class="row m-3">
            <h2>All Courses</h2>
        </div>
        <div id="course" class="row">
            <course-list v-for="course in courses" v-bind:course="course" v-bind:key="course.courseID"></course-list>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        localStorage.setItem("userID", 1)
        
        // Initialise URLs
        var getCoursesURL = "http://localhost:2222/courses"
        var getPrereqsURL = "http://localhost:2222/prereqs"
        var getStudentCompletedUrl = "http://localhost:2222/completed/1"

        // Get Course Details
        var course = new Vue({
            el: '#course',
            data: {
                completedCourses: [],
                courses: []
            },
            created: function() {
                // Get Student's Completed Courses
                fetch(getStudentCompletedUrl)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.courses;
                        for (record of result) {
                            this.completedCourses.push(record.completedCName)
                        }
                    })

                // Get Courses
                fetch(getCoursesURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.courses;
                        for (record of result) {
                            courseID = record.courseID
                            record.prereqsNotMet = []

                            record.status = false
                            if (this.completedCourses.includes(record.courseName)) {
                                record.status = true;
                            }
                            this.courses.push(record);

                            /* If Course is not Completed and Course have prerequisites,
                                Get Course Prerequisites */
                            if (!record.status && record.have) {
                                fetch(getPrereqsURL + `/${courseID}`)
                                    .then(response => response.json())
                                    .then(data => {
                                        result = data.data.courses;
                                        for (record of result) {
                                            
                                            if (!this.completedCourses.includes(record.prereqName)) {
                                                this.courses[record.prereqCourseID].prereqsNotMet.push(record.prereqName)
                                            }
                                        }
                                    })
                            }
                        }
                    })
            }
        })

        Vue.component('course-list', {
            props: ['course'],
            template: `
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/sample.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">{{ course.courseName }}</h5>
                        <div v-if="course.status">
                            <p class="card-text courseStatus1">Course Completed</p>
                        </div>
                        <div v-else>
                            <div v-if="course.prereqsNotMet.length != 0">
                                <p class="card-text courseStatus2 mb-0">Pre-requisites NOT met:</p>
                                <p v-for="prereqCourse in course.prereqsNotMet" class="card-text courseStatus2 m-0">{{ prereqCourse }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer">
                        <a href="#" @click="selectCourse($event, course.courseID)" class="btn btn-default btn-md active" role="button" aria-pressed="true">View Course</a>
                    </div>
                </div>
            </div>
            `,
            methods: {
                selectCourse: function(e, courseID) {
                    e.preventDefault();
                    localStorage.setItem("chosenCourse", courseID);
                    window.location.replace("course.php");
                }
            }
        })
    </script>
</body>

</html>