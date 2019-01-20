<!DOCTYPE html>
<html>

<head>
    <title>Try It!</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <script src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function (e) {
            $('#upload').on('click', function () {
                var form_data = new FormData();
                var ins = document.getElementById('multiFiles').files.length;
                for (var x = 0; x < ins; x++) {
                    form_data.append("files[]", document.getElementById('multiFiles').files[x]);
                }
                $.ajax({
                    url: 'uploads.php', // point to server-side PHP script 
                    dataType: 'text', // what to expect back from the PHP script
                    cache: false,
                    contentType: false,
                    processData: false,
                    data: form_data,
                    type: 'post',
                    success: function (response) {
                        $('#msg').html(response); // display success response from the PHP script
                    },
                    error: function (response) {
                        $('#msg').html(response); // display error response from the PHP script
                    }
                });
            });
        });
    </script>
</head>

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

    <!-- Page Text-->
    <div class="container text-center my-auto">
        <h1 class="mb-1">Resume Parser</h1>
        <h3 class="mb-5">
            <em>Select a group of resumes to be<br/> reviewed and ranked!</em>
        </h3>
    </div>
    <!-- Page Text-->

    <!-- App Buttons -->
    <div style="width:400px;">

        <!-- Browse -->
        <label class="btn btn-primary"style="margin-left: 675px">Browse...
            <input type="file" id="multiFiles" name="files[]" multiple="multiple"/>
        </label>
        
        
        <!-- Upload -->
        <label>
            <button id="upload" class="btn btn-primary"style="margin-left: 685px">Upload</button>
        </label>

        <!-- Parse -->
        <form action="render.php">
            <button class="btn btn-primary" style="margin-left: 690px;">Parse!</button>
        </form>
        
    </div>
    <p id="msg"></p>
    <!-- App Buttons -->

</body>

</html>