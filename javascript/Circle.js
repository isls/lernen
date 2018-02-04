function Circle (x, y, r) {
  function squared () {
    return Math.pow(r, 2);
  }
  function area () {
    return Math.PI * squared();
  }
  return {
    area: area
  };
}
module.exports = Circle;
