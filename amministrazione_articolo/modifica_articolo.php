<?php
include("parametri.php");

$connect = mysqli_connect($server, $username, $password) or die("Connessione non riuscita: " . mysqli_error($connect));

mysqli_select_db($connect, $database) or die("Impossibile selezionare il db");

echo "<html><head><title>Modifica</title></head><body>";
echo "<h1>Modifica di un articolo</h1>";

echo '<form method="post" action="modifica_articolo.php">
    <label for="cdArticolo">CdArticolo:</label>
    <input type="text" name="cdArticolo" required><br>
    <input type="submit" value="Seleziona"></form>
    <p><a href="home.php">Torna agli articoli</a></p>';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $cdArticolo = $_POST["cdArticolo"];

    $checkCdArticoloQuery = "SELECT * FROM db_Articolo WHERE CdArticolo = '$cdArticolo'";
    $resultCdArticolo = mysqli_query($connect, $checkCdArticoloQuery);

    if (mysqli_num_rows($resultCdArticolo) > 0) {
        $row = mysqli_fetch_assoc($resultCdArticolo); // Fetch the data

        echo "Articolo presente all'interno del database";

        echo "<form action='' method='post'>
                <input type='hidden' name='cdArticolo' value='{$row['cdArticolo']}'>
                Descrizione: <input type='text' name='descrizione' value='{$row['descrizione']}'><br>
                <label for='linea'>Linea:</label>
                <select name='Linea' required>
                    <option value='Classic Cars'>Classic Cars</option>
                    <option value='Motorcycles'>Motorcycles</option>
                    <option value='Planes'>Planes</option>
                    <option value='Ships'>Ships</option>
                    <option value='Trains'>Trains</option>
                    <option value='Trucks and Buses'>Trucks and Buses</option>
                    <option value='Vintage Cars'>Vintage Cars</option>
                </select><br>
                Scala: <input type='text' name='scala' value='{$row['scala']}'><br>
                Fornitore: <input type='text' name='fornitore' value='{$row['fornitore']}'><br>
                Note: <input type='text' name='note' value='{$row['note']}'><br>
                Quantità: <input type='text' name='quantita' value='{$row['quantita']}'><br>
                Costo: <input type='text' name='costo' value='{$row['costo']}'><br>
                MSRP: <input type='text' name='msrp' value='{$row['msrp']}'><br>
                <input type='submit' name='submit' value='Salva Modifiche'>
              </form>";

        if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['submit'])) {
            $descrizione = $_POST['descrizione'];
            $linea = $_POST['linea'];
            $scala = $_POST['scala'];
            $fornitore = $_POST['fornitore'];
            $note = $_POST['note'];
            $quantita = $_POST['quantita'];
            $costo = $_POST['costo'];
            $msrp = $_POST['msrp'];

            $query = "UPDATE db_Articolo
                SET descrizione='$descrizione', linea='$linea', scala='$scala', fornitore='$fornitore',
                note='$note', quantita='$quantita', costo='$costo', msrp='$msrp'
                WHERE CdArticolo = '$cdArticolo'";

            if (mysqli_query($connect, $query)) {
                echo "Modifiche salvate con successo!";
            } else {
                echo "Errore nel salvataggio delle modifiche: " . mysqli_error($connect);
            }
        }
    } else {
        echo "Articolo non presente all'interno del database";
    }
}

echo "</body></html>";

mysqli_close($connect);
?>


