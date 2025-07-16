for (let i = 1; i <= 20; i++) {
  if (i % 5 === 0) {
    if (i % 3 === 0) {
      console.log(`Number: Fizz & Buzz`);
    }
    console.log(`Number: Buzz`);
  } else if (i % 3 === 0) {
    console.log(`Number: Fizz`);
  } else {
    console.log(`Number: ${i}`);
  }
}
