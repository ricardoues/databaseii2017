<?php

$nombre = $_POST['nombre'];
$apellido = $_POST['apellidos'];
$email = $_POST['email'];

$servername = "localhost";
$username = "";
$password = "";
$dbname = "";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 


$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('$nombre', '$apellido', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "<script>"; 
    echo "alert(\"Registro ingresado\");"; 
    echo "window.location=\"insertar.html\""; 
    echo "</script>";  
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

?>
