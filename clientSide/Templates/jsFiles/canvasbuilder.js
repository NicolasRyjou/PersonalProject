


var crane = document.querySelector('canvas');
var crane_draw = crane.getContext('2d');
crane_draw.beginPath();


function create_whole_arm(){
    create_base(0, 0, 600, 400, 1);
    create_arm1(0, 0, 600, 400,1);
    create_arm2(0, 0, 600, 400,1);
}

function create_base(x, y, width, height, color) {
    crane_draw.fillRect(x + width/2 - width/5, y + height/5 - 50, 100, 45); // top rectangle
    crane_draw.fillRect(x + width/2 - width/5 + 33, y + height/5 - 0, 33, 10); // connection between
    crane_draw.fillRect(x + width/2 - width/5, y + height/5, 100, 50); // lower rectangle
}

function create_arm1(x, y, width, height, color) {
    crane_draw.arc(x + width/2 - width/5, y + height/5, 50, 0, Math.PI * 2, true);
    crane_draw.fillRect(x + width/2 - width/5, y + height/5 - 50, 100, 45);
    crane_draw.fillRect(x + width/2 - width/5 + 33, y + height/5 - 0, 33, 10);
    crane_draw.fillRect(x + width/2 - width/5, y + height/5 + 5, 100, 50);
}

function create_arm2(x, y, width, height, color) {
    crane_draw.arc(x + width/2 - width/5, y + (height/5 * 4), 50, 0, Math.PI * 2, true);
    crane_draw.fillRect(x + width/2 - width/5, y + height/5 - 50, 100, 45);
    crane_draw.fillRect(x + width/2 - width/5 + 33, y + height/5 - 0, 33, 10);
    crane_draw.fillRect(x + width/2 - width/5, y + height/5 + 5, 100, 50);
}

create_whole_arm();

//function drawCrane(var x,var y){
//}

