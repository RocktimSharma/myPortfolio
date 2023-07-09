/* ----------------------------------For Index------------------------------------------------*/
$(".anim-line1").on("animationend", removeBorder);

function removeBorder() {
    console.log("working");
    $(".anim-line1").css('border', 'none');
}

$(".anim-line2").on("animationstart", showBorder);

function showBorder() {
    console.log("working");
    $(".anim-line2").css('border-right', '2px solid transparent');
}


$(".cursor").on("animationend", runClick);

function runClick() {
    $("#runButton").addClass('clicked')
    window.location.replace("/home");
}

$(document).ready(function () {

    /*---------------------------------------------- Tab Active ----------------------------------------------------*/

    var currentURL = window.location.href;


    if (currentURL.indexOf("/works") !== -1) {
        $('a[href="/works"]').addClass("active");
    } else if (currentURL.indexOf("/home#contact-sec") !== -1) {
        $('a[href="/home#contact-sec"]').addClass("active");
    } else if (currentURL.indexOf("/home#skill-sec") !== -1) {
        $('a[href="/home#skill-sec"]').addClass("active");
    } else {
        $('a[href="/home"]').addClass("active");
    }

    /*--------------------------------------------------Index Page ----------------------------------------------------*/
    // Get the current date and time
    var currentDate = new Date();

    var morningMessage = "Good Morning!";
    var afternoonMessage = "Good Afternoon!";
    var eveningMessage = "Good Evening!";

    // Format the current time in 12-hour format with AM/PM indicator
    var formattedTime = currentDate.toLocaleString('en-US', {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    });

    // Get the AM/PM indicator
    var amPm = currentDate.toLocaleString('en-US', {
        hour: 'numeric',
        hour12: true
    }).split(' ')[1];

    // Get the current date, day, and month
    var formattedDate = currentDate.toLocaleString('en-US', {
        weekday: 'long',
        month: 'long',
        day: 'numeric'
    });

    // Get the current day and month separately
    var day = currentDate.toLocaleString('en-US', {
        day: 'numeric'
    });
    var month = currentDate.toLocaleString('en-US', {
        month: 'long'
    });

    var weekDay = currentDate.toLocaleString('en-US', {
        weekday: 'long'
    });

    var timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

    // Display the appropriate greeting based on the current time
    if (currentDate.getHours() >= 0 && currentDate.getHours() < 12) {
        $('#greeting').text(morningMessage);
    } else if (currentDate.getHours() >= 12 && currentDate.getHours() < 17) {
        $('#greeting').text(afternoonMessage);
    } else {
        $('#greeting').text(eveningMessage);
    }

    // Display the formatted time with AM/PM indicator
    $('#current-time').text(formattedTime);
    $('#format').text(amPm)
    // Display the formatted date, day, and month
    $('#current-date').text(day);
    $('#current-day').text(weekDay);
    $('#current-month').text(month);
    $('#timezone').text(timezone);

    /* ----------------------------------Skill------------------------------------------------*/
    $(".progress").each(function () {
        var level = $(this).data("level");

        $(this).width(level)

    });

    /* ----------------------------------Scroll Animation------------------------------------------------*/
    const fadeElements = $('.fade-element');

    function handleScroll() {
        fadeElements.each(function () {
            const element = $(this);
            if (isElementInViewport(element)) {
                element.addClass('fade-in').removeClass('fade-out');
            } else {
                element.removeClass('fade-in').addClass('fade-out');
            }
        });
    }

    function isElementInViewport(element) {
        const rect = element[0].getBoundingClientRect();
        const windowHeight = window.innerHeight || document.documentElement.clientHeight;
        const elementHeight = rect.height;
        const threshold = windowHeight * 0.1; // 10% of window height

        return (
            rect.bottom >= threshold &&
            rect.top <= windowHeight - threshold
        );
    }


    handleScroll();

    $(window).scroll(handleScroll);
});

/* ----------------------------------Form Submit------------------------------------------------*/
$(document).ready(function () {
    // Prevent form submission on button click
    $('#contactForm').submit(function (event) {
        event.preventDefault();

        // Perform AJAX request to submit the form data
        $.ajax({
            type: 'POST',
            url: window.location.href,  // Use the current URL as the endpoint
            data: $(this).serialize(),
            success: function (response) {

            }
        });
    });
});




  


