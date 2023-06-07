<?php
set_time_limit(300); 
//Conexion a MYSQLi
$conn = mysqli_connect('mysql-5707.dinaserver.com','mouredev_read','mouredev_pass');

if (!$conn)
{ 
//echo 'No se realizo la conexion'; 
}
else{
// echo 'Conexion realizada a sql server por mysqli';
}

   $query0= "SELECT * FROM moure_test.challenges";
   $resultado0= mysqli_query($conn,$query0);
   
   //Si lo encuentra actualiza su estatus
   if (!$resultado0){
      echo 'No se encontro el registro'.'<br>';
      }
    else
      {  	  
	  while($row=mysqli_fetch_array($resultado0))
	  {	   
          echo $row[0].'<br>';
          echo $row[1].'<br>';
          echo $row[2].'<br>';
          echo $row[3].'<br><br>';	 
	  } 
      }  

mysqli_close($conn);

?>
