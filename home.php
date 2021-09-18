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
        // initialise urls
        var getCourseURL = "http://localhost:2222/courses"
        var getPrereqsURL = "http://localhost:2222/prereqs"
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
                        <div v-if="course.status == 'Course Completed'">
                            <p class="card-text courseStatus1">Course Completed</p>
                        </div>
                        <div v-else-if="course.status == 'Pre-requisites NOT met'">
                            <p class="card-text courseStatus2 mb-0">Pre-requisites NOT met:</p>
                            <p v-for="prereqCourse in course.prerequisites" class="card-text courseStatus2 m-0">{{ prereqCourse }}</p>
                        </div>
                    </div>
                    <div class="card-footer">
                        <a href="#" class="btn btn-default btn-md active" role="button" aria-pressed="true">View Course</a>
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
                }
            }
            
        })

        var course = new Vue({
            el: '#course',
            data: {
                courses: [],
                trigger: 0
            },
            methods: {
                
                getCourseCardInfo: function() {
                    alert("in")
                    const response =
                        fetch(getCourseURL)
                        .then(response => response.json())
                        .then(data => {
                            // console.log(data);
                            if (data.code === 404) {
                                // alert("oops")
                                // none returned
                                // alert(data.message);
                            } else {
                                // alert("meep");
                                for (var c in data.data.courses) {
                                    id = data.data.courses[c].courseID;
                                    this.courses[id.toString()] = {
                                        'id':id,
                                        'name':data.data.courses[c].courseName,
                                        'prereqs':[]
                                    }
                                    fetch(getPrereqsURL+ `/${id}`)
                                    .then(response => response.json())
                                    .then(data => {
                                        console.log(id)
                                        // console.log(data)
                                        if (data.code === 404) {
                                            alert("oops")
                                            // none returned
                                            // alert(data.message);
                                        } else {
                                            console.log(data)
                                            for (var i in data.data.courses){
                                                console.log(data.data.courses[i].prereqName);
                                                this.courses[data.data.courses[i].prereqCourseID].prereqs.push(data.data.courses[i].prereqName)
                                            }
                                            
                                        }
                                    })
                                }
                            }
                        })
                        .catch(error => {
                            // Errors when calling the service; such as network error, 
                            // service offline, etc
                            console.log(this.message + error);
                        });
                }
            },
            created: function () {
                // on Vue instance created, load the course list
                this.getCourseCardInfo();
                this.getPrereqs();
            },
            computed: {
                // getPrereqs: function() {
                //     alert("out")
                //     heh = this.courses
                //     console.log(heh[2])
                //     console.log(typeof(heh))
                //     for (var id in heh){
                //         alert("whee")
                //         console.log(id)
                //         fetch(getPrereqsURL+ `/${id}`)
                //         .then(response => response.json())
                //         .then(data => {
                //             console.log(id)
                //             // console.log(data)
                //             if (data.code === 404) {
                //                 alert("oops")
                //                 // none returned
                //                 // alert(data.message);
                //             } else {
                //                 console.log(data)
                //                 for (var i in data.data.courses){
                //                     console.log(data.data.courses[i].prereqName);
                //                     this.courses[id].prereqs.push(data.data.courses[i].prereqName)
                //                 }
                                
                //             }
                //         })
                //     }
                // }
            }
        })
    </script>
</body>



</html>


<!--  prev setup
// {
                    //     id: 0,
                    //     title: '3D Printing and Additive Manufacturing',
                    //     status: 'Pre-requisites Met',
                    //     prerequisites: ["Intro to 3D Printing", "Intro to 3D Printing 2"]
                    // },
                    // {
                    //     id: 1,
                    //     title: '3D Printing Hardware',
                    //     status: 'Course Completed',
                    //     prerequisites: ["Intro to 3D Printing", "Intro to 3D Printing 2"]
                    // },
                    // {
                    //     id: 2,
                    //     title: '3D Printing Software',
                    //     status: 'Pre-requisites NOT met',
                    //     prerequisites: ["Intro to 3D Printing", "Intro to 3D Printing 2"]
                    // },
                    // {
                    //     id: 2,
                    //     title: '3D Engineering Solution',
                    //     status: 'Pre-requisites Met',
                    //     prerequisites: []
                    // } -->
