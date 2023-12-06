<?php
$hostname = 'mysql-5707.dinaserver.com';
$username = 'mouredev_read';
$password = 'mouredev_pass';
$database = 'moure_test';

$con = new mysqli($hostname, $username, $password, $database);
if($con->connect_errno){
    die('Error ' . $this->con->connect_error);
}

if ($resultado = $con->query('SELECT * FROM challenges')) {
    
    while ($fila = $resultado->fetch_array(MYSQLI_NUM)) {
        echo $fila[0] ."\t". $fila[1] ."\t". $fila[2] ."\t". $fila[3] ."\n";
    }

    $resultado->free();
}


$con->close();
?>
