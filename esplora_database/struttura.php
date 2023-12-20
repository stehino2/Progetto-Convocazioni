<?php
 include("parametri.php");

 $connect = mysqli_connect($server, $username, $password)
  or die("Connessione non riuscita: " . mysqli_error($connect));
 // print("Connesso con successo <br>");

 mysqli_select_db($connect, $database)
  or die("Impossibile selezionare il db");

 $selected_table = $_GET['table']; // ottengo il nome della tabella

 $query = "DESCRIBE " . $selected_table;
 $result = mysqli_query($connect, $query)
  or die("Errore nella query" . mysqli_error($connect));

 echo "<html><head><title>Struttura della Tabella</title></head><body>";
 echo "<h1>Struttura della Tabella: $table</h1>";
 echo "<table border='1'>";
 echo "<tr><th>Colonna</th><th>Tipo</th></tr>";

 //stampo i dati della struttura
 while($row = mysqli_fetch_array($result)) {
  echo "<tr><td>{$row['Field']}</td><td>{$row['Type']}</td></tr>";
 }

 echo "</table><p><a href='contenuto.php?table=$selected_table'>Visualizza Contenuto</a></p></body></html>";

 mysqli_free_result($result);
 mysqli_close($connect);
?>
