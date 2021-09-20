<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body onload='getClasses()'>
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
    <div id="classes" class="container">
        <div class="row p-3">
            <a href="home.php">Courses&nbsp;>&nbsp;</a>
            <a href="course.php">3D Printing and Additive Manufacturing&nbsp;>&nbsp;</a>
            <a href="#">Registration&nbsp;>&nbsp;</a>
            <a href="#" class="current">Choose your preferred class</a>
        </div>
        <div class="row">
            <div class="col">
                <p class="title text-center">Choose your preferred class</p>
            </div>
        </div>
        <div class="row" id="cardContainer">
            
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        var cCID = localStorage.getItem("chosenCourse");
        var loginID = 1 //student ID but initialised for now cos no login


        var getClassesURL = "http://localhost:2222/classList/" + cCID
        //var getCourseSectionsURL = "http://localhost:2222/courses/10"
        window.onload = function(){
            fetch(getClassesURL)
            .then(response => response.json())
            .then(data => {
                classes = data.data.classes;
                for (classs in classes){
                    console.log(classes[classs].classID)
                    document.getElementById("cardContainer").innerHTML +=
                    `<div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                        <div class="card shadow h-100">
                            <img class="card-img-top" src="images/class.png">
                            <div class="card-body">
                                <h5 class="card-title color-orange">Class ${classes[classs].classID}</h5>
                                <p class="card-text">Start Date: ${classes[classs].clsStartTime}<br>End Date: ${classes[classs].clsEndTime}</p>
                                <a href="enrollclass.php" onclick="return prepareAssignment($event, ${classes[classs].clsCourseID},${classes[classs].classID}, ${loginID})" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a>
                            </div>
                        </div>
                    </div>`
                }
            })
        }
        function prepareAssignment(e, courseID,classID , studentID){
            e.preventDefault();
            localStorage.setItem("courseID", courseID);
            localStorage.setItem("classID", classID);
            localStorage.setItem("studentID", studentID)

            alert("check")
            // window.location.replace("enrollclass.php");
        }
        
    </script>
</body>

</html>