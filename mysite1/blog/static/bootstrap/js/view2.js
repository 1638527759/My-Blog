$(document).ready(function() {
    // 登陆
    $(".up").click(function() {
        var fromdata_up = new FromData();
        fromdata_up.append("user", $("#up_user"));
        fromdata_up.append("password", $("#up_passwords"));
    });

    // 注册
    // $("in").click(function(){
    //     var fromdata_in = new FromData();
    //     fromdata_in.append("")
    // });
    $.ajax({
        url: "",
        type: "post",
        async: true,
        contentType: false,
        processData: false,
        data: fromdata_up,
        success: function(data) {
            console.log(data);
        }
    })
});


// var pull_signin = document.querySelector(".in");
// var pull_signup = document.querySelector(".up");
// var window_face = document.querySelector(".window_face");
// var window_back = document.querySelector(".window_back");

// function rotate_face() {
//     window_face.style.animationName = "rotate_back";
//     window_back.style.animationName = "rotate_face";
//     a1 = setInterval(close, 600);
// }

// function close() {
//     window_face.style.display = "none";
//     window_back.style.display = "block";
//     // pull_signin.style.display = "none";
//     // pull_signup.style.display = "block";
//     clearInterval(a1);
// }

// pull_signup.addEventListener("click", rotate_face);

// function rotate_back() {
//     window_face.style.animationName = "rotate_face";
//     window_back.style.animationName = "rotate_back";
//     a2 = setInterval(poen, 700);
// }

// function poen() {
//     window_face.style.display = "block";
//     window_back.style.display = "none";
//     // pull_signin.style.display = "block";
//     // pull_signup.style.display = "none";
//     clearInterval(a2);
// }

// pull_signin.addEventListener("click", rotate_back);