<?php
// Assuming your database credentials
$hostname = 'localhost';
$username = 'root';
$password = 'U2gtza(6xOND4GfO';
$database = 'person';

// Create a new MySQLi instance
$mysqli = new mysqli($hostname, $username, $password, $database);

// Check for connection errors
if ($mysqli->connect_error) {
    die('Connection failed: ' . $mysqli->connect_error);
}

// Use prepared statement to avoid SQL injection
$firstName = 'Jim';
$lastName = 'Baker';

$stmt = $mysqli->prepare("INSERT INTO name (`First Name`, `Last Name`) VALUES (?, ?)");
$stmt->bind_param("ss", $firstName, $lastName);

// Execute the statement
$stmt->execute();

// Close the statement and connection
$stmt->close();
$mysqli->close();
?>
