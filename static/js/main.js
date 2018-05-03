//Scripts for clock.
function startTime() {
  var today = new Date();
  var y = today.getFullYear();
  var month = today.getMonth() + 1;
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('txt').innerHTML = today.getDate() + "/" + month + "/" + y + "  " + "  " + h + ":" + m + ":" + s;
  var t = setTimeout(startTime, 500);
      }
function checkTime(i) {
  if (i < 10) {i = "0" + i}; //add zero in front of numbers < 10
  return i;
}
//END - Scripts for clock.

//Scripts for changing page theme colour.
function changeBackgroundPurple() {
        document.getElementById("main_container").style.backgroundImage = "url('/static/images/background-pflower.jpg')";
        document.getElementById("event_popup_header").style.backgroundColor = "#B648FD";
        document.getElementById("note_popup_header").style.backgroundColor = "#B648FD";
        document.getElementById("background_popup_header").style.backgroundColor = "#B648FD";
        document.getElementById("logout_popup_header").style.backgroundColor = "#B648FD";
}

function changeBackgroundBlue() {
        document.getElementById("main_container").style.backgroundImage = "url('/static/images/background-tree.jpeg')";
        document.getElementById("event_popup_header").style.backgroundColor = "#56a0d9";
        document.getElementById("note_popup_header").style.backgroundColor = "#56a0d9";
        document.getElementById("background_popup_header").style.backgroundColor = "#56a0d9";
        document.getElementById("logout_popup_header").style.backgroundColor = "#56a0d9";
}

function changeBackgroundRed() {
  document.getElementById("main_container").style.backgroundImage = "url('/static/images/background-rflower.jpeg')";
  document.getElementById("event_popup_header").style.backgroundColor = "#BB0303";
  document.getElementById("note_popup_header").style.backgroundColor = "#BB0303";
  document.getElementById("background_popup_header").style.backgroundColor = "#BB0303";
  document.getElementById("logout_popup_header").style.backgroundColor = "#BB0303";
}

function changeBackgroundYellow() {
  document.getElementById("main_container").style.backgroundImage = "url('/static/images/background-yflower.jpg')";
  document.getElementById("event_popup_header").style.backgroundColor = "#FABB02";
  document.getElementById("note_popup_header").style.backgroundColor = "#FABB02";
  document.getElementById("background_popup_header").style.backgroundColor = "#FABB02";
  document.getElementById("logout_popup_header").style.backgroundColor = "#FABB02";
}

function changeBackgroundOrange() {
  document.getElementById("main_container").style.backgroundImage = "url('/static/images/background-web.jpg')";
  document.getElementById("event_popup_header").style.backgroundColor = "#FF8300";
  document.getElementById("note_popup_header").style.backgroundColor = "#FF8300";
  document.getElementById("background_popup_header").style.backgroundColor = "#FF8300";
  document.getElementById("logout_popup_header").style.backgroundColor = "#FF8300";
}

function changeBackgroundGreen() {
  document.getElementById("main_container").style.backgroundImage = "url('/static/images/background-grass.jpg')";
  document.getElementById("event_popup_header").style.backgroundColor = "#33AC20";
  document.getElementById("note_popup_header").style.backgroundColor = "#33AC20";
  document.getElementById("background_popup_header").style.backgroundColor = "#33AC20";
  document.getElementById("logout_popup_header").style.backgroundColor = "#33AC20";
}
//END - Scripts for changing page theme colour.

//Background Image Preloader
var images = new Array()
function preload() {
  for (i = 0; i < preload.arguments.length; i++) {
    images[i] = new Image()
    images[i].src = preload.arguments[i]
  }
}
preload(
"/static/images/background-rflower.jpeg",
"/static/images/background-tree.jpeg",
"/static/images/background-grass.jpg",
"/static/images/background-yflower.jpg",
"/static/images/background-pflower.jpg",
"/static/images/background-web.jpg"
)
//END - Background Image Preloader

//Quote of the Refresh
var r_text = new Array ();
r_text[0] = "Be yourself; everyone else is already taken. <br> - Oscar Wilde";
r_text[1] = "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind. <br> -  Bernard M. Baruch";
r_text[2] = "You know you're in love when you can't fall asleep because reality is finally better than your dreams. <br> - Dr. Seuss";
r_text[3] = "It is better to be hated for what you are than to be loved for what you are not. <br> - André Gide";
r_text[4] = "We are all in the gutter, but some of us are looking at the stars. <br> - Oscar Wilde";
r_text[5] = "I have not failed. I've just found 10,000 ways that won't work. <br> - Thomas A. Edison";
r_text[6] = "I may not have gone where I intended to go, but I think I have ended up where I needed to be. <br> - Douglas Adams";
r_text[7] = "Today you are You, that is truer than true. There is no one alive who is Youer than You. <br> - Dr. Seuss";
r_text[8] = "Our patience will achieve more than our force. <br> - Edmund Burke";
r_text[9] = "Everything precious is also vulnerable. <br> - Mary H.K. Choi";
r_text[10] = "Don’t Let Yesterday Take Up Too Much Of Today. <br> - Will Rogers";
r_text[11] = "We May Encounter Many Defeats But We Must Not Be Defeated. <br> - Maya Angelou";

var i = Math.floor(r_text.length * Math.random());

document.write("<center><FONT COLOR='black'>" +
r_text[i]  + "</FONT></center><br/>");
//END - Quote of the Refresh
