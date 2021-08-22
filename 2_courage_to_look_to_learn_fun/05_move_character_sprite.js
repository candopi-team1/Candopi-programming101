var canvas;  // the canvas element which will draw on
var ctx;     // the "context" of the canvas that will be used (2D or 3D)
var dx = 50; // the rate of change (speed) horizontal object
var x = 30;  // horizontal position of the object (with initial value)
var y = 0;   // vertical position of the object (with initial value)
var WIDTH = 1000; // width of the rectangular area
var HEIGHT = 340; // height of the rectangular area

var tile1 = new Image ();  // Image to be loaded and drawn on canvas
var curr_pos_of_character = 0;           // display the current position of the character
var NUM_POSICOES = 6;      // Number of images that make up the movement




function KeyDown(evt){
    switch (evt.keyCode) {
        case 39:  /* Arrow to the right */
            if (x + dx < WIDTH){
                x += dx;
                curr_pos_of_character++;
                if(curr_pos_of_character > NUM_POSICOES)
                    curr_pos_of_character = 0; //1;
            }
            break;

        case 37:  /* Arrow to the Left */
            if (x > 20){
                x -= dx;
                curr_pos_of_character--;                
                if(curr_pos_of_character == -1)
                    curr_pos_of_character = 6;
            }
            break;
            
    }
}


function Draw() {    
    console.log(curr_pos_of_character);

    tile1.src = curr_pos_of_character+".png";
    ctx.drawImage(tile1, x, y);
}


function LimparTela() {
    ctx.fillStyle = "rgb(233,233,233)";    
    ctx.beginPath();
    ctx.rect(0, 0, WIDTH, HEIGHT);
    ctx.closePath();
    ctx.fill();    
}

function Update() {
    LimparTela();    
    Draw();
}


function Start() {
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
    return setInterval(Update, 100);
}

window.addEventListener('keydown', KeyDown);
Start();



