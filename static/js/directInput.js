// 아이디, 비밀번호 찾기 - 이메일 입력받는 기능


function selectEmail(ele) {
    var $ele = $(ele);
    var $email2 = $('input[name=email2]');

    // '1'인 경우 직접입력 
    if ($ele.val() == "1") {
        $email2.attr('readonly', false);
        $email2.val('');
        
    } else {
        $email2.attr('readonly', true);
        $email2.val($ele.val());
    }
}