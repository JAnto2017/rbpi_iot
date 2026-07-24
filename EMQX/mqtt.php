<?php

//require_once __DIR__ . '/vendor/autoload.php';
require('/var/www/mqtt_php/html/vendor/autoload.php');


use Bluerhinos\phpMQTT;
//use \Bluerhinos\phpMQTT;

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

  $send = isset($json["tempC"]) ? $json["tempC"] : $message;
  echo 'mensaje: '.$send;
}

// bucle que está escuchando continuamente
while ($mqtt->proc()) {
  
}

//$mqtt->close();
