/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
function onChange() {
  const password = document.querySelector("input[name=password]");
  const confirm = document.querySelector("input[name=confirm]");
  if (confirm.value === password.value) {
    confirm.setCustomValidity("");
  } else {
    confirm.setCustomValidity("Passwords do not match");
  }
}
