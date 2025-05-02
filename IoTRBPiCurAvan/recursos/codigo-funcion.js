// @ts-nocheck
temp = msg.payload

msg.payload = [{
    temperatura: temp
},
{
    sensorid: msg.topic
}];

return msg;
