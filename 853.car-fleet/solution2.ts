class Car {
  constructor(
      public readonly position: number,
      public readonly speed: number,
  ) {
      Object.freeze(this);
  }
}
class Fraction {
  public readonly numerator: number;
  public readonly denominator: number;

  constructor(
      numerator: number = 0,
      denominator: number = 1,
  ) {
      if (denominator === 0) {
          this.numerator = 0;
          this.denominator = 1;
          return;
      }
      const common = this.gcd(numerator, denominator);
      this.numerator = Math.floor(numerator / common);
      this.denominator = Math.floor(denominator / common);
      Object.freeze(this);
  }
  
  private gcd(
      a: number,
      b: number,
  ): number {
      if (a > b) {
          return this.gcd(b, a);
      }
      
      let x = a % b;
      while (x !== 0) {
          a = b;
          b = x;
          x = a % b;
      }
      return b;
  }

  isLessThanOrEqual(other): boolean {
      return this.compare(other) <= 0;
  }

  private compare(other: Fraction): number {
      // Return 1 if this fraction is greater than other one.
      // Return 0 if this and other one are the same.
      // Return 1 if this is less than other one.
      
      const common = this.denominator * other.denominator;
      const myNum = this.numerator * (common / this.denominator);
      const otherNum = other.numerator * (common / other.denominator);
      if (myNum > otherNum) {
          return 1;
      } else if (myNum === otherNum) {
          return 0;
      }
      return -1;
  }
}

function carFleet(target: number, position: number[], speed: number[]): number {
  const carNums = position.length;
  const cars: Car[] = [];
  for (let i = 0; i < carNums; i++) {
      cars.push(new Car(position[i], speed[i]));
  }
  
  // position, speedの順にソート
  cars.sort((a, b) => {
      const delta = a.position - b.position;
      if (delta !== 0) {
          return delta;
      }
      return a.speed - b.speed;
  });
  
  // targetに近い順に予想時間を計算する
  // もし1つ前に車の予想時間よりも短い場合は、前の車に追いつく（追い抜けない）ので
  // fleetになる
  let fleets = 1;
  let aheadCar = calcEta(cars[carNums - 1], target);
  
  for (let i = carNums - 2; i >= 0; i--) {
      const eta = calcEta(cars[i], target);
      if (eta.isLessThanOrEqual(aheadCar)) {
          continue;
      }
      fleets++;
      aheadCar = eta;
  }
  
  return fleets;
};

function calcEta(car: Car, target: number): Fraction {
  const numerator = target - car.position;
  const denominator = car.speed;
  return new Fraction(numerator, denominator);
};
