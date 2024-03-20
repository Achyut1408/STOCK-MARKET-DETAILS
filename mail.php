<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('log_errors', 1);
ini_set('error_log', 'error.log');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Admin's email address
    $admin_email = "digitalliving2@gmail.com";

    // Email subject
    $subject = "Mail from Website";

    // Email message
    $email_message = "Name: $name\n";
    $email_message .= "Email: $email\n";
    $email_message .= "Message:\n$message";

    // Send email to admin
    $headers = "From: $email";

    if (mail($admin_email, $subject, $email_message, $headers)) {
        // Email sent successfully
        header("Location: index.html");
        exit();
    } else {
        // Email sending failed
        error_log("Email sending failed.");
        header("Location: error.html");
        exit();
    }
}


?>
