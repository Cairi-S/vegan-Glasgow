const password = document.querySelector("#password");
const confirmPassword = document.querySelector("#confirmPassword");
const formBtn = document.querySelector(".form-button");

formBtn.addEventListener("click", checkPasswords);

function checkPasswords() {
  if(password.value != confirmPassword.value){
      alert("Passwords must match");
      return false;
  }
  else if(password.value == confirmPassword.value){
      return true;
  }
}