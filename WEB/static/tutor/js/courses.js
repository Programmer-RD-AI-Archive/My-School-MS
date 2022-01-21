/*
sumary_line

Keyword arguments:
argument -- description
Return: return_description
*/

var idx = 0;
var idx_iter = 0;
const idx_val = {};
function removeElement(idx) {
  const element = document.getElementById(`${idx}`);
  element.remove();
}
function add_to_content(val) {
  val = val.split(",");
  idx += 1;
  idx_val[idx] = val;
  document.getElementById("content").insertAdjacentHTML(
    "beforeend",
    `<div id="${idx}" class="${idx}" style="background-color:lightgray; padding:12.5px; margin:12.5px; border-radius: 25px">
        <h4>${val[0]}</h4>
        <p>${val[2]}</p>
        <button type="button" class="btn btn-outline-danger" onclick='removeElement("${idx}");'>Delete</button>
      </div>`
  );
}
function add_courses_API_button_submit(_id) {
  console.log(_id);
  const marks = document.getElementById("Marks Required to Pass").value;
  const image = document.getElementById("Image").value;
  const name = document.getElementById("Name").value;
  const description = document.getElementById("Description").value;
  const subject = document.getElementById("Subject").value;
  const info = {};
  for (idx_iter = 1; idx_iter <= idx; idx_iter++) {
    info[idx_iter] = [idx_val[idx_iter]];
  }

  $.ajax({
    type: "POST",
    url: `/Tutor/${_id}/Courses/Post/`,
    data: JSON.stringify({
      info: info,
      whole_content: $("#content").html(),
      marks: marks,
      image: image,
      name: name,
      description: description,
      subject: subject,
    }),
  });
  alert("Course Added");
  window.location.reload(0);
}
