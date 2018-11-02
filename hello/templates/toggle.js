function myFunction(to_toggle) {
  var x = document.getElementById(to_toggle);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
