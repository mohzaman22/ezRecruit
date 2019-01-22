<!DOCTYPE html>
<html>

<head>
    <title>Results</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1 user-scalable=no">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>
</head>

<style>
    #rcorners2 {
        border-radius: 25px;
        background-color: #007bff;
        padding: 20px;
        color: white;
        width: 700px;
        height: 170px;
        margin: 0px auto;
    }
    a {
        color: white;
    }
</style>

<!-- Navbar -->
<nav class="navbar navbar-expand-md navbar-light bg-light sticky-top">
    <div class="container-fluid">
        <a class="navbar-brand" href="index.html"><img src="img/res.png"></a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
                        aria-haspopup="true" aria-expanded="false">Menu</a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="index.html">Home</a>
                        <a class="dropdown-item" href="app.php">Resume Parser</a>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</nav>
<!-- Navbar -->

<body>

    <!-- Page header text-->
    <div class="container text-center my-auto">
        <h1 class="mb-1">Here are your results!</h1>
    </div>
    <!-- Page header text-->

    <!-- All results -->
    <div>
        <p style="text-align:center">
            <?php
                $command = escapeshellcmd('/Users/donnelldebnam/Documents/GitHub/ezRecruit/parse.py');
                $output = shell_exec($command);
                echo $output;
            ?>
        </p>
    </div>
    <!-- All results -->
    
</body>

</html>