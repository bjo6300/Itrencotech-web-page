var check = function () {
    const pw1 = document.getElementById('input-showed-01').value;
    const pw2 = document.getElementById('input-showed-02').value;
    if (pw1 === pw2 && pw1 !== '' && pw2 !== '') {
        document.getElementById('span-confirm-message').style.color = 'green';
        document.getElementById('span-confirm-message').innerHTML = '✔ 비밀번호가 일치합니다.';
        document.getElementById('btn-confirm-02').disabled = false;
    } else {
        document.getElementById('span-confirm-message').style.color = 'red';
        document.getElementById('span-confirm-message').innerHTML = '✘ 비밀번호가 일치하지 않습니다.';
        document.getElementById('btn-confirm-02').disabled = true;
    }
};