<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Home | LMS</title>
</head>

<body>
    <div id="navbar">
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">
            </div>
            <div class="mx-auto order-0">
                <a class="navbar-brand mx-auto" href="#"><img src="images/All-In-One logo.png"></a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=".dual-collapse2">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
            <div class="navbar-collapse collapse w-100 order-3 dual-collapse2">
                <div class="d-flex flex-md-fill flex-shrink-1 justify-content-end order-3">
                    <form class="d-flex flex-nowrap align-items-center">
                        <div class="search-container pr-2">
                            <input class="form-control border-orange" type="search" placeholder="Search" aria-label="Search" />
                            <img @click="navbarSearch" src="images/search.svg" style="width:20px;" />
                        </div>
                    </form>
                    <button class="btn btn-default" type="button">
                        Login
                    </button>
                </div>
            </div>
        </nav>
    </div>
    <div class="container-fluid p-0">
        <div class="jumbotron jumbotron-fluid cover-text">
            <h1 class="display-4">STAY AHEAD OF THE GAME<br>UPSKILL YOURSELF TODAY</h1>
        </div>
    </div>

    <div class="container">
        <div class="row mb-3">
            <h2>All Courses</h2>
        </div>
        <div id="course" class="row">
            <course-list v-for="course in courses" v-bind:course="course" v-bind:key="course.courseID"></course-list>
        </div>
    </div>


    <?php include 'includes/footer.php' ?>
    <script>
        // initialise urls
        var getCourseURL = "http://localhost:2222/courses"
        var getPrereqsURL = "http://localhost:2222/prereqs"
        var getStudentCompletedUrl = "http://localhost:3333/completed/1"

        var navbar = new Vue({
            el: '#navbar',
            methods: {
                navbarSearch: function() {
                    /* Function to search..?*/
                }
            }
        })

        var course = new Vue({
            el: '#course',
            data: {
                completedCourses: [],
                courses: [],
                trigger: 0
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
                fetch(getCourseURL)
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
                                        for (record in result) {
                                            if (!this.completedCourses.includes(result[record].prereqName)) {
                                                this.courses[result[record].prereqCourseID].prereqsNotMet.push(result[record].prereqName)
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
                        <a href="#" @click="seeCourse($event, course.courseID)" class="btn btn-default btn-md active" role="button" aria-pressed="true">View Course</a>
                    </div>
                </div>
            </div>
            `,
            methods: {
                statusClass: function(status) {
                    if (status == "Course Completed") {
                        return "courseStatus1"
                    } else {
                        return "courseStatus2"
                    }
                },
                seeCourse: function(e, cID) {
                    e.preventDefault();
                    localStorage.setItem("chosenCourse", cID);
                    window.location.replace("course.php");
                }
            }

        })
    </script>
</body>

</html>