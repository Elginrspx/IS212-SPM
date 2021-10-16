<!doctype html>
<html lang="en">

<head>
    <?php include 'includes/header.php' ?>
    <title>Trainer Class | LMS</title>
</head>

<body>
    <?php include 'includes/navbar.php' ?>
    <div class="container" id="trainerClass">
        <nav class="mt-2" style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item"><a href="#" class="current">My Classes</a></li>
            </ol>
        </nav>
        <div class="row">
            <div class="col">
                <p class="title">My Classes</p>
            </div>
        </div>
        <div class="row">
            <select class="form-select" id="classDropdown">
                <option selected>Select course...</option>
                <option value="1">3D Printing Test [Class 2]</option>
                <option value="2">3D Manufacturing Test [Class 3]</option>
                <option value="3">Introduction to Printing Test [Class 2]</option>
            </select>
        </div>
        <div class="row mt-5">
            <div class="col-4">
                <div class="timelineWrapper">
                    <h1 class="color-darkgrey">Courses</h1>
                    <h1>3D Printing Test</h1>
                    <ul class="sessions">
                        <li>
                            <div class="color-darkgrey">Chapter 1</div>
                            <p>3D Printing and Additive Manufacturing</p>
                        </li>
                        <li>
                            <div class="color-darkgrey">Chapter 2</div>
                            <p>3D Printing Hardware</p>
                        </li>
                        <li class="select">
                            <div class="color-darkgrey">Chapter 3</div>
                            <p>3D Printing Software</p>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="col-8">
                <div class="p-3" style="border: 1px solid #dedede; border-radius: 10px;">
                    <p style="font-size:1.5em;">Course Materials</p>
                    <hr>
                    <table class="table table-borderless table-sm">
                        <thead>
                            <tr>
                                <th style="width:7.5%"></th>
                                <th style="width:7.5%"></th>
                                <th style="width:77.5%"></th>
                                <th style="width:7.5%"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                                <td>Chapter_01_Introduction_to_3D_printing.pdf</td>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                            </tr>
                            <tr>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                                <td>Chapter_01_Introduction_to_3D_printing.mp4</td>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                            </tr>
                            <tr>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td> 
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                                <td>Chapter_01_Introduction_to_3D_printing</td>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td>
                            </tr>
                            <tr>
                                <td class="text-center"><img src="images/download.png" style="width:15px;height:15px;"></td> 
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="p-3 mt-4" style="border: 1px solid #dedede; border-radius: 10px;">
                    <p style="font-size:1.5em;">Quiz</p>
                    <hr>
                </div>
            </div>

        </div>
    </div>
    </div>
    <?php include 'includes/footer.php' ?>
    <script>
        /* FOR YINGHUI
        Need you to get me the data in the following format. You can take a look at Figma and see if you understand what I mean
        
        each -> will be one url call

        For Select Course dropdown:
        - Based on Trainer ID
          -> get CourseID, Course Name and Class ID (i.e. Class Number)

        - Based on Selected Course ID
          -> get Section Name (and Order?)
        
        - Based on Selected Section:
          -> get docType ("doc", "video", "link"), materialName?, isCompleted

        -> Function to add Section for selected Course
        -> Function to add material for selected Section of selected Course
        
        - Based on Selected Section
          -> get quiz name


        */
        // // Initialise URLs
        // var getClassesURL = "http://localhost:2222/classes/1/2"

        // // Get Class by Trainer
        // var trainerClass = new Vue({
        //     el: '#trainerClass',
        //     data: {
        //         classes: []
        //     },
        //     created: function() {
        //         // Get Courses
        //         fetch(getClassesURL)
        //             .then(response => response.json())
        //             .then(data => {
        //                 print(data)
        //                 // result = data.data.classes;

        //                 // for (record of result) {
        //                 //     this.classes.push(record);
        //                 // }
        //             })
        //     }
        // })
    </script>
</body>

</html>