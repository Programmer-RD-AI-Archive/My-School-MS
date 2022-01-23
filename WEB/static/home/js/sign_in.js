/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/
function onChange() {
  /**
   * Function to add two numbers
   * @param a The first number to add
   * @param b The second number to add
   * @returns The sum of two numbers
   */
  const password = document.querySelector("input[name=password]");
  const confirm = document.querySelector("input[name=confirm]");
  if (confirm.value === password.value) {
    confirm.setCustomValidity("");
  } else {
    confirm.setCustomValidity("Passwords do not match");
  }
}
