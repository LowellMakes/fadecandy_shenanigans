
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

<a href='index.php?picamstart=true'>Run picam</a>
</br>
<a href='index.php?mariostart=true'>Run mario</a>
</br>
<a href='index.php?pidaystart=true'>Run piday</a>
</br>
<a href='index.php?flamestart=true'>Run flame</a>
</br>
<a href='index.php?pacmanstart=true'>Run pacman</a>
</br>
<a href='index.php?lowellmakesstart=true'>Run lowellmakes</a>
</br>
<a href='index.php?videostart=true'>Run video</a>
</br>
<a href='index.php?nonestart=true'>Run none</a>
</br>
</html>
