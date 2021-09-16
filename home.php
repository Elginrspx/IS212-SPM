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
            <course-list v-for="course in courses" v-bind:course="course" v-bind:key="course.id"></course-list>
        </div>
    </div>


    <?php include 'includes/footer.php' ?>
    <script>
        var navbar = new Vue({
            el: '#navbar',
            methods: {
                navbarSearch: function() {
                    /* Function to search..?*/
                }
            }
        })

        Vue.component('course-list', {
            props: ['course'],
            template: `
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/sample.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">{{ course.title }}</h5>
                    </div>
                    <div class="card-footer">
                        <p class="card-text" v-bind:class="statusClass(course.status)">{{ course.status }}</p>
                        <a href="#" class="btn btn-default btn-md active" role="button" aria-pressed="true">View Course</a>
                    </div>
                </div>
            </div>
            `,
            methods: {
                statusClass: function(status) {
                    if (status == "Pre-requisites Met") {
                        return "courseStatus1"
                    } else if (status == "Course Completed") {
                        return "courseStatus2"
                    } else {
                        return "courseStatus3"
                    }
                }
            }
        })

        var course = new Vue({
            el: '#course',
            data: {
                courses: [{
                        id: 0,
                        title: '3D Printing and Additive Manufacturing',
                        status: 'Pre-requisites Met'
                    },
                    {
                        id: 1,
                        title: '3D Printing Hardware',
                        status: 'Course Completed'
                    },
                    {
                        id: 2,
                        title: '3D Printing Software',
                        status: 'Pre-requisites NOT met'
                    }
                ]
            }
        })
    </script>
</body>

</html>