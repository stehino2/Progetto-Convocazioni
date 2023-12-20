<?php

  include("parametri.php");
  
  // Connessione al server dbms
  $connect = mysqli_connect($server, $username, $password, $databases)
        or die("Connessione non riuscita: " . mysqli_error($connect));
  print ("Connesso con successo <br />");
  
  // selezione database
  mysqli_select_db($connect, $database) 
    or die ("Impossibile selezionare il db");
  
    // Esecuzione della query
  $query = "SHOW TABLES"; // query da eseguire
  $result = mysqli_query($connect, $query)
    or die ("Errore nella query" . mysqli_error($connect));
  
  // Visualizzo il risultato della query
  if (!$result){
    echo "Errore nella query: ".mysqli_error($connect);
  
    }else{

    echo "<h2>Elenco delle tabelle presenti </h2>";
    echo "<table border = 1>";   

    while ($search = mysqli_fetch_array($result))
    {
      echo "<tr><th><a href = 'struttura.php?table={$search[0]}'>" . $search[0] . "</a></th></tr>";
    }

    echo "</table>";
    mysqli_free_result($result);

  }
  
  // libero la memoria occupata dall'istruzione SELECT
  mysqli_close($connect); // chiusura della connessione al server Mysql
?>
