
<?php
  function picam() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh picam");
  }
  function pacman() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh pacman");
  }
  function lowellmakes() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh lowellmakes");
  }
  function flame() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh flame");
  }
  function mario() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh mario");
  }
  function piday() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh piday");
  }
  function video() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh video");
  }
  function none() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh none");
  }

  if (isset($_GET['nonestart'])) {
    none();
  }
  if (isset($_GET['picamstart'])) {
    picam();
  }
  if (isset($_GET['pacmanstart'])) {
    pacman();
  }
  if (isset($_GET['flamestart'])) {
    flame();
  }
  if (isset($_GET['lowellmakesstart'])) {
    lowellmakes();
  }
  if (isset($_GET['mariostart'])) {
    mario();
  }
  if (isset($_GET['pidaystart'])) {
    piday();
  }
  if (isset($_GET['videostart'])) {
    video();
  }
?>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" /> 
</head>
<center>
<table border=1 style="height:100%;width:100%; position: absolute; top: 0; bottom: 0; left: 0; right: 0;">
<tr>
<td><a href='index.php?picamstart=true'><image style="display:block;" width="100%" height="100%" src=picam.png></image></a></td>
<td><a href='index.php?mariostart=true'><image style="display:block;" width="100%" height="100%" src=mario2.jpg></image></a></td>
</tr>
<tr>
<td><a href='index.php?pidaystart=true'><image style="display:block;" width="100%" height="100%" src=piday_s.png></image></a></td>
<td><a href='index.php?flamestart=true'><image style="display:block;" width="100%" height="100%" src=flame-0.jpg></image></a></td>
</tr>
<tr>
<td><a href='index.php?pacmanstart=true'><image style="display:block;" width="100%" height="100%" src=pacman.jpg></image></a></td>
<td><a href='index.php?lowellmakesstart=true'><image style="display:block;" width="100%" height="100%" src=lm.png></image></a></td>
</tr>
<tr>
<td><a href='index.php?videostart=true'><image style="display:block;" width="100%" height="100%" src=bbb.png></image></a></td>
<td><a href='index.php?nonestart=true'><image style="display:block;" width="100%" height="100%" src=off.png></image></a></td>
</tr>
</table>
</html>
