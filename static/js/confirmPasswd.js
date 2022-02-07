var check = function() {
    if (document.getElementById('input-showed-01').value ==
        document.getElementById('input-showed-02').value) {
        document.getElementById('span-confirm-message').style.color = 'green';
        document.getElementById('span-confirm-message').innerHTML = '✔ 비밀번호가 일치합니다.';
        document.getElementById('btn-confirm-02').disabled = false;
    } else {
        document.getElementById('span-confirm-message').style.color = 'red';
        document.getElementById('span-confirm-message').innerHTML = '✘ 비밀번호가 일치하지 않습니다.';
        document.getElementById('btn-confirm-02').disabled = true;
    }
}