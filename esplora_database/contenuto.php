<?php
 include("parametri.php");

 $connect = mysqli_connect($server, $username, $password)
  or die("Connessione non riuscita: " . mysqli_error($connect));

 mysqli_select_db($connect, $database)
  or die("Impossibile selezionare il db");

 $selected_table = $_GET['table'];

 $query = "SELECT * FROM " . $selected_table;
 $result = mysqli_query($connect, $query)
  or die("Errore nella query" . mysqli_error($connect));

 echo "<html><head><title>Contenuto della Tabella</title></head><body>";
 echo "<h1>Contenuto della Tabella: $tableName</h1>";
 echo "<table border='1'><tr>";

 //ottengo i nomi delle colonne
 $fields = mysqli_fetch_fields($result);

 echo "<tr>";

 //stampo i nomi delle colonne
 foreach ($fields as $field) {
  echo "<th>" . $field->name . "</th>";
 }

 echo "</tr>";

 //cerco i dati
 mysqli_data_seek($result, 0);

 //stampo i dati
 while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    foreach ($row as $value) {
        echo "<td>$value</td>";
    }
    echo "</tr>";
 }

 echo "</table></body></html>";

 mysqli_free_result($result);
 mysqli_close($connect);
?>