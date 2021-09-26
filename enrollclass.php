<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>

    <div class="container">
        <nav id="course" class="mt-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="home.php">Courses</a></li>
                <li class="breadcrumb-item"><a href="course.php">{{ courseName }}</a></li>
                <li class="breadcrumb-item"><a href="course.php">Choose your preferred class</a></li>
                <li class="breadcrumb-item"><a href="#" class="current">Enrollment Application Confirmation</a></li>
            </ol>
        </nav>
        <div class="row">
            <div class="col">
                <p class="title text-center">Enrollment Application Confirmation</p>
            </div>
        </div>
        <div id="enrollment" class="row">
            <div class="col-12">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/class.png" style="object-fit: cover; height: 250px;">
                    <div v-if="!isSubmit" class="card-body text-center">
                        <h5 class="card-title color-orange">Choice: Class {{ classDetail[0].classID }}</h5>
                        <p class="card-text">Start Date: {{ classDetail[0].clsStartTime }}<br>End Date: {{ classDetail[0].clsEndTime }}</p>
                        <button @click="submitApplication" class="btn btn-default" type="button">
                            Submit Application
                        </button>
                        <br>
                        <a href="class.php">Back</a>
                    </div>
                    <div v-else class="card-body text-center">
                        <img src="images/check.svg" style="height: 30px;">
                        <h5 class="card-title color-orange">Your application has been successfully submitted!<br>
                            A confirmation email will be sent to you shortly.
                        </h5>
                        <a href="home.php" class="btn btn-default btn-md active m-2" role="button" aria-pressed="true">Back to Home Page</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>

    <script>
        var courseID = localStorage.getItem("chosenCourse");
        var classID = localStorage.getItem("chosenClass");
        var studentID = localStorage.getItem("userID");

        // Initialise URLs
        var getCourseDetailsURL = "http://localhost:2222/courses/" + courseID
        var getClassDetailsURL = "http://localhost:2222/classes/" + courseID + "/" + classID
        var registrationURL = "http://localhost:2222/registerClass"

        var course = new Vue({
            el: '#course',
            data: {
                courseName: ""
            },
            created: function() {
                // Get Course Details
                fetch(getCourseDetailsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.course;

                        this.courseName = result.courseName;
                    })
            }
        })

        var enrollment = new Vue({
            el: '#enrollment',
            data: {
                isSubmit: false,
                studentID: studentID,
                classDetail: []
            },
            created: function() {
                // Get Class Details
                fetch(getClassDetailsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.class;

                        this.classDetail.push(result)
                    })
            },
            methods: {
                submitApplication: function() {
                    let jsonData = JSON.stringify({
                        "regStudentID": studentID,
                        "regCourseID": this.classDetail[0].clsCourseID,
                        "regClassID": this.classDetail[0].classID,
                        "regStatus": "enrolled"
                    });
                    fetch(registrationURL, {
                            method: "POST",
                            headers: {
                                "Content-type": "application/json"
                            },
                            body: jsonData
                        })
                        .then(response => response.json())
                        .then(data => {
                            this.isSubmit = true;
                        })
                }
            }
        })
    </script>
</body>

</html>