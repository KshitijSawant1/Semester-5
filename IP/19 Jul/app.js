// Define a function to get the square of a number
console.log("Define a function to get the square of a number");
function getSqr(num) {
  sqrnumber = num * num;
  console.log(`The square of ${num} is ${sqrnumber}`);
}
getSqr(5);
getSqr(7);

// Define a function to get the add two numbers
console.log("Define a function to get the add two numbers");
function addnums(num1, num2) {
  sum = num1 + num2;
  console.log(`The Sum of ${num1} and ${num2} is ${sum}`);
  return sum;
}
addnums(addnums(7, 9), 5);

//Define Factorial of a number using for loop
console.log("Define Factorial of a number using for loop");
function fact(num) {
  fact = 1;
  for (i = 1; i <= num; i++) {
    fact = fact * i;
  }
  console.log(`The Factorial of ${num} is ${fact}`);
  return fact;
}
fact(5);

// Define fibonnacci Series till n
console.log("Define Fibonacci Series till n");
function fib(n) {
  console.log(`The Fibonacci Series of ${n} terms is:`);
  let a = 0,
    b = 1;
  if (n >= 1) console.log(a);
  if (n >= 2) console.log(b);
  for (let i = 3; i <= n; i++) {
    let c = a + b;
    console.log(c);
    a = b;
    b = c;
  }
}

fib(5);

//Write a recursive function to get total Cans
console.log("Write a recursive function to get total Cans ");
function getTotalCans(cans) {
  if (cans < 6) return cans;

  const free = Math.floor(cans / 6);
  const remaining = cans % 6;

  return cans + getTotalCans(free + remaining);
}

// Examples
console.log(getTotalCans(6));
console.log(getTotalCans(36));

//Create a tic-tac-toe game using node js
//npm install prompt-sync

//Create a tic-tac-toe game using node js
//npm install prompt-sync
// num = prompt("Enter number: ")
// console.log(`Square of ${num} is ${num * num}`);

const prompt = require("prompt-sync")();

board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

function printBoard(board) {
  console.clear();
  for (let i = 0; i < 3; i++) {
    output = ``;
    for (let j = 0; j < 3; j++) output += `${board[i][j]} \t`;
    console.log(output);
  }
}

printBoard(board);

for (let i = 1; i < 10; i++) {
  player = i % 2 == 1 ? "X" : "O";
  pos = Number(prompt(`Player ${player}: Enter position: `));

  switch (pos) {
    case 1:
      board[0][0] = player;
      break;
    case 2:
      board[0][1] = player;
      break;
    case 3:
      board[0][2] = player;
      break;
    case 4:
      board[1][0] = player;
      break;
    case 5:
      board[1][1] = player;
      break;
    case 6:
      board[1][2] = player;
      break;
    case 7:
      board[2][0] = player;
      break;
    case 8:
      board[2][1] = player;
      break;
    case 9:
      board[2][2] = player;
      break;
  }

  printBoard(board);

  if (checkWinPattern(board)) {
    console.log(`Player ${player} is winner`);
    break;
  }
}

function checkWinPattern(board) {
  if (board[0][0] == board[0][1] && board[0][0] == board[0][2]) return true;
  if (board[1][0] == board[1][1] && board[1][0] == board[1][2]) return true;
  if (board[2][0] == board[2][1] && board[2][0] == board[2][2]) return true;
  if (board[0][0] == board[1][0] && board[0][0] == board[2][0]) return true;
  if (board[0][1] == board[1][1] && board[0][1] == board[2][1]) return true;
  if (board[0][2] == board[1][2] && board[0][2] == board[2][2]) return true;
  if (board[0][0] == board[1][1] && board[0][0] == board[2][2]) return true;
  if (board[2][0] == board[1][1] && board[2][0] == board[0][2]) return true;

  return false;
}
