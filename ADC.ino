int sensor;
float val;


void setup()
{
  Serial.begin(115200);
  delay(10);
}


void loop()
{
  sensor = analogRead(A0);
  val = (float)sensor/1024*5.0;
  
  if (val<0.100)
  {
    Serial.print(-1);
    delay(10000);
    return;
  }

  Serial.println(val,3);
  delay(3000);
}
