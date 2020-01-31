interface SolutionInterface {
  numberToGuess: number,
  highestNumber:number
}

export class Solution implements SolutionInterface {
  numberToGuess:number;
  highestNumber:number;
  constructor(highest:number) {
    this.highestNumber = highest;
    this.numberToGuess = Math.floor((Math.random()*this.highestNumber)+1);
  }
  guess(n:number) {
    if (this.numberToGuess < n) {
      return -1
    }
    if (this.numberToGuess > n) {
      return 1
    }
    if (this.numberToGuess === n) {
      return 0
    }
    else {
      return TypeError();
    }
  }

  guessNumber() {
    console.log(`Attempting to guess ${this.numberToGuess} using binary search...`);
    let low = 1;
    let high = this.highestNumber;
    let mid; 
    let midGuess;
    while (low <= high) {
      console.log(`Guessing a number from ${low} to ${high}...`);
      mid = Math.floor((low+high)/2);
      console.log(`My Guess is ${mid}!`);
      midGuess = this.guess(mid);
      if (midGuess === 0){
        console.log(`Guess is correct! ${mid} is the answer!`);
        return mid;
      }
      if (midGuess === -1) {
        console.log(`Too High! Guess Again!`)
        high = mid -1;
        continue;
      }
      if (midGuess === 1) {
        console.log(`Too Low! Guess Again!`)
        low = mid + 1;
        continue;
      }
    }
    return null;
  }
}

export const guessingGame = function(n:number) {
  return new Solution(n).guessNumber();
}

export const timedGuessingGame = function(n:number) {
  let timerStart = Date.now();
  guessingGame(n);
  let timerEnd = Date.now();
  let timeToExecute = timerEnd - timerStart;
  console.log(`Game completed in ${timeToExecute}ms.`);
  return timeToExecute;
}
