
<?php
  function picam() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh picam > /dev/null 2>&1 &");
  }
  function pacman() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh pacman > /dev/null 2>&1 &");
  }
  function lowellmakes() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh lowellmakes > /dev/null 2>&1 &");
  }
  function flame() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh flame > /dev/null 2>&1 &");
  }
  function mario() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh mario > /dev/null 2>&1 &");
  }
  function piday() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh piday > /dev/null 2>&1 &");
  }
  function video() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh video > /dev/null 2>&1 &");
  }
  function mariovideo() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh mariovideo > /dev/null 2>&1 &");
  }
  function none() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh none > /dev/null 2>&1 &");
    exec("sudo /home/pi/fadecandy_shenanigans/black.py > /dev/null 2>&1 &");
  }
  function shutdown() {
    exec("sudo /home/pi/fadecandy_shenanigans/webservice.sh none > /dev/null 2>&1 &");
    exec("sudo /home/pi/fadecandy_shenanigans/black.py > /dev/null 2>&1 &");
    exec("sudo /sbin/shutdown -h now > /dev/null 2>&1 &");
  }
  if (isset($_GET['nonestart'])) {
    none();
  }
  if (isset($_GET['shutdown'])) {
    shutdown();
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
  if (isset($_GET['mariovideostart'])) {
    mariovideo();
  }
?>
<head>
</head>
<script type="text/javascript">
<!--
if (screen.width <= 699) {
document.location = "mobile.php";
}
//-->
</script>
<center>
<table border=1>
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
<td><a href='index.php?mariovideostart=true'><image style="display:block;" width="100%" height="100%" src=mario11.png></image></a></td>
</tr>
<tr>
<td><a href='index.php?nonestart=true'><image style="display:block;" width="100%" height="100%" src=screenoff.png></image></a></td>
<td><a href='index.php?shutdown=true'><image style="display:block;" width="100%" height="100%" src=poweroff.png></image></a></td>
</tr>
</table>
</html>
