function grayCode(n: number): number[] {
    let result:number[] = [];

    for (let i:number = 0; i < (1 << n); i++) {
        result.push(i ^ (i >> 1));
    }

    return result;
};
