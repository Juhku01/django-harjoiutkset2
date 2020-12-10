var player1 = prompt("Player One: Enter Your Name, you will be Blue");
var Player1Color = 'rbg(86, 15, 255)';

var player2 = prompt("Player Two: Enter Your Name, you will be Red");
var Player2Color = 'rbg(237, 45, 73)';

var game_on = true;
var table = $('table tr');

function reportWin(rowNum,colNum){
    console.log('You won starting at this row,col');
    console.log(rowNum);
    console.log(colNum);
}

function changeColor(rowIndex,colIndex,color){
    return table.eq(rowIndex).find("td").eq(colIndex).find('button').css('background-color',color);
    
}
function returnColor(rowIndex,colIndex,color){
    return table.eq(rowIndex).find("td").eq(colIndex).find('button').css('background-color');
    
}

function checkBottom(colIndex){
    var colorReport = returnColor(5,colIndex);
    
        for (var row = 5; row > -1; row --){
            colorReport=returnColor(row,colIndex);
            if(colorReport === 'rgb(128, 128, 128)') {
            return row
            }
        }
     
}
function colorMatchCheck(one,two,three,four){
    return(one === two && one === three && one === four && one !=='rgb(128, 128, 128)'&& one !== undefined)
}

for(var col =0; col < 5; col++){
    for(var row =0; row <7; row++){
        if(colorMatchCheck(returnColor(row,col),returnColor(row+1,col+1) ,returnColor(row+2,)))
        console.log("diag");
        reportWin(row,col);
        return true;
    }else if(colorMatchCheck(returnColor(row,col), returnColor(row-1, col+1) ,returnColor))
    console.log('diag');
    reportWin(row,col);
    return true;
}else {
    countinue;
}
}