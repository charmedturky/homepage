const canvas = document.getElementById("canvas")
canvas.widht = window.innerWidth;
canvas.height = window.innerHeight;

const gc = canvas.getContext("2d");

const BG_color = "#00aee3"
const enemy_speed = 3;
var enemy_spawned = false;
const distance = window.innerHeight/3;
let count = 0 

setInterval(() => {enemy_speed += 0,3}, 4000);

const player = {
    color: "#ffff00",
    size: window.innerHeight/10,
    x: window.innerWidth/5,
    y: window.innerHeight/2-window.innerWidth/10/2,
    gravity: 0
}

const enemy = [

    {color: "#00db04",
    widht: window.innerWidth/7,
    height: 0,
    y: 0, 
    x: window.innerWidth},

    {color: "#00db04",
    widht: window.innerWidth/7,
    height: 0,
    y: 0, 
    x: window.innerWidth}

]

document.addEventListener("keypress", event => {

    if(event.code === "Space")
        player.gravity = window.innerHeight/80 *-1;
})




spawnEnemies()
update();

function update(){

    if (count > 100) {
        return
    }
    count
    requestAnimationFrame(update);

    // löschen
    gc.fillStyle = BG_color;
    gc.fillRect(0, 0, window.innerWidth, window.innerHeight);

    // spielre malen
    gc.fillStyle = player.color;
    gc.fillRect(player.x, player.y, player.size, player.size);

    // zieh spieler nach unten
    player.y += player.gravity;
    player.gravity += window.innerHeight/100/15;


    
    
    enemy.forEach(nmy => {
        gc.fillStyle = enemy[0].color;
        gc.fillRect(nmy.x, nmy.y, nmy.widht, nmy.height );
        nmy.x -= enemy_speed; 
    })



}

function spawnEnemies(){



    if(enemy_spawned === true)
        return;

    enemy[0].x = window.innerWidth;
    enemy[1].x = window.innerWidth;
    enemy[0].y = 0;
    enemy[0].height = Math.random() * (window.innerHeight - distance);
    enemy[1].y = enemy[0].height + distance;
    enemy[1].height = window.innerHeight - enemy[1].y
    enemy_spawned = true ;
}

