<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

// Get form data
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
$subject = filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING);
$message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

// Validate required fields
if (empty($name) || empty($email) || empty($subject) || empty($message)) {
    http_response_code(400);
    echo json_encode(['error' => 'Alle Felder sind erforderlich']);
    exit;
}

// Validate email
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['error' => 'Ungültige E-Mail-Adresse']);
    exit;
}

// Email configuration
$to = 'office@fj-marketing.com';
$email_subject = 'Neue Kontaktanfrage von JKB Website: ' . $subject;

// Email body
$email_body = "
Neue Kontaktanfrage von der JKB Software Website:

Name: $name
E-Mail: $email
Betreff: $subject

Nachricht:
$message

---
Diese E-Mail wurde automatisch von der JKB Software Website gesendet.
Antworten Sie direkt an: $email
";

// Email headers
$headers = array(
    'From' => 'noreply@jkb-software.de',
    'Reply-To' => $email,
    'X-Mailer' => 'PHP/' . phpversion(),
    'Content-Type' => 'text/plain; charset=UTF-8'
);

// Convert headers array to string
$headers_string = '';
foreach ($headers as $key => $value) {
    $headers_string .= $key . ': ' . $value . "\r\n";
}

// Send email
if (mail($to, $email_subject, $email_body, $headers_string)) {
    echo json_encode(['success' => 'E-Mail erfolgreich gesendet']);
} else {
    http_response_code(500);
    echo json_encode(['error' => 'Fehler beim Senden der E-Mail']);
}
?>
