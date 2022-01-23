/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
function onChange() {
  const password = document.querySelector("input[name=Password]");
  const confirm = document.querySelector("input[name=Confirm Password]");
  if (confirm.value === password.value) {
    confirm.setCustomValidity("");
  } else {
    confirm.setCustomValidity("Passwords do not match");
  }
}
