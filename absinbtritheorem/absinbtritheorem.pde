float r = 400 / 2f;
float theta = 0;
float a = -r / 4;
float b = 3 * r / 4;
float c = sin(acos(b / r)) * r;

void setup() {
  size(800, 800);
  frameRate(60);
}

void drawGraph() {
  b = mouseX;
  c = -sin(acos(b / r)) * r;
  
  translate(width / 2, height / 2);
  stroke(0);
  line(-width / 2f, 0, width / 2f, 0);  
  line(0, -height / 2f, 0, height / 2f);  
  
  fill(0, 0, 0, 0);
  ellipse(0, 0, r*2f, r*2f);
  ellipse(a, 0, 10, 10);
  ellipse(b, 0, 10, 10);
  ellipse(b, c, 10, 10);
  
  line(a, 0, b, c);
  line(b, 0, b, c);
  
  float theta = atan(-c / abs(a - b));
  
  textSize(20);
  fill(0);
  text("b: " + b, b + 10, -10);
  text("a: " + a, a, 25);
  text("sin(acos(b / r)): " + c, b + 10, c - 10);
  text("θ: " + theta, a, 50);
}

void draw() {
  background(255);
  pushMatrix();
  drawGraph();
  popMatrix();
  
  theta += .005f;
  if(degrees(theta) >= 360) theta = 0;
}