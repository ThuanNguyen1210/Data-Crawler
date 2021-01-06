<!DOCTYPE html>
<html>

<head>
    <title>New Jobs</title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/animate.css">
    <link rel="stylesheet" type="text/css" href="css/header_icon.css">
    <link rel="stylesheet" type="text/css" href="css/home.css">
    <link rel="icon" href="images/iconTitle.svg" type="image/svg">
    <style>
        .wow:first-child {
            visibility: hidden;
        }
    </style>
</head>

<body>

    <!-- Start Header  -->
    <header>
        <div class="container">
            <div class="logo">
                <a href="shoes_shop.php">New<span>!</span>Jobs</a>
            </div>
            <div class="nav">
                <ul>
                    <li><a href="home.php">Trang chủ</a></li>
                    <li><a href="newjob.html">Tin tuyển dụng</a></li>
                    <li><a href="description.html">Đăng tin</a></li>
                    
                </ul>
            </div>
            <div>
               
                <a href="login.php" class="user"><img src="../shoes_shop/images/icon/user.png" alt=""></a>
                
            </div>
           
        </div>
    </header>
    <!-- End Header  -->

    <!-- Start Home -->
    <section class="home wow flash" id="home">
        <div class="container">
            <h1 class="wow slideInLeft" data-wow-delay="1s">Upgrade <span>your job</span> with <span>us</span></h1>
            <h1 class="wow slideInRight" data-wow-delay="1s">Are you ready?</h1>
        </div>
        <!-- go down -->
        <a href="#about" class="go-down">
            <i class="fa fa-angle-down" aria-hidden="true"></i>
        </a>
        <!-- go down -->

    </section>
    <!-- End Home -->

    <!-- Start Hype News -->
    <section class="classes" id="classes">
        <div class="container">
            <div class="content">
                <div class="box img wow slideInLeft">
                    <img src="images/new4.jpg" alt="classes" />
                </div>
                <div class="box text wow slideInRight">
                    <h2>Hype news</h2>
                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type
                        specimen book. It has survived not only five centuries.</p>
                    <div class="class-items">
                        <div class="item wow bounceInUp">
                            <div class="item-img">
                                <img src="images/new1.jpg" alt="classes" />
                            </div>
                            <div class="item-text">
                                <h4>Stretching Training</h4>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                                <a href="">Get Details</a>
                            </div>
                        </div>
                        <div class="item wow bounceInUp">
                            <div class="item-text">
                                <h4>Stretching Training</h4>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                                <a href="">Get Details</a>
                            </div>
                            <div class="item-img">
                                <img src="images/new3.jpg" alt="classes" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Classes -->

    <!-- Start Clean your shoes -->
    <section class="start-today">
        <div class="container">
            <div class="content">
                <div class="box text wow slideInLeft">
                    <h2>Please apply here</h2>
                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type
                        specimen book. It has survived not only five centuries,</p>
                    <a href="" class="btn">Register Now</a>
                </div>
                <div class="box img wow slideInRight">
                    <img src="images/apply.jpg" alt="start today" />
                </div>

            </div>
        </div>
    </section>
    <!-- End Start Today -->

   


    <!-- Start Contact -->
    <section class="contact" id="contact">
        <div class="container">
            <div class="content">
                <div class="box form wow slideInLeft">
                    <form>
                        <input type="text" placeholder="Enter Name">
                        <input type="text" placeholder="Enter Email">
                        <input type="text" placeholder="Enter Mobile">
                        <textarea placeholder="Enter Message"></textarea>
                        <button type="submit">Send Message</button>
                    </form>
                </div>
                <div class="box text wow slideInRight">
                    <h2>Get Connected with us</h2>
                    <p class="title-p">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</p>
                    <div class="info">
                        <ul>
                            <li><span class="fa fa-map-marker"></span>KTX Khu A DHQG TP HCM, phuong Dong Hoa, thi xa Di An, tinh Binh Duong</li>
                            <li><span class="fa fa-phone"></span> 91 9999999999</li>
                            <li><span class="fa fa-envelope"></span> newjobs@gmail.com</li>
                        </ul>
                    </div>
                    <div class="social">
                        <a href=""><span class="fa fa-facebook"></span></a>
                        <a href=""><span class="fa fa-linkedin"></span></a>
                        <a href=""><span class="fa fa-skype"></span></a>
                        <a href=""><span class="fa fa-youtube-play"></span></a>
                    </div>

                </div>
            </div>
        </div>
    </section>
    <!-- End Contact -->



    <!-- jquery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script>
        $(document).ready(function() {

            $(".ham-burger, .nav ul li a").click(function() {

                $(".nav").toggleClass("open")

                $(".ham-burger").toggleClass("active");
            })
            $(".accordian-container").click(function() {
                $(".accordian-container").children(".body").slideUp();
                $(".accordian-container").removeClass("active")
                $(".accordian-container").children(".head").children("span").removeClass("fa-angle-down").addClass("fa-angle-up")
                $(this).children(".body").slideDown();
                $(this).addClass("active")
                $(this).children(".head").children("span").removeClass("fa-angle-up").addClass("fa-angle-down")
            })

            $(".nav ul li a, .go-down").click(function(event) {
                if (this.hash !== "") {

                    event.preventDefault();

                    var hash = this.hash;

                    $('html,body').animate({
                        scrollTop: $(hash).offset().top
                    }, 800, function() {
                        window.location.hash = hash;
                    });

                    // add active class in navigation
                    $(".nav ul li a").removeClass("active")
                    $(this).addClass("active")
                }
            })
        })
    </script>
    <script src="js/wow.min.js"></script>
    <script>
        wow = new WOW({
            animateClass: 'animated',
            offset: 0,
        });
        wow.init();
    </script>
</body>

</html>