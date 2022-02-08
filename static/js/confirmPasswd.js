var check = function() {
    var pw1 = document.getElementById('input-showed-01').value;
    var pw2 = document.getElementById('input-showed-02').value

    //새 비밀번호, 비밀번호 확인 칸이 둘 다 공백이 아니면 -> 두 값이 일치하는지 확인
    if ((pw1 != '') && (pw2 != '')){
        // 일치
        if (pw1 == pw2) {
            document.getElementById('span-confirm-message').style.color = 'green';
            document.getElementById('span-confirm-message').innerHTML = '✔ 비밀번호가 일치합니다.';
            document.getElementById('btn-confirm-02').disabled = false;  // 확인 버튼 활성화
        }
        // 불일치
        else {
            document.getElementById('span-confirm-message').style.color = 'red';
            document.getElementById('span-confirm-message').innerHTML = '✘ 비밀번호가 일치하지 않습니다.';
            document.getElementById('btn-confirm-02').disabled = true;
        }
    }
    // 두 칸 중 하나가 공백이면
    else if (((pw1 != '') && (pw2 == '')) || ((pw1 == '') && (pw2 != ''))){
        document.getElementById('span-confirm-message').style.color = 'blue';
        document.getElementById('span-confirm-message').innerHTML = '※ 입력하지 않은 칸이 있습니다.';
        document.getElementById('btn-confirm-02').disabled = true;
    }
    // 두 칸 모두 공백이면
    else {
        document.getElementById('span-confirm-message').innerHTML = '';
        document.getElementById('btn-confirm-02').disabled = true;
    }
};