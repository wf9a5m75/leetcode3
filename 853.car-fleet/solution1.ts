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
