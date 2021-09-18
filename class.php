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
            <a href="#" class="current">Choose your preferred class</a>
        </div>
        <div class="row">
            <div class="col">
                <p class="title text-center">Choose your preferred class</p>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/class.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">Class 1</h5>
                        <p class="card-text">Start Date: 1 November 2021<br>End Date: 28 November 2021</p>
                        <a href="enrollclass.php" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/class.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">Class 2</h5>
                        <p class="card-text">Start Date: 1 November 2021<br>End Date: 28 November 2021</p>
                        <a href="enrollclass.php" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/class.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">Class 3</h5>
                        <p class="card-text">Start Date: 1 November 2021<br>End Date: 28 November 2021</p>
                        <a href="enrollclass.php" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 col-sm-12 py-1 my-1">
                <div class="card shadow h-100">
                    <img class="card-img-top" src="images/class.png">
                    <div class="card-body">
                        <h5 class="card-title color-orange">Class 4</h5>
                        <p class="card-text">Start Date: 1 November 2021<br>End Date: 28 November 2021</p>
                        <a href="enrollclass.php" class="btn btn-default btn-md active" role="button" aria-pressed="true">Enroll</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <?php include 'includes/footer.php' ?>
</body>

</html>