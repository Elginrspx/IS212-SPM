<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div id="course">
        <nav class="m-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="home.php">Courses</a></li>
                <li class="breadcrumb-item"><a href="#">{{ courseName }}</a></li>
                <li class="breadcrumb-item"><a href="#" class="current">Choose your preferred class</a></li>
            </ol>
        </nav>
        <div class="container-fluid p-0">
            <div class="jumbotron jumbotron-fluid course-jumbotron" style="background:linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(images/sample.png); background-size:cover;">
                <h1 class="display-4 text-shadow">{{ courseName }}</h1>
                <p>{{ courseDescription }}</p>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col">
                <p class="title text-center pt-5 m-0">Choose your preferred class</p>
                <p class="text-center color-orange">*All slots are subjected to availability</p>
            </div>
        </div>
        <div id="courseClassInfo" class="row">
            <class-list v-for="classitem in classes" v-bind:classitem="classitem" v-bind:key="classitem.classID"></class-list>
        </div>
    </div>


    <?php include 'includes/footer.php' ?>
    <script>
        var courseID = localStorage.getItem("chosenCourse");

        // Initialise URLs
        var getCourseDetailsURL = "http://localhost:2222/courses/" + courseID
        var getCourseClassInfoURL = "http://localhost:2222/classInfo/" + courseID

        var course = new Vue({
            el: '#course',
            data: {
                courseName: "",
                courseDescription: ""
            },
            created: function() {
                // Get Course Details
                fetch(getCourseDetailsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.course;

                        this.courseName = result.courseName;
                        this.courseDescription = result.cDescription;
                    })
            }
        })

        var courseClassInfo = new Vue({
            el: '#courseClassInfo',
            data: {
                classes: []
            },
            created: function() {
                // Get Course Class Info
                fetch(getCourseClassInfoURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.classInfo

                        for (record of result) {
                            this.classes.push(record)
                        }
                    })
            }
        })

        Vue.component('class-list', {
            props: ['classitem'],
            template: `
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/class.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">Class {{ classitem.classID }}</h5>
                        <p class="card-text">Start Date: {{ classitem.clsStartTime }}<br>End Date: {{ classitem.clsEndTime }}</p>
                        <p class="card-text">Trainer: {{ classitem.clsTrainer }}</p>
                        <div class="d-flex align-items-end justify-content-between">
                            <a v-if="classitem.noAccepted < classitem.clsLimit" href="#" @click="enrollClass($event, classitem.clsCourseID, classitem.classID)" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a>
                            <a v-else class="btn btn-disabled btn-md active" role="button" aria-pressed="true" disabled>Full</a>
                            <p class="mb-0 registrationText">Registration period:<br>{{ classitem.regPeriod }}</p>
                        </div>
                    </div>
                </div>
            </div>
            `,
            methods: {
                enrollClass: function(e, courseID, classID) {
                    e.preventDefault();
                    localStorage.setItem("chosenCourse", courseID);
                    localStorage.setItem("chosenClass", classID);
                    window.location.replace("enrollclass.php");
                }
            }
        })
    </script>
</body>

</html>