#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === null) {
      this.print();
    } else if (c === 'C') {
      for (let i = 0; i < this.size; i++) {
        let container = [];
        for (let j = 0; j < this.size; j++) {
          container += 'C';
        }
        console.log(container);
      }
    }
  }
}
module.exports = Square;
