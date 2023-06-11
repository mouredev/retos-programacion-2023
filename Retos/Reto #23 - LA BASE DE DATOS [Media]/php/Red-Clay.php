<?php
$dbhost = "mysql-5707.dinaserver.com";
$dbuser = "mouredev_read";
$dbpass = "mouredev_pass";
$dbname = "moure_test";
$port = 3306;

/*Iniciamos la conexión*/
$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname,$port);
if($con==false)
{
  die("no hay conexion: ".mysqli_connect_error());
  echo "no hay conexion: ".mysqli_connect_error();
}

$query="SELECT * FROM challenges";
$resultado= mysqli_query($con,$query);
$columnas = mysqli_fetch_fields($resultado);
mysqli_close($con)
?>
<table >
    <?php foreach($columnas as $columna):?>
        <th scope="col">
            <?php  echo utf8_encode(ucfirst($columna->name)); ?>
        </th>
    <?php endforeach;
    foreach($resultado as $datos=>$valor):?>
        <tr>               
        <?php 
        foreach($valor as $columna):?>
        <td>
        <?php 
            echo utf8_encode($columna);
            next($valor);  
        ?>
        </td>
        <?php endforeach; ?>
        </tr>
    <?php endforeach;?>
</table>
