<?php
/*
//For Insert query
// Assuming your database credentials
$hostname = 'localhost';
$username = 'root';
$password = 'your_password';
$database = 'person';

// Create a new MySQLi instance
$mysqli = new mysqli($hostname, $username, $password, $database);

// Check for connection errors
if ($mysqli->connect_error) {
    die('Connection failed: ' . $mysqli->connect_error);
}

// Use prepared statement to avoid SQL injection
$firstName = 'Paul';
$lastName = 'Shalaye';

$stmt = $mysqli->prepare("INSERT INTO name (`First Name`, `Last Name`) VALUES (?, ?)");
$stmt->bind_param("ss", $firstName, $lastName);

// Execute the statement
$stmt->execute();

// Close the statement and connection
$stmt->close();
$mysqli->close();



// For select Query
// Assuming your database credentials
$hostname = 'localhost';
$username = 'root';
$password = 'your_password';
$database = 'person';

// Create a new MySQLi instance
$mysqli = new mysqli($hostname, $username, $password, $database);

// Check for connection errors
if ($mysqli->connect_error) {
    die('Connection failed: ' . $mysqli->connect_error);
}


// SELECT query
$querySelect = "SELECT * FROM name";
$result = $mysqli->query($querySelect);

$result_count=$mysqli->field_count;

// Check if the SELECT query was successful
if ($result) {
    // Fetch data and display it
    while ($row = $result->fetch_assoc()) {
        echo "First Name: " . $row['First Name'] . " | Last Name: " . $row['Last Name'] . "<br>";
    }

    // Free the result set
    $result->free();
} else {
    // Display an error message if the SELECT query fails
    echo "Error: " . $mysqli->error . "<br>";
}

// Close the connection
$mysqli->close();
*/


// Assuming your database credentials
$hostname = 'localhost';
$username = 'root';
$password = 'your_password';
$database = 'person';

// Create a new MySQLi instance
$mysqli = new mysqli($hostname, $username, $password, $database);

// Check for connection errors
if ($mysqli->connect_error) {
    die('Connection failed: ' . $mysqli->connect_error);
}

// SELECT query Joining two tables
$querySelect = "SELECT n.ID, n.First_Name, n.Last_Name, p.Manufacture_Date 
FROM name n 
LEFT JOIN product p 
ON n.ID = p.ID";
$result = $mysqli->query($querySelect);

// Check if the SELECT query was successful
if ($result) {
    // Display the result in a tabular form
    echo '<table border="1">';
    echo '<tr><th>ID</th><th>First_Name</th><th>Last_Name</th><th>Manufacture_Date</th></tr>';

    // Fetch data and display it
    while ($row = $result->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . $row['ID'] . '</td>';
        echo '<td>' . $row['First_Name'] . '</td>';
        echo '<td>' . $row['Last_Name'] . '</td>';
        echo '<td>' . $row['Manufacture_Date'] . '</td>';
        echo '</tr>';
    }

    echo '</table>';

    // Free the result set
    $result->free();
} else {
    // Display an error message if the SELECT query fails
    echo "Error: " . $mysqli->error . "<br>";
}

// Close the connection
$mysqli->close();