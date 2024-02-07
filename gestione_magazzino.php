<?php
 // Includo i parametri per poter accedere al database
 include("parametri.php");

 // Mi connetto al database
 $connect = mysqli_connect($server, $username, $password)
  or die("Connessione non riuscita: " . mysqli_error($connect));

 mysqli_select_db($connect, $database)
  or die("Impossibile selezionare il db");

 // Seleziono la tabella di mio interesse e mi connetto ad essa
 $table = "2401_db_Magazzino";

 // Variabili per gestire la ricerca
 $searchField = isset($_GET['searchField']) ? $_GET['searchField'] : '';
 $searchValue = isset($_GET['searchValue']) ? $_GET['searchValue'] : '';

 /* Se ho scritto qualcosa nel campo della ricerca
 allora esegue la ricerca, altrimenti stampa
 semplicemente la tabella */
 if (!empty($searchField) && !empty($searchValue)) {
    $query = "SELECT * FROM " . $table . " WHERE $searchField LIKE '%$searchValue%'";
 } else {
    $query = "SELECT * FROM " . $table;
 }

 $result = mysqli_query($connect, $query)
  or die("Errore nella query" . mysqli_error($connect));

 // Stampo il titolo della pagina e il nome delle colonne della tabella
 echo "<html><head><title>Elenco Magazzino</title></head><body>";
 echo "<h1>Magazzino</h1>";
 echo "<table border='1'>";

 // Tasto di ricerca
 echo "<form method='get' action='gestione_magazzino.php'>
        <label for='Campo'>Ricerca in:</label>
        <select name='searchField' value= '$searchField' required>
        <option value='CodiceArticolo'>Codice Articolo</option>
        <option value='Descrizione'>Descrizione</option>
        <option value='Quantità'>Quantità</option>
        <option value='Prezzo'>Prezzo</option>
        </select><br>
        <label for='search'>Valore</label>
    <input type='text' name='searchValue' value='$searchValue'>
    <button type='submit'>Cerca</button>
    </form>";

 echo "<tr>";
 echo "<th>Codice Articolo</th> 
       <th>Descrizione</th>
       <th>Quantità</th>
       <th>Prezzo</th>";
 echo "</tr>";

// Verifica se è stata inviata una richiesta GET per la ricerca
if(isset($_GET['search']) && isset($_GET['searchField'])) {
   $searchTerm = $_GET['search'];
   $searchField = $_GET['searchField'];

   // Aggiungi la clausola WHERE solo se sono stati forniti valori di ricerca
   if (!empty($searchTerm)) {
       $query .= " WHERE $searchField LIKE '%$searchTerm%'";
   }
}

 // Stampo i dati della tabella
while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>{$row['CodiceArticolo']}</td>";
    echo "<td>{$row['Descrizione']}</td>";
    echo "<td>{$row['Quantità']}</td>";
    echo "<td>{$row['Prezzo']}</td>";
    // Aggiungo anche un pulsante per modificare gli articoli nel magazzino
    echo "<td><a href='modifica_articolo.php?id={$row['CodiceArticolo']}'><button type='button'>Modifica</button></a>";
    echo "</tr>";
 }

 echo "</table></body></html>";

 // Libero il buffer
 mysqli_free_result($result);
 mysqli_close($connect);
?>
