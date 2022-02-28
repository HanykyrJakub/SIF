<!DOCTYPE html>
<html>
<body>
<?php

    date_default_timezone_set("EUROPE/PRAGUE");
    echo "<p>";

    $days = [
       1=> "Pondeli", "utery", "streda", "ctvrtek", "Patek", "Sobota", "Nedele" 
    ];

    echo $days[date("N")];
    echo " " . date("j. ");

    $Months = [
        1 => "Leden","unor", "brezen", "Duben", "Kveten", "Cerven", "cervenec", "srpen", "Zari", "Rijen", "Listopad", "Prosinec"
    ];

    echo $Months[date("n")];
    echo date("Y H:i:s");
    echo "</p>";
    echo '<ul>';
    echo '<li>H:';


?>
</body>
</html>