<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Course | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div class="container">
        <nav class="mt-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Admin</a></li>
                <li class="breadcrumb-item"><a href="adminCourseApplication.php" class="current">Course Registration</a></li>
            </ol>
        </nav>
        <div class="row">
            <div class="col">
                <p class="title">All Course Applications</p>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <div class="accordion" id="classAccordion">
                    <course-list v-for="courseitem in courses" v-bind:courseitem="courseitem" v-bind:classlist="classList" v-bind:key="courseitem.courseID"></course-list>
                </div>
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        // initialise urls
        var getCourseURL = "http://localhost:2222/courses"
        var getRegistrationInfo = "http://localhost:2222/registrations"

        var classAccordion = new Vue({
            el: '#classAccordion',
            data: {
                courses: [],
                classList: []
            },
            created: function() {
                // Get Courses
                fetch(getRegistrationInfo)
                    .then(response => response.json())
                    .then(data => {
                        result = data.courseList;

                        for (record of result) {
                            this.courses.push(record);
                        }
                    })
            }
        })

        Vue.component('course-list', {
            props: ['courseitem', 'classlist'],
            template: `
            <div class="accordion-item my-1">
                <h2 class="accordion-header" v-bind:id="'heading' + courseitem.courseID">
                    <button @click="selectCourse($event, courseitem.courseID)" class="accordion-button collapsed py-1" type="button" data-bs-toggle="collapse" v-bind:data-bs-target="'#collapse' + courseitem.courseID" aria-expanded="false" v-bind:aria-controls="'collapse' + courseitem.courseID">
                        {{ courseitem.courseName }}
                    </button>
                </h2>
                <div v-bind:id="'collapse' + courseitem.courseID" class="accordion-collapse collapse" v-bind:aria-labelledby="'heading' + courseitem.courseID" data-bs-parent="#classAccordion">
                    <div class="accordion-body">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th scope="col">Name</th>
                                    <th scope="col">Class Applied</th>
                                    <th scope="col">Class Vacancy</th>
                                    <th scope="col">Enroll</th>
                                </tr>
                            </thead>
                            <tbody>
                                <class-list v-for="classitem in classlist" v-bind:classitem="classitem" v-bind:key="classitem.classID"></class-list>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            `,
            methods: {
                selectCourse: function(e, courseID) {
                    e.preventDefault();

                    // Initialise URLs
                    var getCourseClassListURL = "http://localhost:2222/classList/" + courseID

                    //Get Course Details
                    fetch(getCourseClassListURL)
                        .then(response => response.json())
                        .then(data => {
                            result = data.data.classes;

                            classAccordion.classList = []

                            for (record of result) {
                                classAccordion.classList.push(record)
                            }
                        })
                },

                assignStudent: function() {
                    let jsonData = JSON.stringify({
                        "studentID": studentID,
                        "courseID": courseID,
                        "classID": classID,
                        "regStatus": "accepted"
                    });
                    fetch(registrationURL, {
                            method: "PUT",
                            headers: {
                                "Content-type": "application/json"
                            },
                            body: jsonData
                        })
                        .then(response => response.json())
                        .then(data => {
                            result = data;
                            console.log(result)
                        })
                    alert("check console to confirm it went through")
                    //refreshes page automatically
                    location.reload()
                }
            }
        })

        Vue.component('class-list', {
            props: ['classitem'],
            template: `
            <tr>
                <td>name??</td>
                <td>{{ classitem.classID }}</td>
                <td>{{ classitem.clsLimit }}</td>
                <td><a href="#" @click class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a></td>           
            </tr>
            `
        })
    </script>
</body>

</html>