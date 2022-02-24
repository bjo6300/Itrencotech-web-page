function alert_function() {
    var username = document.getElementById("username").value;
    var company_name = document.getElementById("company_name").value;
    var userid = document.getElementById("userid").value;
    var company_address = document.getElementById("company_address").value;
    var password1 = document.getElementById("input-showed").value;
    var company_tel = document.getElementById("company_tel").value;
    var phone_num = document.getElementById("phone_num").value;
    var email = document.getElementById("email").value;
    var password2 = document.getElementById("input-showed2").value;

    // 빈 칸 확인
    if (username.length + company_name.length + userid.length + company_address.length + password1.length + company_tel.length + phone_num.length + email.length + password2.length == 0) {
        alert('입력하지 않은 칸이 있습니다.');
    }
    // 아이디의 길이가 5자 미만이면
    else if (userid.length < 5) {
        alert('아이디가 5자 미만입니다.');
    }
    // 비밀번호 일치 여부 확인
    else if (password1 != password2) {
        alert('비밀번호가 일치하지 않습니다.');
    }

}
