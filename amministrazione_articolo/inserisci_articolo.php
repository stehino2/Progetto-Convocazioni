<?php

include("parametri.php");

$connect = mysqli_connect($server, $username, $password)
or die("Connessione non riuscita: " . mysqli_error($connect));

mysqli_select_db($connect, $database)
or die("Impossibile selezionare il db");

echo "<html><head><title>Inserimento</title></head><body>";
echo "<h1>Inserimento di un nuovo articolo</h1>";

echo '<form method="post" action="inserisci_articolo.php">

    <label for="cdArticolo">CdArticolo:</label>
    <input type="text" name="cdArticolo" required><br>

    <label for="Descrizione">Descrizione:</label>
    <input type="text" name="Descrizione" required><br>

    <label for="Linea">Linea:</label>
    <select name="Linea" required>
        <option value="Classic Cars">Classic Cars</option>
        <option value="Motorcycles">Motorcycles</option>
        <option value="Planes">Planes</option>
        <option value="Ships">Ships</option>
        <option value="Trains">Trains</option>
        <option value="Trucks and Buses">Trucks and Buses</option>
        <option value="Vintage Cars">Vintage Cars</option>
    </select><br>

    <label for="Scala">Scala:</label>
    <input type="text" name="Scala" required><br>

    <label for="Fornitore">Fornitore:</label>
    <input type="text" name="Fornitore" required><br>

    <label for="Note">Note:</label>
    <input type="text" name="Note"><br>

    <label for="Quantita">Quantita:</label>
    <input type="number" name="Quantita" required><br>

    <label for="Costo">Costo:</label>
    <input type="number" name="Costo" required><br>

    <label for="MSRP">MSRP:</label>
    <input type="number" name="MSRP" required><br>

    <input type="submit" value="Inserisci">
    </form>
    <p><a href="home.php">Torna agli articoli</a></p>';

echo "</body></html>";

//$selected_table = $_GET['table'];

// Controlla se il modulo di inserimento è stato inviato
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $cdArticolo = $_POST["cdArticolo"];
    $Descrizione = $_POST["Descrizione"];
    $Linea = $_POST["Linea"];
    $Scala = $_POST["Scala"];
    $Fornitore = $_POST["Fornitore"];
    $Note = $_POST["Note"];
    $Quantita = $_POST["Quantita"];
    $Costo = $_POST["Costo"];
    $MSRP = $_POST["MSRP"];

    // Verifica se il cdArticolo già esiste nel database
    $checkCdArticoloQuery = "SELECT CdArticolo FROM db_Articolo WHERE CdArticolo = '$cdArticolo'";
    $resultCdArticolo = mysqli_query($connect, $checkCdArticoloQuery);

    if (mysqli_num_rows($resultCdArticolo) > 0) {
        echo "Errore: CdArticolo già esistente nel database.";
    } else {
        $query = "INSERT INTO db_Articolo (cdArticolo, Descrizione, Linea, Scala, Fornitore, Note, Quantita, Costo, MSRP) 
        VALUES ('$cdArticolo', '$Descrizione', '$Linea', '$Scala', '$Fornitore', '$Note', '$Quantita', '$Costo', '$MSRP')";

        if (mysqli_query($connect, $query)) {
            echo "Nuovo articolo inserito con successo.";
        } else {
            echo "Errore durante l'inserimento dell'articolo: " . mysqli_error($connect);
        } 
    } 
}

mysqli_close($connect);
?>

