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
    <div id="course" class="container">
        <div class="row p-3">
            <a href="home.php">Courses&nbsp;>&nbsp;</a>
            <a href="#" class="current">{{ courseName }}</a>
        </div>
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
                            <h1 class="title">{{ courseName }}</h1>
                            <div style="position:absolute; bottom:0;">
                                <a href="class.php" class="btn btn-default btn-md active" role="button" aria-pressed="true">
                                    Enroll Here
                                </a>
                                <p class="color-orange m-0">Registration Period:<br>13 September 2021 - 17 October 2021</p>
                            </div>

                        </div>
                        <div class="col-lg-6 p-1">
                            <img src="images/sample.png" style="width:100%">
                        </div>
                    </div>
                </div>
                <h1 class="my-3 text-center title">Course Description</h1>
                <p class="color-darkgrey">{{ courseDescription }}</p>
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        var cCID = localStorage.getItem("chosenCourse");

        var getCourseDetailsURL = "http://localhost:2222/courses/" + cCID
        //var getCourseSectionsURL = "http://localhost:2222/courses/10"

        var course = new Vue({
            el: '#course',
            data: {
                courseName: "",
                courseDescription: ""
                //sections: []

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

                /*
                // Get Course Sections
                fetch(getCourseSectionsURL)
                    .then(response => response.json())
                    .then(data => {
                        result = data.data.course;

                        for (record in result) {
                            // rmb to replace sectionName with whatever u called it
                            // get it to return sectionNo and sectionName
                            this.sections.push(record)
                        }
                    })
                    */
            }
        })
    </script>
</body>

</html>