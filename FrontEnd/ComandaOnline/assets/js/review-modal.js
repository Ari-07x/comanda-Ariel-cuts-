


//Cambiar de color del me gusta o no me gusta

function like(){
  document.getElementById("like").classList.remove("no-selected")
  document.getElementById("like").classList.add("selected")

  document.getElementById("dislike").classList.add("no-selected")
  document.getElementById("dislike").classList.remove("selected")
}

document.getElementById("like").onclick = function(){
  like();
}

function dislike(){
  document.getElementById("dislike").classList.remove("no-selected")
  document.getElementById("dislike").classList.add("selected")

  document.getElementById("like").classList.remove("selected")
  document.getElementById("like").classList.add("no-selected")

}

document.getElementById("dislike").onclick = function(){
  dislike();
}

