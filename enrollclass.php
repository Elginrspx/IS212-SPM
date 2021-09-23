<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
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
    <div class="container">
        <div class="row p-3">
            <a href="home.php">Courses&nbsp;>&nbsp;</a>
            <a href="course.php">3D Printing and Additive Manufacturing&nbsp;>&nbsp;</a>
            <a href="#">Registration&nbsp;>&nbsp;</a>
            <a href="class.php">Choose your preferred class&nbsp;>&nbsp;</a>
            <a href="#" class="current">Enrollment Application Confirmation</a>
        </div>
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
                        <h5 class="card-title color-orange">Choice: Class 1</h5>
                        <p class="card-text">Start Date: 1 November 2021<br>End Date: 28 November 2021</p>
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
        console.log(courseID);
        alert("meep");

        var registrationURL = "http://localhost:2222/registerClass" 

        var enrollment = new Vue({
            el: '#enrollment',
            data: {
                isSubmit: false,
                courseID: courseID,
                classID: classID,
                studentID: studentID
            },
            methods: {
                submitApplication: function() {
                    alert("insubmit")
                    let jsonData = JSON.stringify({
                        "regStudentID": studentID,
                        "regCourseID": courseID,
                        "regClassID": classID,
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
                        result = data;
                        console.log(result);
                        this.isSubmit = true;
                    })
                    
                }
            }
        })
    </script>
</body>

</html>