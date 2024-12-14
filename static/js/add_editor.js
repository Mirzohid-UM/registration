function toggleEducationFields() {
    const educationLevel = document.getElementById("educationLevel").value;
    const higherEducation = document.getElementById("higherEducation");
    const secondarySchool = document.getElementById("secondarySchool");
    const schoolName = document.getElementById("school_name");
    const isStudying = document.getElementById("is_studying");
    const studyLevel = document.getElementById("study_level");
    const currentActivity = document.getElementById("current_activity");
    const formStatusMessage = document.getElementById("formStatusMessage");

    // Ma'lumot yuborilganini tekshirish
    if (formStatusMessage && formStatusMessage.style.display === "block") {
        formStatusMessage.innerText = "Siz bu ma'lumotlarni allaqachon topshirdingiz.";
        formStatusMessage.style.color = "red";
        return; // Agar ma'lumot yuborilgan bo'lsa, yana yubormaslik uchun chiqish
    }

    // Oliy ta'limni tanlasa
    if (educationLevel === "Oliy ta'lim") {
        if (higherEducation) higherEducation.style.display = "block";
        if (secondarySchool) secondarySchool.style.display = "none";
        if (schoolName) schoolName.removeAttribute("required");
        if (isStudying) isStudying.removeAttribute("required");
        if (studyLevel) studyLevel.removeAttribute("required");
        if (currentActivity) currentActivity.removeAttribute("required");

        if (higherEducation) {
            higherEducation.querySelectorAll("input").forEach(input => input.setAttribute("required", "true"));
        }
    }
    // O'rta ta'limni tanlasa
    else if (educationLevel === "O'rta ta'lim") {
        if (higherEducation) higherEducation.style.display = "none";
        if (secondarySchool) secondarySchool.style.display = "block";

        if (higherEducation) {
            higherEducation.querySelectorAll("input").forEach(input => input.removeAttribute("required"));
        }
        if (schoolName) schoolName.setAttribute("required", "true");
        if (isStudying) isStudying.setAttribute("required", "true");
        if (studyLevel) studyLevel.setAttribute("required", "true");
        if (currentActivity) currentActivity.setAttribute("required", "true");
    }
    // Hech narsa tanlanmasa
    else {
        if (higherEducation) higherEducation.style.display = "none";
        if (secondarySchool) secondarySchool.style.display = "none";

        if (higherEducation) {
            higherEducation.querySelectorAll("input").forEach(input => input.removeAttribute("required"));
        }
        if (secondarySchool) {
            secondarySchool.querySelectorAll("input").forEach(input => input.removeAttribute("required"));
        }
    }
}

function validateAndSubmitForm() {
    const form = document.getElementById("myForm");
    const formStatusMessage = document.getElementById("formStatusMessage");

    if (!form) return false; // Form mavjudligini tekshirish

    // Formani validatsiya qilish
    if (!form.checkValidity()) {
        if (formStatusMessage) {
            formStatusMessage.innerText = "Iltimos, barcha maydonlarni to'ldiring.";
            formStatusMessage.style.color = "red";
            formStatusMessage.style.display = "block";
        }
        return false;
    } else {
        if (formStatusMessage) {
            formStatusMessage.innerText = "Siz bu ma'lumotlarni allaqachon topshirdingiz.";
            formStatusMessage.style.color = "green";
            formStatusMessage.style.display = "block";
        }
        return true;
    }
}

(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // Initiate the wowjs
    new WOW().init();

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });

    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";

    $(window).on("load resize", function() {
        if (window.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
                function() {
                    const $this = $(this);
                    $this.addClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "true");
                    $this.find($dropdownMenu).addClass(showClass);
                },
                function() {
                    const $this = $(this);
                    $this.removeClass(showClass);
                    $this.find($dropdownToggle).attr("aria-expanded", "false");
                    $this.find($dropdownMenu).removeClass(showClass);
                }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Header carousel
    $(".header-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        items: 1,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ]
    });

    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav: false,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });

})(jQuery);
