<?php
    include("parametri.php");

    $connect = mysqli_connect($server, $username, $password)
    or die("Connessione non riuscita: " . mysqli_error($connect));

    mysqli_select_db($connect, $database)
    or die("Impossibile selezionare il db");

    echo "<html><head><title>Eliminazione</title></head><body>";
    echo "<h1>Eliminazione di un articolo</h1>";

    echo '<form method="post" action="elimina_articolo.php">

        <label for="cdArticolo">CdArticolo:</label>
        <input type="text" name="cdArticolo" required><br>
        <input type="submit" value="Elimina"></form>
        <p><a href="home.php">Torna agli articoli</a></p>';

    echo "</body></html>";

    // Controlla se il modulo di inserimento è stato inviato
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $cdArticolo = $_POST["cdArticolo"];

        $query = "DELETE FROM db_Articolo WHERE cdArticolo = '$cdArticolo'";

        if (mysqli_query($connect, $query)) {
            echo "Articolo eliminato con successo.";
        } else {
            echo "Errore durante l'eliminazione dell'articolo: " . mysqli_error($connect);
        } 
    }

    mysqli_close($connect);
?>

