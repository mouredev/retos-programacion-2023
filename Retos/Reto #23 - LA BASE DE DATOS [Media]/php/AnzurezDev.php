<?php
define( "HOST"  , "mysql-5707.dinaserver.com" );
define( "USER"  , "mouredev_read" );
define( "PASS"  , "mouredev_pass" );
define( "DB"    , "moure_test" );
define( "PORT"  , 3306 );

$mysqli = new mysqli( HOST, USER, PASS, DB, PORT );
$query  = "SELECT * FROM `challenges`";

if ( !$mysqli->connect_errno ) {
    $result = $mysqli->query( $query );

    while ( $row = $result->fetch_assoc() ) {
        $columns = array_keys( $row );

        for ( $index=0; $index<count($row); $index++ ) {
            $column = $columns[ $index ];
            echo utf8_encode( $row[$column] ) . "\t";
        }

        echo "\n";
    }

    $result->free();
} else {
    echo "Falló la conexión: " . $mysqli->connect_error;
}

$mysqli->close();
?>