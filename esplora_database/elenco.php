<?php
 include("parametri.php");

 $connect = mysqli_connect($server, $username, $password)
  or die("Connessione non riuscita: " . mysqli_error($connect));
 // print("Connesso con successo <br>");

 mysqli_select_db($connect, $database)
  or die("Impossibile selezionare il db");

 $query = "SHOW TABLES";
 $result = mysqli_query($connect, $query)
  or die("Errore nella query" . mysqli_error($connect));

 echo "<html><head><title>Elenco Tabelle</title></head></body>";
 echo "<h1>Elenco delle Tabelle</h1>";
 echo "<ul>";

 while($table = mysqli_fetch_array($result)) {
  echo "<li><a href = 'struttura.php?table={$table[0]}'>" . $table[0] . "</a></li>";
 }

 echo "</ul></body></html>";

 mysqli_free_result($result);
 mysqli_close($connect);
?>