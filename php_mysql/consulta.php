<?php

$nombre = "";
$apellido = "";
$email = "";

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


$sql = "SELECT id, firstname, lastname,reg_date FROM MyGuests";  
$result = $conn->query($sql); 

echo '<table align="center" border=1>';
echo '<tr>'; 
echo '<td>id </td>';
echo '<td>firstname</td>';
echo '<td>lastname</td>';
echo '<td>reg_date</td>';
echo '</tr>';  

if ($result->num_rows > 0)
{
    while($row = $result->fetch_assoc()) {
        echo "<tr>"; 
        echo "<td>". $row["id"]. "</td>";     
        echo "<td>". $row["firstname"]. "</td>";     
        echo "<td>". $row["lastname"]. "</td>";     
        echo "<td>". $row["reg_date"]. "</td>";     
        echo "</tr>"; 


    }


}

echo "</table>"; 


?>
