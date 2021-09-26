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
                    <course-list ref="courseComponent" v-for="courseitem in courseList" v-bind:courseitem="courseitem" v-bind:classlist="classList" v-bind:key="courseitem.regCourseID"></course-list>
                </div>
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        // initialise urls
        var getRegistrationCoursesURL = "http://localhost:2222/registrationCourses"
        var getRegistrationURL = "http://localhost:2222/registration/"
        var getAssignRegistrationURL = "http://localhost:2222/assignRegistration"

        var classAccordion = new Vue({
            el: '#classAccordion',
            data: {
                courseList: [],
                classList: []
            },
            created: function() {
                fetch(getRegistrationCoursesURL)
                    .then(response => response.json())
                    .then(data => {
                        // Get Course List that has registrations
                        result = data.courseList;

                        for (record of result) {
                            this.courseList.push(record);
                        }
                    })
            }
        })

        Vue.component('course-list', {
            props: ['courseitem', 'classlist'],
            template: `
            <div class="accordion-item my-1">
                <h2 class="accordion-header" v-bind:id="'heading' + courseitem.regCourseID">
                    <button @click="selectCourse(courseitem.regCourseID)" class="accordion-button collapsed py-1" type="button" data-bs-toggle="collapse" v-bind:data-bs-target="'#collapse' + courseitem.regCourseID" aria-expanded="false" v-bind:aria-controls="'collapse' + courseitem.regCourseID">
                        {{ courseitem.courseName }}
                    </button>
                </h2>
                <div v-bind:id="'collapse' + courseitem.regCourseID" class="accordion-collapse collapse" v-bind:aria-labelledby="'heading' + courseitem.regCourseID" data-bs-parent="#classAccordion">
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
                                <class-list @reload="reloadCourse(courseitem.regCourseID)" v-for="classitem in classlist" v-bind:classitem="classitem" v-bind:key="classitem.classID"></class-list>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            `,
            methods: {
                selectCourse: function(courseID) {
                    classAccordion.classList = []

                    //Get Course Details
                    fetch(getRegistrationURL + courseID)
                        .then(response => response.json())
                        .then(data => {
                            result = data.data.registrations;

                            for (record of result) {
                                classAccordion.classList.push(record)
                            }
                        })
                },
                reloadCourse: function(courseID) {
                    this.selectCourse(courseID)
                }
            }
        })

        Vue.component('class-list', {
            props: ['classitem'],
            template: `
            <tr>
                <td>{{ classitem.studentName }}</td>
                <td>Class {{ classitem.regClassID }}</td>
                <td>{{ classitem.taken }} / {{ classitem.clsLimit }}</td>
                <td><a @click="assignStudent(classitem.studentID, classitem.regCourseID, classitem.regClassID)" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a></td>           
            </tr>
            `,
            methods: {
                assignStudent: function(studentID, courseID, classID) {
                    let jsonData = JSON.stringify({
                        "studentID": studentID,
                        "courseID": courseID,
                        "classID": classID,
                        "regStatus": "accepted"
                    });
                    fetch(getAssignRegistrationURL, {
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
                            this.$emit('reload')
                        })
                }
            }
        })
    </script>
</body>

</html>