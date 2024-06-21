# step1: とりあえず解いてみる (レビューされ済み)

## 時間計算量: O(n log n)
- n は車の数
- 位置を揃えるためにソートしているので、`O(n log n)`
  
## 空間計算量: O(n)
- 全ての車が前の車を追い越さない場合(最悪ケース)、`stack`に全部溜まるので`O(n)`

```python
from typing import List

class Car:
    def __init__(self, position: int, speed: int):
        self.position = position
        self.speed = speed


    def estimate(self, target: int) -> int:
        return (target - self.position) / self.speed


    def __lt__(self, other) -> bool:
        return self.position <= other.position


    def __repr__(self) -> str:
        return f"[p:{self.position}, s:{self.speed}]"

class Solution:
    def carFleet(self,
                    target: int,
                    position: List[int],
                    speed: List[int]) -> int:

        cars: List[Car] = []
        number_of_cars: int = len(position)
        for i in range(number_of_cars):
            cars.append(Car(position[i], speed[i]))
        cars.sort()

        estimates = list(map(lambda car : car.estimate(target), cars))

        stack: List[int] = []
        for i in range(number_of_cars - 1, - 1, - 1):
            if not stack or stack[ - 1] < estimates[i]:
                stack.append(estimates[i])

        return len(stack)
```

------------------------------

# step2: zip関数を使う(レビューされ済み)

## 時間計算量: O(n log n)
- `step1`と同じなので省略

## 空間計算量: O(n)
- `zip()`が新しい配列を生成しているので、結果的に`O(n)`
- 全ての車が前の車を追い越さない場合(最悪ケース)、`stack`に全部溜まるので`O(n)`

```python
from typing import List

class Solution:
    def carFleet(self,
                    target: int,
                    position: List[int],
                    speed: List[int]) -> int:

        # Combine the position and speed values,
        # then reverse sort them.
        # 
        # This denotes sort cars by position.
        cars = sorted(zip(position, speed), reverse = True)

        # Pile cars which faster than the other cars.
        stack: List[int] = []
        for position, speed in cars:
            estimate = (target - position) / speed
            if not stack or stack[ - 1] < estimate:
                stack.append(estimate)

        return len(stack)
```

------------------------------

# step3: いろいろと不便なTypeScriptで書いてみる(ライブラリに頼らない)

## 時間計算量: O(n log n)
- `step1`と同じなので省略

## 空間計算量: O(n)
- `step1`では`stack`を使っていたのを止めて、カウントだけにした。
- でも`cars`で新しい配列を生成しているので、結果的に`O(n)`

## メモ：
- TypeScriptは若干面倒。でも不便だから勉強になる。

```typescript
type Car = [number, number];
function carFleet(target: number, position: number[], speed: number[]): number {
    const car_nums = position.length;
    
    // pythonのzip関数はないので、自分で行う
    const cars: Car[] = [];  // 0: position, 1: speed
    for (let i = 0; i < car_nums; i++) {
        cars.push([position[i], speed[i]]);
    }
    
    // position, speedの順にソート
    cars.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    });
    
    // targetに近い順に予想時間を計算する
    // もし1つ前に車の予想時間よりも短い場合は、前の車に追いつく（追い抜けない）ので
    // fleetになる
    let fleets = 0;
    let ahead_car_eta = 0;
    
    for (let i = car_nums - 1; i >= 0; i--) {
        const eta = (target - cars[i][0]) / cars[i][1];
        if (ahead_car_eta >= eta) {
            continue;
        }
        ahead_car_eta = eta;
        fleets++;
    }
    
    return fleets;
};

function calc_eta(car: Car, target: number): [number, number] {
    const numerator = target - car[0];
    const denominator = car[1];
    return [Math.floor(numerator / denominator), numerator % denominator];
};
```

------------------------------

# step4: 有理数でやるべし、とのレビューに応えてみる

## 時間計算量: O(n log n)
- 省略

## 空間計算量: O(n)
- 省略

## メモ：
- 基本的に `snakeCase`で書きたい人なので、`snakeCase`に書き直した。
- Carを配列から、クラスにした。やはりこちらのが読みやすい。
- Fractionを実装（LeetCodeには外部のライブラリは持ち込めない）。改めて、面倒だなー、と思いつつ、久しぶりに`gcd`とか書いて（若干ウル覚えだったので）爽やかな気分。
- Tech interviewは、チョイスがあるなら、Pythonにしようと改めて誓う。

```typescript
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
```

------------------------------------

# step5: Pythonで書き直してみる

## 所要時間
- 4分

```python
from fractions import Fraction
from typing import List

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ahead_car = Fraction()
        fleets = 0
        for position, speed in sorted(zip(position, speed), reverse=True):
            eta = Fraction(target - position, speed)
            if ahead_car >= eta:
                continue
            ahead_car = eta
            fleets += 1
        return fleets
```