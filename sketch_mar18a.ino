char stringToMorseCode[] = "FIAP"; //String to be converted to Morse Code

int ledY = 8;
int dotLen = 100;
int dashLen = dotLen * 8;
int pause = dotLen * 4;
int letterpause = pause * 2;

//F . . _ .
//I . .
//A . _
//P . _ _ .

void setup() {
pinMode(ledY, OUTPUT);
}

void loop()
{
for (int i = 0; i < sizeof(stringToMorseCode) - 1; i++)
  {
    char tmpChar = stringToMorseCode[i];
    tmpChar = toUpperCase(tmpChar);
	GetChar(tmpChar);
  }
}

// Dot
void MorseDot(){
    digitalWrite(ledY, HIGH);
    delay(dotLen);
}

// Dash
void MorseDash(){
    digitalWrite(ledY, HIGH);
    delay(dashLen);
}

// Pause between dot and dash
void dotdashpause(){
    digitalWrite(ledY, LOW);
    delay(pause);
}

//Letters to Morse Code
void GetChar(char tmpChar)
{

switch (tmpChar)
{
case 'F':
  MorseDot();
  dotdashpause();
  MorseDot();
  dotdashpause();
  MorseDash();
  dotdashpause();
  MorseDot();
  dotdashpause();
break;
    
case 'I':
  MorseDot();
  dotdashpause();
  MorseDot();
  dotdashpause();
break;
    
case 'A':
  MorseDot();
  dotdashpause();
  MorseDash();
  dotdashpause();
break;

case 'P':
  MorseDot();
  dotdashpause();
  MorseDash();
  dotdashpause();
  MorseDash();
  dotdashpause();
  MorseDot();
  dotdashpause();
break;
    }
delay(letterpause);
} 

