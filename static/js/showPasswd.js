// 가려진 비밀번호 표시 기능


function showPasswd() {
    var x = document.getElementById("input-showed");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
}

function showPasswd01() {
  var x = document.getElementById("input-showed-01");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function showPasswd02() {
  var x = document.getElementById("input-showed-02");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}