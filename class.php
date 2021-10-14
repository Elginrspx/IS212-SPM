<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div id="classDetail" class="container">
        <nav class="mt-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="home.php">Courses</a></li>
                <li class="breadcrumb-item"><a href="course.php">{{ courseName }}</a></li>
                <li class="breadcrumb-item"><a href="course.php">Choose your preferred class</a></li>
                <li class="breadcrumb-item"><a href="#" class="current">Registration</a></li>
            </ol>
        </nav>
        <div class="row">
            <div class="col-4">
                <div class="timelineWrapper">
                    <h1 class="color-darkgrey">Courses</h1>
                    <h1>{{ courseName }}</h1>
                    <ul class="sessions">
                        <li class="select">
                            <div class="color-darkgrey">Chapter 1</div>
                            <p>3D Printing and Additive Manufacturing</p>
                        </li>
                        <li>
                            <div class="color-darkgrey">Chapter 2</div>
                            <p>3D Printing Hardware</p>
                        </li>
                        <li>
                            <div class="color-darkgrey">Chapter 3</div>
                            <p>3D Printing Software</p>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="col-8">
                <div style="border: 1px solid #dedede; border-radius: 10px;">
                    <div class="row p-3">
                        <div class="col-lg-6">
                            <div class="d-flex align-items-start flex-column" style="height:175px">
                                <div class="mb-auto p-2 bd-highlight">
                                    <h1 class="title mb-auto">Class {{ classDetails[0].classID }}</h1>
                                </div>
                                <div>
                                    <a href="enrollclass.php" @click="enrollClass($event, classDetails[0].clsCourseID, classDetails[0].classID)" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll Here</a>
                                </div>
                                <div>
                                    <p class="color-orange m-0">Registration Period:<br>{{ classDetails[0].regPeriod }}</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6 p-1">
                            <img src="images/class.png" style="width:100%">
                        </div>
                    </div>
                </div>
                <h1 class="my-3 text-center title">Course Description</h1>
                <!-- <p class="color-darkgrey"></p> -->
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        var courseID = localStorage.getItem("chosenCourse");
        var classID = localStorage.getItem("chosenClass");
        var loginID = localStorage.getItem("userID");

        var getCourseDetailsURL = "http://localhost:2222/courses/" + courseID;
        var getClassDetailsURL = "http://localhost:2222/classes/" + courseID + "/" + classID;
        // var registrationURL = "http://localhost:2222/registerClass";

        var classDetail = new Vue({
            el: '#classDetail',
            data: {
                courseName: "",
                classDetails: []
            },
            created: function() {
                // Get Course Details
                fetch(getCourseDetailsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.course;

                        this.courseName = result.courseName;
                    })

                // Get Class Details
                fetch(getClassDetailsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.class;

                        this.classDetails.push(result)
                    })
            },
            methods: {
                enrollClass: function(e, courseID, classID) {
                    e.preventDefault();
                    window.location.replace("enrollclass.php");
                }
            }
        })
    </script>
</body>

</html>