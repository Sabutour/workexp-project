var submitted;

function submit_user_id_form() {
  if (submitted == null) {
    document.getElementById("user_id_number_form").submit();
    var submitted = 1;
    alert("Hi");
  }
}
