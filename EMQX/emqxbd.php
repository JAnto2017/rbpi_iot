<?php

require('/var/www/html/vendor/autoload.php');

use Bluerhinos\phpMQTT;

$server   = "192.168.1.41";
$port     = 1883;
$username = "emqx";
$password = "public";
$clientId = 'phpMQTT-'.rand(5, 15);
$topicPub = "phpMQTT/testpub";
$topicSub = "phpMQTT/testsub";

$mqtt = new phpMQTT($server, $port, $clientId, null);

$conex_ok = $mqtt->connect(false, null, $username, $password);

if ($conex_ok) {
  $mqtt->publish($topicPub, "Hello World from PHP", '', 0, false);
  
  //topicos a suscribirse
  $topicos[$topicSub] = array("qos"=>0, "function"=>"phpMQTTsubcribe");
  
  $mqtt->subscribe($topicos);
  //$mqtt->close();
}

// definición de la función que recibe los mensajes del MQTT al que se está suscrito
function phpMQTTsubcribe($topic, $message) {
  //echo "Topic: $topic\n";
  //echo "Message: $message\n";

  //variabes JSON
  $json = json_decode($message, true);
  //$json = json_encode($message);
  // {"temperatura": "23.5" }
  // permite extraer el valor de la clave "temperatura"
  $sendDB = isset($json["tempC"]) ? $json["tempC"] : $message;
  echo 'mensaje: '.$sendDB;

  // escribir en la base de datos
  $host = '192.168.1.41';
  $dbname = 'mqtt';
  $dbuser = 'root';
  $dbpass = '1234';
  try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $dbuser, $dbpass);
    //$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("INSERT INTO datos VALUES (NULL,?,?)");
    //$stmt->bindParam(':temperatura', $send);
    $stmt->execute(array($topic, $sendDB));
    //$stmt->execute();
    $conn = null;
  } catch (PDOException $e) {
    die("Error al conectar con la base de datos: ". $e->getMessage());
  }
}

// bucle que está escuchando continuamente
while ($mqtt->proc()) {
  
}

//$mqtt->close();
