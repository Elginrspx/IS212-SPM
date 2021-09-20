<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div id="course">
        <div class="container">
            <nav class="mt-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="home.php">Courses</a></li>
                    <li class="breadcrumb-item"><a href="#">{{ courseName }}</a></li>
                    <li class="breadcrumb-item"><a href="#">Registration</a></li>
                    <li class="breadcrumb-item"><a href="#" class="current">Choose your preferred class</a></li>
                </ol>
            </nav>
        </div>
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
                <p class="title text-center pt-5">Choose your preferred class</p>
            </div>
        </div>
        <div id="courseClassList" class="row">
            <class-list v-for="classitem in classes" v-bind:classitem="classitem" v-bind:key="classitem.classID"></class-list>
        </div>
    </div>


    <?php include 'includes/footer.php' ?>
    <script>
        var courseID = localStorage.getItem("chosenCourse");

        // Initialise URLs
        var getCourseDetailsURL = "http://localhost:2222/courses/" + courseID
        var getCourseClassListURL = "http://localhost:2222/classList/" + courseID

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

        var courseClassList = new Vue({
            el: '#courseClassList',
            data: {
                classes: []
            },
            created: function() {
                // Get Course Class List
                fetch(getCourseClassListURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.classes;

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
                        <div class="d-flex align-items-end justify-content-between">
                            <a href="#" @click="selectClass($event, classitem.classID)" class="btn btn-default btn-md active" role="button" aria-pressed="true">View</a>
                            <p class="mb-0 registrationText">Registration period:<br>{{ classitem.regPeriod }}</p>
                        </div>
                    </div>
                </div>
            </div>
            `,
            methods: {
                selectClass: function(e, classID) {
                    e.preventDefault();
                    localStorage.setItem("chosenClass", classID);
                    window.location.replace("class.php");
                }
            }
        })
    </script>
</body>

</html>